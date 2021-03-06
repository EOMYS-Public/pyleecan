# -*- coding: utf-8 -*-
from os.path import join

from numpy import zeros

from ....Functions.FEMM.draw_FEMM import draw_FEMM
from ....Classes._FEMMHandler import _FEMMHandler
from ....Classes.OutMagFEMM import OutMagFEMM


def comp_flux_airgap(self, output, axes_dict):
    """Build and solve FEMM model to calculate and store magnetic quantities

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    output : Output
        an Output object
    axes_dict: {Data}
        Dict of axes used for magnetic calculation

    Returns
    -------
    out_dict: dict
        Dict containing the following quantities:
            Br : ndarray
                Airgap radial flux density (Nt,Na) [T]
            Bt : ndarray
                Airgap tangential flux density (Nt,Na) [T]
            Tem : ndarray
                Electromagnetic torque over time (Nt,) [Nm]
            Phi_wind_stator : ndarray
                Stator winding flux (qs,Nt) [Wb]
            meshsolution: MeshSolution
                MeshSolution object containing magnetic quantities B, H, mu for each time step
    """

    # Init output
    out_dict = dict()
    if output.mag.internal is None:
        output.mag.internal = OutMagFEMM()

    # Get time and angular axes
    Angle = axes_dict["Angle"]
    Time = axes_dict["Time"]

    # Set the angular symmetry factor according to the machine and check if it is anti-periodic
    sym, is_antiper_a = Angle.get_periodicity()

    # Import angular vector from Data object
    angle = Angle.get_values(
        is_oneperiod=self.is_periodicity_a,
        is_antiperiod=is_antiper_a and self.is_periodicity_a,
    )
    Na = angle.size

    # Check if the time axis is anti-periodic
    _, is_antiper_t = Time.get_periodicity()

    # Number of time steps
    time = Time.get_values(
        is_oneperiod=self.is_periodicity_t,
        is_antiperiod=is_antiper_t and self.is_periodicity_t,
    )
    Nt = time.size

    # Get rotor angular position
    angle_rotor = output.get_angle_rotor()[0:Nt]

    # Interpolate current on magnetic model time axis
    # Get stator current from elec out
    if self.is_mmfs:
        Is = output.elec.comp_I_mag(time, is_stator=True)
    else:
        Is = None
    # Get rotor current from elec out
    if self.is_mmfr:
        Ir = output.elec.comp_I_mag(time, is_stator=False)
    else:
        Ir = None

    # Setup the FEMM simulation
    # Geometry building and assigning property in FEMM
    # Instanciate a new FEMM
    femm = _FEMMHandler()
    output.mag.internal.handler_list.append(femm)
    if self.import_file is None:
        self.get_logger().debug("Drawing machine in FEMM...")
        FEMM_dict = draw_FEMM(
            femm,
            output,
            is_mmfr=self.is_mmfr,
            is_mmfs=self.is_mmfs,
            sym=sym,
            is_antiper=is_antiper_a,
            type_calc_leakage=self.type_calc_leakage,
            is_remove_vent=self.is_remove_vent,
            is_remove_slotS=self.is_remove_slotS,
            is_remove_slotR=self.is_remove_slotR,
            type_BH_stator=self.type_BH_stator,
            type_BH_rotor=self.type_BH_rotor,
            kgeo_fineness=self.Kgeo_fineness,
            kmesh_fineness=self.Kmesh_fineness,
            user_FEMM_dict=self.FEMM_dict_enforced,
            path_save=self.get_path_save_fem(output),
            is_sliding_band=self.is_sliding_band,
            transform_list=self.transform_list,
            rotor_dxf=self.rotor_dxf,
            stator_dxf=self.stator_dxf,
        )
    else:
        self.get_logger().debug("Reusing the FEMM file: " + self.import_file)
        FEMM_dict = self.FEMM_dict_enforced

    # Init flux arrays in out_dict
    out_dict["Br"] = zeros((Nt, Na))
    out_dict["Bt"] = zeros((Nt, Na))
    # Init torque array in out_dict
    out_dict["Tem"] = zeros((Nt))
    # Init stator winding flux array in out_dict
    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        qs = output.simu.machine.stator.winding.qs  # Winding phase number
        out_dict["Phi_wind_stator"] = zeros((Nt, qs))

    # Solve for all time step and store all the results in out_dict
    if self.nb_worker > 1:
        # With parallelization
        B_elem, H_elem, mu_elem, meshFEMM, groups = self.solve_FEMM_parallel(
            femm,
            output,
            out_dict,
            FEMM_dict=FEMM_dict,
            sym=sym,
            Nt=Nt,
            angle=angle,
            Is=Is,
            Ir=Ir,
            angle_rotor=angle_rotor,
        )
    else:
        # Without parallelization
        B_elem, H_elem, mu_elem, meshFEMM, groups = self.solve_FEMM(
            femm,
            output,
            out_dict,
            FEMM_dict=FEMM_dict,
            sym=sym,
            Nt=Nt,
            angle=angle,
            Is=Is,
            Ir=Ir,
            angle_rotor=angle_rotor,
            is_close_femm=self.is_close_femm,
            filename=self.import_file,
        )

    # Store FEMM_dict in out_dict if FEMM file is not imported
    if self.import_file is None:
        output.mag.internal.FEMM_dict = FEMM_dict

    # Store FEMM mesh results in meshsolution
    if self.is_get_mesh:
        # Build MeshSolution object and store it in out_dict
        out_dict["meshsolution"] = self.build_meshsolution(
            Nt, meshFEMM, Time, B_elem, H_elem, mu_elem, groups
        )
        # Save meshsolution as .h5 on disk if requested
        if self.is_save_FEA:
            save_path = output.get_path_result()
            save_path_fea = join(save_path, "MeshSolutionFEMM.h5")
            out_dict["meshsolution"].save(save_path_fea)

    return out_dict
