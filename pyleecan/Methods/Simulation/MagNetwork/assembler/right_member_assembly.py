# -*- coding: utf-8 -*-
import time
import numpy as np
from scipy.sparse import coo_matrix


def right_member_assembly(
    self,
    list_permeability_cell,  # cells materials
    Num_Unknowns,
    list_elem,
    list_coord,
    reluc_list,
    Br,
    material_dict,
    mask_magnet,
    la,
    type_coord_sys,
    JA=None,
    JB=None,
    JC=None,
):

    #######################################################################################
    # Defining the geometry material properties
    #######################################################################################
    # Get machine object
    Machine = self.parent.machine

    if Machine.comp_periodicity_spatial()[1] == True:
        periodicity = Machine.comp_periodicity_spatial()[0]
    else:
        periodicity = Machine.comp_periodicity_spatial()[0] / 2

    # Number of PMs per period
    nb_PM_per_period = round(Machine.rotor.get_pole_pair_number() / periodicity)

    # Number of stator teeth per period
    nb_stator_teeth_per_period = round(Machine.stator.get_Zs() / (2 * periodicity))

    # Relative permeabiltity of the PMs
    mur_PM = []
    for i in range(nb_PM_per_period):
        mur_PM.append(material_dict["PM" + str(i + 1)])

    # Relative permeabiltity of the stator windings
    mur_windings = []
    for j in range(nb_stator_teeth_per_period):
        mur_windings.append(material_dict["winding" + str(j + 1)])

    #######################################################################################
    # Modeling the PM regions and calculating the FEMM (PM), PM_Magnetization_Direction = y
    #######################################################################################

    # Masking the magnet : mask_magnet is true if the permeability is equal to mur_PM
    # mask_magnet = list_permeability_cell == mur_PM[0]
    # mask_magnet_1p = []
    # for ii in range(nb_PM_per_period):
    #     mask_magnet_1p[str(ii)] = mask_magnet[ii]

    N_unknowns = Num_Unknowns.max() + 1

    # Calculation of the phi_PM according to the coordinate system type
    # Linear : Ref 1: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9473194
    if type_coord_sys == 1:

        h_x = np.linalg.norm(
            list_coord[list_elem[:, 0]] - list_coord[list_elem[:, 1]], axis=1, ord=2
        )  # step according to x

        h_y = np.linalg.norm(
            list_coord[list_elem[:, 1]] - list_coord[list_elem[:, 2]], axis=1, ord=2
        )  # step according to y

        phi_PM = 2 * Br * h_y[mask_magnet] * la / mur_PM[0]

    # Radial: Ref 2: https://www.researchgate.net/publication/269405270_Modeling_of_a_Radial_Flux_PM_Rotating_Machine_using_a_New_Hybrid_Analytical_Model
    elif type_coord_sys == 2:

        R1 = list_coord[list_elem[:, 0], 1]

        R2 = list_coord[list_elem[:, -1], 1]

        sigma_R = np.abs(R2 - R1)  # step according to r

        sigma_theta = np.abs(
            list_coord[list_elem[:, 1], 0] - list_coord[list_elem[:, 0], 0]
        )  # step according to theta

        for kk in range(nb_PM_per_period):
            # Determination of the direction of the magnet magnetization
            if (kk % 2) == 0:
                Magnetization = +1  # positive magnetization direction
            else:
                Magnetization = -1  # negative magnetization direction

            # Determine the flux of the one magnet
            phi_PM = (
                Magnetization
                * 2
                * Br
                * sigma_R[mask_magnet["PM" + str(kk + 1)]]
                * la
                / mur_PM[kk]
            )

        # Initialize returned vector -> RHS
        RHS = np.zeros(N_unknowns, dtype=np.float64)

        # Permanant Magnet assembling
        index_unknowns_1 = Num_Unknowns[list_elem[mask_magnet, 0]]
        index_unknowns_2 = Num_Unknowns[list_elem[mask_magnet, 1]]
        index_unknowns_3 = Num_Unknowns[list_elem[mask_magnet, 2]]
        index_unknowns_4 = Num_Unknowns[list_elem[mask_magnet, 3]]

        RHS[index_unknowns_1] += phi_PM * reluc_list[mask_magnet, 3]
        RHS[index_unknowns_2] -= phi_PM * reluc_list[mask_magnet, 1]
        RHS[index_unknowns_3] -= phi_PM * reluc_list[mask_magnet, 1]
        RHS[index_unknowns_4] += phi_PM * reluc_list[mask_magnet, 3]

    #######################################################################################
    # Calculating the contribution of the windings in the RHS
    #######################################################################################

    if JA is None and JB is None and JC is None:
        # Phase 1
        mask_winding = list_permeability_cell == mur_windings[0]

        if type_coord_sys == 1:
            S = h_x[mask_winding] * h_y[mask_winding] / 4
        elif type_coord_sys == 2:
            S = (
                0.5
                * sigma_theta[mask_winding]
                * (R2[mask_winding] ** 2 - R1[mask_winding] ** 2)
                / 4
            )

        index_unknowns_1 = Num_Unknowns[list_elem[mask_winding, 0]]
        index_unknowns_2 = Num_Unknowns[list_elem[mask_winding, 1]]
        index_unknowns_3 = Num_Unknowns[list_elem[mask_winding, 2]]
        index_unknowns_4 = Num_Unknowns[list_elem[mask_winding, 3]]

        RHS[index_unknowns_1] += JA * S
        RHS[index_unknowns_2] += JA * S
        RHS[index_unknowns_3] += JA * S
        RHS[index_unknowns_4] += JA * S

        # Phase 2
        mask_winding = list_permeability_cell == mur_windings[1]
        # here to be changed by the winding number bob1, bob2..

        if type_coord_sys == 1:
            S = h_x[mask_winding] * h_y[mask_winding] / 4
        elif type_coord_sys == 2:
            S = (
                0.5
                * sigma_theta[mask_winding]
                * (R2[mask_winding] ** 2 - R1[mask_winding] ** 2)
                / 4
            )

        index_unknowns_1 = Num_Unknowns[list_elem[mask_winding, 0]]
        index_unknowns_2 = Num_Unknowns[list_elem[mask_winding, 1]]
        index_unknowns_3 = Num_Unknowns[list_elem[mask_winding, 2]]
        index_unknowns_4 = Num_Unknowns[list_elem[mask_winding, 3]]

        RHS[index_unknowns_1] += JB * S
        RHS[index_unknowns_2] += JB * S
        RHS[index_unknowns_3] += JB * S
        RHS[index_unknowns_4] += JB * S

        ###Phase 3
        mask_winding = list_permeability_cell == mur_windings[2]
        if type_coord_sys == 1:
            S = h_x[mask_winding] * h_y[mask_winding] / 4
        elif type_coord_sys == 2:
            S = (
                0.5
                * sigma_theta[mask_winding]
                * (R2[mask_winding] ** 2 - R1[mask_winding] ** 2)
                / 4
            )

        index_unknowns_1 = Num_Unknowns[list_elem[mask_winding, 0]]
        index_unknowns_2 = Num_Unknowns[list_elem[mask_winding, 1]]
        index_unknowns_3 = Num_Unknowns[list_elem[mask_winding, 2]]
        index_unknowns_4 = Num_Unknowns[list_elem[mask_winding, 3]]

        RHS[index_unknowns_1] += JC * S
        RHS[index_unknowns_2] += JC * S
        RHS[index_unknowns_3] += JC * S
        RHS[index_unknowns_4] += JC * S
    # np.savetxt("Everif.csv",RHS.reshape((50,60)),fmt="%5.2f")

    return RHS
