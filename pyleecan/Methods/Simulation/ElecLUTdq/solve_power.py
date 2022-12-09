import numpy as np


def solve_power(self, LUT, Rs):
    """Solve EEC to achieve given input / output power with respect to voltage and current constraints

    Parameters
    ----------
    self : ElecLUTdq
        a ElecLUTdq object
    LUT : LUTdq
        Calculated look-up table
    Rs: float
        Stator phase resistance [Ohm]

    Returns
    ----------
    out_dict: dict
        Dict containing all output quantities

    """

    # Get output, machine and OP
    output = self.parent.parent

    machine = output.simu.machine
    OP = output.elec.OP

    # Maximum voltage
    Urms_max = self.Urms_max
    # Maximum current
    Irms_max = self.Irms_max
    # Electrical frequency
    felec = OP.get_felec()
    # Electrical pulsation
    ws = 2 * np.pi * felec
    # Stator winding number of phases
    qs = machine.stator.winding.qs

    # Check if there is a loss model
    is_loss_model = LUT.simu.loss is not None

    # iteration until convergence is reached, and max number of iterations on EEC
    delta_Pem = 1e10
    delta_Pem_max = 0.1
    Nmax = 20
    niter_Pem = 1
    Id_min = self.Id_min
    Id_max = self.Id_max
    Iq_min = self.Iq_min
    Iq_max = self.Iq_max
    Nd = (
        self.n_Id
        if self.n_Id == 1
        else int(self.n_Id * self.n_interp / (self.n_Id + self.n_Iq))
    )
    Nq = (
        self.n_Iq
        if self.n_Iq == 1
        else int(self.n_Iq * self.n_interp / (self.n_Id + self.n_Iq))
    )
    while abs(delta_Pem) > delta_Pem_max and niter_Pem < Nmax:

        # Refine Id/Iq mesh
        Id_vect = np.linspace(Id_min, Id_max, Nd)
        Iq_vect = np.linspace(Iq_min, Iq_max, Nq)
        Id, Iq = np.meshgrid(Id_vect, Iq_vect)
        Id, Iq = Id.ravel(), Iq.ravel()

        # Calculate maximum current
        Imax_interp = np.sqrt(Id ** 2 + Iq ** 2)

        # Interpolate Phid/Phiq on the refined mesh
        (Phid, Phiq, Phih) = LUT.interp_Phi_dqh(Id, Iq)

        # Calculate voltage (Ud/Uq) for the refined mesh
        Ud = Rs * Id - Phiq * ws
        Uq = Rs * Iq + Phid * ws
        Umax_interp = np.sqrt(Ud ** 2 + Uq ** 2)

        if is_loss_model:
            # Interpolate losses from LUT:
            # - 1st column : Joule losses
            # - 2nd column : stator core losses
            # - 3rd column : magnet losses
            # - 4th column : rotor core losses
            # - 5th column : proximity losses
            Ploss_dqh = LUT.interp_Ploss_dqh(Id, Iq, N0=OP.N0)
            Ploss_ovl = np.sum(Ploss_dqh, axis=1)
        else:
            # Only consider stator Joule losses
            Ploss_ovl = qs * Rs * (Id ** 2 + Iq ** 2)

        if is_loss_model:
            # The input power must cover electrical power + additional losses
            P_in = qs * (Ud * Id + Uq * Iq) + np.sum(Ploss_dqh[:, 1:], axis=1)
        else:
            # The input power must cover electrical power + Joule losses
            P_in = qs * (Ud * Id + Uq * Iq)

        # The output power is the input power minus all losses
        P_out = P_in - Ploss_ovl

        # Set input/ouput power condition
        if OP.Pem_av_in is None:
            P_cond = P_out >= OP.Pem_av_ref
        else:
            P_cond = P_in >= OP.Pem_av_in

        # Set maximum voltage condition
        U_cond = Umax_interp <= Urms_max

        # Set maximum current condition
        I_cond = Imax_interp <= Irms_max

        # Finding indices of operating points satisfying voltage, current and power conditions
        i0 = np.logical_and.reduce((U_cond, I_cond, P_cond))

        if np.any(i0):
            # Finding index of operating point with lowest losses among feasible operating points
            imin = np.argmin(Ploss_ovl[i0])

            # Get error between calculated and requested powers
            if OP.Pem_av_in is None:
                delta_Pem = P_out[i0][imin] - OP.Pem_av_ref
            else:
                delta_Pem = P_in[i0][imin] - OP.Pem_av_in

            if abs(delta_Pem) > delta_Pem_max:
                # Zoom in Id / Iq grid to achieve better accuracy on output values
                jd = np.where(Id_vect == Id[i0][imin])[0][0]
                jq = np.where(Iq_vect == Iq[i0][imin])[0][0]

                jd_min = max([jd - 1, 0])
                jd_max = min([jd + 1, Nd - 1])
                jq_min = max([jq - 1, 0])
                jq_max = min([jq + 1, Nq - 1])

                Id_min = Id_vect[jd_min]
                Id_max = Id_vect[jd_max]
                Iq_min = Iq_vect[jq_min]
                Iq_max = Iq_vect[jq_max]

            niter_Pem = niter_Pem + 1

        else:
            # Find strategy to get closest to requested power although violating voltage / current constraints
            i1 = np.logical_and(P_cond, U_cond)
            i2 = np.logical_and(P_cond, I_cond)

            if np.any(i1):
                # Only consider requested power and voltage constraint
                i0 = i1
            elif np.any(i2):
                # Only consider requested power and current constraint
                i0 = i2
            else:
                # Only consider requested power
                i0 = P_cond

            if np.any(i0):
                # Find indices of operating points that reaches power
                if OP.Pem_av_in is None:
                    P_min = np.min(P_out[i0])
                    P_cond = P_out == P_min
                else:
                    P_min = np.min(P_in[i0])
                    P_cond = P_out == P_min

                if np.where(P_cond)[0].size == 1:
                    # Take the only point that reaches requested power
                    imin = 0
                else:
                    # Take the operating point that minimizes voltage
                    imin = np.argmin(Umax_interp[i0])

                # Get error between calculated and requested powers
                if OP.Pem_av_in is None:
                    delta_Pem = P_out[i0][imin] - OP.Pem_av_ref
                else:
                    delta_Pem = P_in[i0][imin] - OP.Pem_av_in

                if abs(delta_Pem) > delta_Pem_max:
                    # Zoom in Id / Iq grid to achieve better accuracy on output values
                    jd = np.where(Id_vect == Id[i0][imin])[0][0]
                    jq = np.where(Iq_vect == Iq[i0][imin])[0][0]

                    jd_min = max([jd - 1, 0])
                    jd_max = min([jd + 1, Nd - 1])
                    jq_min = max([jq - 1, 0])
                    jq_max = min([jq + 1, Nq - 1])

                    Id_min = Id_vect[jd_min]
                    Id_max = Id_vect[jd_max]
                    Iq_min = Iq_vect[jq_min]
                    Iq_max = Iq_vect[jq_max]

                niter_Pem = niter_Pem + 1

            else:
                # Find operating point that get closest to requested power
                if OP.Pem_av_in is None:
                    P_max = np.max(P_out)
                    i0 = P_out == P_max
                else:
                    P_max = np.max(P_in)
                    i0 = P_out == P_max

                if np.where(i0)[0].size == 1:
                    # Take the closest point to requested power
                    imin = 0
                else:
                    # Take the operating point that minimizes voltage
                    imin = np.argmin(Umax_interp[i0])

                # Stop loop
                delta_Pem = delta_Pem_max

    # Launch warnings
    if OP.Pem_av_in is None and P_out[i0][imin] < OP.Pem_av_ref:
        self.get_logger().warning(
            "Output power cannot be reached within current and voltage constraints, taking maximum feasible power"
        )

    elif OP.Pem_av_in is not None and P_in[i0][imin] < OP.Pem_av_in:
        self.get_logger().warning(
            "Input power cannot be reached within current and voltage constraints, taking maximum feasible power"
        )

    if Umax_interp[i0][imin] > Urms_max:
        self.get_logger().warning("Voltage constraint cannot be reached")

    if Imax_interp[i0][imin] > Irms_max:
        self.get_logger().warning("Current constraint cannot be reached")

    # calculate and store some quantities
    if output.simu.input.is_generator:
        # Calculate torque from input power
        Tem = P_in[i0][imin] / (2 * np.pi * OP.N0 / 60)
    else:
        # Calculate torque from output power
        Tem = P_out[i0][imin] / (2 * np.pi * OP.N0 / 60)

    out_dict = self.solve_post(
        self, LUT, ws, Ud, Uq, Iq, Id, Phid, Phiq, P_in, P_out, Tem, i0, imin
    )

    if is_loss_model:
        # Store losses
        out_dict["Pjoule"] = Ploss_dqh[i0, 0][imin]
        out_dict["Pstator"] = Ploss_dqh[i0, 1][imin]
        out_dict["Pmagnet"] = Ploss_dqh[i0, 2][imin]
        out_dict["Protor"] = Ploss_dqh[i0, 3][imin]
        out_dict["Pprox"] = Ploss_dqh[i0, 4][imin]
    else:
        out_dict["Pjoule"] = Ploss_ovl[i0][imin]

    return out_dict
