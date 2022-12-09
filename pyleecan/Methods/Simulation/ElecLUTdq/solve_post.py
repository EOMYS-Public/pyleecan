from numpy import abs as np_abs


def solve_post(self, LUT, ws, Ud, Uq, Iq, Id, Phid, Phiq, P_in, P_out, Tem, i0, imin):
    """Some common post-processings after solving EEC.

    Parameters
    ----------
    self : ElecLUTdq
        a ElecLUTdq object
    LUT : LUTdq
        Calculated look-up table
    ws : float
        electrical pulsation
    Ud, Uq, Id, Iq : ndarrays
        dq axis voltages and currents
    Phid, PHiq : ndarrays
        dq axis fluxlinkages
    P_in, P_out : ndarrays
        input and output power
    Tem : float
        torque
    i0, imin : float
        operation point indices

    Returns
    ----------
    out_dict: dict
        Dict containing all output quantities

    """

    out_dict = dict()

    # Store power & torque
    out_dict["P_in"] = P_in[i0][imin]
    out_dict["P_out"] = P_out[i0][imin]
    out_dict["Tem_av"] = Tem

    # Calculate efficiency
    out_dict["efficiency"] = out_dict["P_out"] / out_dict["P_in"]

    # Store voltage and currents
    out_dict["Id"] = Id[i0][imin]
    out_dict["Iq"] = Iq[i0][imin]
    out_dict["Ud"] = Ud[i0][imin]
    out_dict["Uq"] = Uq[i0][imin]

    # Store dq fluxes
    out_dict["Phid"] = Phid[i0][imin]
    out_dict["Phiq"] = Phiq[i0][imin]

    # Calculate flux linkage and back-emf
    Phidqh_mag = LUT.get_Phi_dqh_mag_mean()
    out_dict["Phid_mag"] = Phidqh_mag[0]
    out_dict["Phiq_mag"] = Phidqh_mag[1]
    out_dict["Erms"] = ws * Phidqh_mag[0]

    # Calculate inductances
    if Id[i0][imin] != 0:
        out_dict["Ld"] = (Phid[i0][imin] - out_dict["Phid_mag"]) / Id[i0][imin]
    if Iq[i0][imin] != 0:
        out_dict["Lq"] = Phiq[i0][imin] / Iq[i0][imin]

    # Calculate torque ripple
    Tem_rip_pp = LUT.interp_Tem_rip_dqh(Id[i0][imin], Iq[i0][imin])
    if Tem_rip_pp is not None:
        out_dict["Tem_rip_pp"] = float(Tem_rip_pp)
        if out_dict["Tem_av"] == 0:
            out_dict["Tem_rip_norm"] = 0
        else:
            out_dict["Tem_rip_norm"] = np_abs(Tem_rip_pp / out_dict["Tem_av"])

    return out_dict
