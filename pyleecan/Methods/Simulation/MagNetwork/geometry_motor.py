# -*- coding: utf-8 -*-

# from tkinter.ttk import _TreeviewColumnDict
from tkinter import *
from turtle import st
import numpy as np
from scipy.fft import ifftn
import matplotlib.pyplot as plt
from collections import defaultdict


def geometry_motor(self, N_point_theta):
    """Define the discretized geometry of the electric machine under study

    Parameters
    ----------
    self : MagNetwork
        the MagNetwork object to update
    N_point_theta : integer
        Number of discretization points in the theta-direction
    N_point_r : integer
        Number of discretization points in the r-direction
    rotor_shift : integer (Default = 8)
        Number of rotor mesh cells to be shifted with respect to the stator

    Returns
    -------
    cells_materials: ndarray
        The permeability of each cell of the motor geometry
    material_dict : dict
        The permeabilities of the materials constituting the motor
    N_point_theta : integer
        Updated number of discretization points in the theta-direction according to condition 1
        {condition 1 :
        nb_stator_teeth_per_period * (stator_slot_elements_theta + 2 * half_stator_tooth_opening)
        = nb_PM_per_period * (magnet_elements_theta + 2 * half_airgap_PM) }
    """

    #######################################################################################
    # Definition of the general machine input parameters
    #######################################################################################

    # Getting the machine object
    Machine = self.parent.machine

    # Conversion
    # rad_to_deg = 180 / np.pi

    # Machine periodicity
    if Machine.comp_periodicity_spatial()[1] == True:
        periodicity = Machine.comp_periodicity_spatial()[0]
    else:
        periodicity = Machine.comp_periodicity_spatial()[0] / 2

    # Pole pitch angle
    # angle_tp = (np.pi / periodicity) * rad_to_deg
    angle_tp = np.pi / periodicity

    # Number of PMs per period
    nb_PM_per_period = round(Machine.rotor.get_pole_pair_number() / periodicity)

    # Number of stator teeth per period
    nb_stator_teeth_per_period = round(Machine.stator.get_Zs() / (2 * periodicity))

    # Number of winding layers
    nb_layers = Machine.stator.winding.Nlayer

    # Active length (m)
    # la = Machine.rotor.L1

    #######################################################################################
    # Material properties definition
    #######################################################################################

    # Permeability of vacuum (H/m)
    mu0 = np.pi * 4e-7

    # Relative permeability of air
    mu_air = 1

    # Relative permeability of the stator iron
    mu_stator = Machine.stator.mat_type.mag.mur_lin

    # Relative permeability of the rotor iron
    mu_rotor = Machine.rotor.mat_type.mag.mur_lin

    # Relative permeability of the winding
    if Machine.stator.winding.conductor.cond_mat.mag != None:
        mu_winding = Machine.stator.winding.conductor.cond_mat.mag.mur_lin
    else:
        mu_winding = 1

    # Relative permeabiltity of the PM
    mur_PM = Machine.rotor.magnet.mat_type.mag.mur_lin

    # Defining the material dict
    material_dict = defaultdict(float)

    material_dict["vacuum"] = mu0
    material_dict["air"] = mu_air
    material_dict["stator"] = mu_stator
    material_dict["rotor"] = mu_rotor

    for ii in range(nb_stator_teeth_per_period * nb_layers):
        material_dict["winding" + str(ii + 1)] = mu_winding

    for jj in range(nb_PM_per_period):
        material_dict["PM" + str(jj + 1)] = mur_PM

    #######################################################################################
    # Definition of the discretization along theta and r
    #######################################################################################

    # Defining the x and y axes of the motor geometry
    x = angle_tp
    y = Machine.stator.Rext - Machine.rotor.Rint

    # Number of elements in the x-axis direction
    N_element_theta = N_point_theta - 1

    # Definition of the discretization steps
    h_theta = x / (N_point_theta - 1)

    #######################################################################################
    # Definition of the angles of the motor elements (theta)
    #######################################################################################

    """ Rotor geometry angular dimensions in deg"""
    # Angular opening of the rotor magnet
    # angle_magnet = Machine.rotor.slot.comp_angle_active_eq() * rad_to_deg
    angle_magnet = Machine.rotor.slot.comp_angle_active_eq()

    """ Stator geometry angular dimensions in deg"""
    # Angular opening of the stator slot
    # angle_stator_slot = Machine.stator.slot.comp_angle_active_eq() * rad_to_deg
    angle_stator_slot = Machine.stator.slot.comp_angle_active_eq()

    """ Geometry discretization according to the theta-axis """
    """ Discritized stator """
    # Discretized slot angle according to the theta-direction
    stator_slot_elements_theta = round(angle_stator_slot / h_theta)

    # angle slot is multiple of number of layers
    stator_slot_elements_theta = nb_layers * round(
        stator_slot_elements_theta / nb_layers
    )

    # Angular opening of the stator tooth
    stator_tooth_opening = (
        N_element_theta - nb_stator_teeth_per_period * stator_slot_elements_theta
    ) / nb_stator_teeth_per_period

    # Discretized 1/2 stator tooth angle according to the theta-direction
    half_stator_tooth_elements_theta = round(stator_tooth_opening / 2)

    # Discretized stator tooth angle according to the theta-direction
    stator_tooth_elements_theta = round(stator_tooth_opening)

    """ Discritized rotor """
    # Discretized PM angle according to the theta-direction
    magnet_elements_theta = round(angle_magnet / h_theta)

    # Discretized 1/2 air-gap between two adjacent PMs in the theta-direction
    half_airgap_magnet_elements_theta = round(
        (N_element_theta - magnet_elements_theta * nb_PM_per_period)
        / (2 * nb_PM_per_period)
    )

    # Discretized air-gap between two adjacent PMs in the theta-direction
    airgap_magnet_elements_theta = half_airgap_magnet_elements_theta * 2

    #######################################################################################
    # Definition of the radius of the motor elements (r)
    #######################################################################################

    """ Rotor geometry dimensions"""
    # Rotor interior radius
    radius_rotor_interior = Machine.rotor.Rint

    # Height of the rotor yoke
    height_rotor_yoke = Machine.rotor.comp_height_yoke()

    # Rotor exterior radius
    radius_rotor_exterior = radius_rotor_interior + height_rotor_yoke

    # Height of the magnet
    height_magnet = Machine.rotor.slot.comp_height_active()

    # Airgap thickness
    e = Machine.comp_width_airgap_mec()

    """ Stator geometry dimensions"""
    # Stator exterior and interior radius
    radius_stator_exterior = Machine.stator.Rext
    radius_stator_interior = Machine.stator.Rint

    # Stator slots interior and exterior radius
    radius_stator_slot_exterior = (
        radius_stator_exterior - Machine.stator.comp_height_yoke()
    )
    radius_stator_slot_interior = (
        radius_stator_slot_exterior - Machine.stator.slot.comp_height_active()
    )

    # Height of the stator slot
    # height_stator_slot = radius_stator_slot_exterior - radius_stator_slot_interior

    # Stator yoke
    # height_stator_yoke = Machine.stator.comp_height_yoke()

    # Height of the air between the interior radius of the stator slot and the interior radius of the stator
    # Null in case radius_stator_slot_interior = radius_stator_interior
    # height_stator_isthmus = radius_stator_slot_interior - radius_stator_interior

    """ Geometry discretization according to the r-axis """
    """ Discritized stator """
    # Discretized stator yoke in the r-axis
    # dr_stator_yoke = round(height_stator_yoke / self.stator_yoke_elements_r)

    # Stator = stator tooth region : Conform mesh
    # dr_stator_tooth = round(height_stator_slot / self.stator_tooth_elements_r)

    # Stator air elements between the stator inner radius and the slot inner radius
    # dr_stator_isthmus = round(height_stator_isthmus / self.stator_isthmus_elements_r)

    """ Discritized rotor """
    # Discretized rotor yoke in the r-axis
    # dr_rotor_yoke = round(height_rotor_yoke / self.rotor_yoke_elements_r)

    # Number of elements in the airgap and magnet in the y-direction
    # dr_airgap = round(e / self.airgap_elements_r)
    # dr_magnet = round(height_magnet / self.magnet_elements_r)

    # airgap_and_magnet_elements_r = self.airgap_elements_r + self.magnet_elements_r

    """ Elements characteristics according to the r-axis of the geometry (in a dict):
    characteristics_elements_r = {nbr_elements_r, element_height}"""
    axes_r = {}
    axes_r["rotor_yoke"] = np.linspace(
        radius_rotor_interior,
        radius_rotor_exterior,
        (self.rotor_yoke_elements_r + 1),
    )
    # Delete the last point of the rotor yoke axis to avoid duplication
    axes_r["rotor_yoke"] = np.delete(axes_r["rotor_yoke"], -1)

    axes_r["magnet"] = np.linspace(
        radius_rotor_exterior,
        (radius_rotor_exterior + height_magnet),
        (self.magnet_elements_r + 1),
    )
    axes_r["magnet"] = np.delete(axes_r["magnet"], -1)

    axes_r["airgap"] = np.linspace(
        (radius_rotor_exterior + height_magnet),
        (radius_rotor_exterior + height_magnet + e),
        (self.airgap_elements_r + 1),
    )
    axes_r["airgap"] = np.delete(axes_r["airgap"], -1)

    axes_r["stator_tooth"] = np.linspace(
        radius_stator_slot_interior,
        radius_stator_slot_exterior,
        (self.stator_tooth_elements_r + 1),
    )
    axes_r["stator_tooth"] = np.delete(axes_r["stator_tooth"], -1)

    if radius_stator_interior != radius_stator_slot_interior:
        axes_r["stator_isthmus"] = np.linspace(
            radius_stator_interior,
            radius_stator_slot_interior,
            (self.stator_isthmus_elements_r + 1),
        )
        axes_r["stator_isthmus"] = np.delete(axes_r["stator_isthmus"], -1)
    else:
        axes_r["stator_isthmus"] = []

    axes_r["stator_yoke"] = np.linspace(
        radius_stator_slot_exterior,
        radius_stator_exterior,
        (self.stator_yoke_elements_r + 1),
    )

    # Total number of elements of the geometry
    if radius_stator_interior != radius_stator_slot_interior:
        N_element_r_total = (
            self.rotor_yoke_elements_r
            + self.magnet_elements_r
            + self.airgap_elements_r
            + self.stator_tooth_elements_r
            + self.stator_isthmus_elements_r
            + self.stator_yoke_elements_r
        )
    else:
        N_element_r_total = (
            self.rotor_yoke_elements_r
            + self.magnet_elements_r
            + self.airgap_elements_r
            + self.stator_tooth_elements_r
            + self.stator_yoke_elements_r
        )
    # Total number of elements in the geometry
    N_point_r = N_element_r_total + 1

    # Position in the middle of the airgap
    index_middle_airgap = (
        self.rotor_yoke_elements_r
        + self.magnet_elements_r
        + self.airgap_elements_r // 2
    )

    #######################################################################################
    # Update and re-calculation of N_element_theta and the dependent parameters
    # Condition 1 (theta is unchangeable for all elements)
    #######################################################################################
    if (
        nb_stator_teeth_per_period
        * (stator_slot_elements_theta + 2 * half_stator_tooth_elements_theta)
    ) == (
        nb_PM_per_period
        * (magnet_elements_theta + 2 * half_airgap_magnet_elements_theta)
    ):
        N_element_theta_kk = N_element_theta
        N_point_theta = N_element_theta_kk + 1

    for kk in range(
        1, (nb_PM_per_period * nb_stator_teeth_per_period * round(angle_tp)), 1
    ):

        N_element_theta_kk = N_element_theta * kk
        N_point_theta = N_element_theta_kk + 1
        h_theta = x / (N_point_theta - 1)
        # stator_slot_elements_theta = nb_layers * round(
        #     (Machine.stator.slot.comp_angle_active_eq() * rad_to_deg / h_theta)
        #     / nb_layers
        # )
        stator_slot_elements_theta = nb_layers * round(
            (Machine.stator.slot.comp_angle_active_eq() / h_theta) / nb_layers
        )

        stator_tooth_opening = (
            N_element_theta_kk - nb_stator_teeth_per_period * stator_slot_elements_theta
        ) / nb_stator_teeth_per_period

        half_stator_tooth_elements_theta = round(stator_tooth_opening / 2)

        stator_tooth_elements_theta = round(stator_tooth_opening)

        magnet_elements_theta = round(angle_magnet / h_theta)

        half_airgap_magnet_elements_theta = round(
            (N_element_theta_kk - magnet_elements_theta * nb_PM_per_period)
            / (2 * nb_PM_per_period)
        )

        airgap_magnet_elements_theta = half_airgap_magnet_elements_theta * 2

        if (
            nb_stator_teeth_per_period
            * (stator_slot_elements_theta + 2 * half_stator_tooth_elements_theta)
        ) == (
            nb_PM_per_period
            * (magnet_elements_theta + 2 * half_airgap_magnet_elements_theta)
        ):
            break

    #######################################################################################
    # Defining the geometry discretization
    #######################################################################################

    # Total number of elements
    N_total_element = N_element_r_total * N_element_theta_kk

    # Attribute an array of N_total_element size of zeros to cells_materials
    cells_materials = np.zeros(N_total_element, dtype=np.float64)

    # Identify the position of the magnets in the geometry
    mask_magnet = defaultdict(bool)
    for nbr in range(nb_PM_per_period):
        mask_magnet["PM" + str(nbr + 1)] = [False for i in range(N_total_element)]

    """Add the geoemtry_disctint list to be able to plot the different motor elements
     (even with them having the same permeabilities) in the view_contour_flux method"""
    geometry_disctint = np.zeros(N_total_element, dtype=np.uint16)

    # Assignment of geometry elements
    for i in range(N_element_r_total):

        # Assigning rotor elements
        if i < self.rotor_yoke_elements_r:
            for j in range(N_element_theta_kk):
                num_element = N_element_theta_kk * i + j
                cells_materials[num_element] = material_dict["rotor"]  # rotor material
                geometry_disctint[num_element] = 3

        # Assignment of PM and the airgap between PMs elements
        elif i < (self.rotor_yoke_elements_r + self.magnet_elements_r):

            for j in range(N_element_theta_kk):
                num_element = N_element_theta_kk * i + j
                # Assignment of the first half of the airgap elements
                if j < half_airgap_magnet_elements_theta:
                    cells_materials[num_element] = material_dict["air"]  # air material
                    geometry_disctint[num_element] = 2

                elif j < (N_element_theta_kk - half_airgap_magnet_elements_theta):
                    for PM_idx in range(nb_PM_per_period):
                        # Assignment of PM elements
                        if (
                            j
                            >= (
                                half_airgap_magnet_elements_theta
                                + PM_idx
                                * (magnet_elements_theta + airgap_magnet_elements_theta)
                            )
                        ) and (
                            j
                            < (
                                half_airgap_magnet_elements_theta
                                + (PM_idx + 1) * magnet_elements_theta
                                + PM_idx * airgap_magnet_elements_theta
                            )
                        ):
                            cells_materials[num_element] = material_dict[
                                "PM" + str(PM_idx + 1)
                            ]  # PM materials
                            geometry_disctint[num_element] = 4 + PM_idx
                            mask_magnet["PM" + str(PM_idx + 1)][num_element] = True

                        # Assignment of the airgaps between PMs elements
                        if (
                            j
                            >= (
                                half_airgap_magnet_elements_theta
                                + PM_idx * magnet_elements_theta
                                + (PM_idx - 1) * airgap_magnet_elements_theta
                            )
                        ) and (
                            j
                            < (
                                half_airgap_magnet_elements_theta
                                + PM_idx
                                * (magnet_elements_theta + airgap_magnet_elements_theta)
                            )
                        ):
                            cells_materials[num_element] = material_dict[
                                "air"
                            ]  # air material between the PMs
                            geometry_disctint[num_element] = 2

                # Assignment of the last half of the airgap
                else:
                    cells_materials[num_element] = material_dict["air"]  # air material
                    geometry_disctint[num_element] = 2

        # Assignment of the airgap between the PMs and the stator
        elif i < (
            self.rotor_yoke_elements_r + self.airgap_elements_r + self.magnet_elements_r
        ):
            for j in range(N_element_theta_kk):
                num_element = N_element_theta_kk * i + j
                cells_materials[num_element] = material_dict["air"]  # air
                geometry_disctint[num_element] = 2

        # Stator elements
        elif i < N_element_r_total - self.stator_yoke_elements_r:

            # Case where the stator slot is not aligned with the stator tooth
            if radius_stator_slot_interior != radius_stator_interior:
                if (
                    i
                    <= self.stator_isthmus_elements_r
                    + self.rotor_yoke_elements_r
                    + self.airgap_elements_r
                    + self.magnet_elements_r
                ):
                    for j in range(N_element_theta_kk):
                        num_element = N_element_theta_kk * i + j
                        # Assignment of the elements in the first half tooth
                        if j < half_stator_tooth_elements_theta:
                            cells_materials[num_element] = material_dict[
                                "stator"
                            ]  # stator
                            geometry_disctint[num_element] = 1

                        elif j <= (
                            N_element_theta_kk - half_stator_tooth_elements_theta
                        ):
                            for slot_idx in range(nb_stator_teeth_per_period):
                                if (
                                    j
                                    >= (
                                        half_stator_tooth_elements_theta
                                        + slot_idx
                                        * (
                                            stator_slot_elements_theta
                                            + stator_tooth_elements_theta
                                        )
                                    )
                                ) and (
                                    j
                                    < (
                                        half_stator_tooth_elements_theta
                                        + (slot_idx + 1) * stator_slot_elements_theta
                                        + slot_idx * stator_tooth_elements_theta
                                    )
                                ):
                                    cells_materials[num_element] = material_dict["air"]
                                    geometry_disctint[num_element] = 2
                                    break

                                # Assignment of tooth elements
                                else:
                                    cells_materials[num_element] = material_dict[
                                        "stator"
                                    ]  # stator
                                    geometry_disctint[num_element] = 1

                        # Assignment f the last half of the stator tooth
                        else:
                            cells_materials[num_element] = material_dict[
                                "stator"
                            ]  # stator
                            geometry_disctint[num_element] = 1

                # Assignment of the remaining stator elements
                else:
                    for j in range(N_element_theta_kk):
                        num_element = N_element_theta_kk * i + j
                        # Assignment of the elements in the first half tooth
                        if j < half_stator_tooth_elements_theta:
                            cells_materials[num_element] = material_dict[
                                "stator"
                            ]  # stator
                            geometry_disctint[num_element] = 1

                        elif j <= (
                            N_element_theta_kk - half_stator_tooth_elements_theta
                        ):
                            for slot_idx in range(nb_stator_teeth_per_period):

                                # Assignement of the winding elements
                                if (
                                    j
                                    >= (
                                        half_stator_tooth_elements_theta
                                        + slot_idx
                                        * (
                                            stator_slot_elements_theta
                                            + stator_tooth_elements_theta
                                        )
                                    )
                                ) and (
                                    j
                                    < (
                                        half_stator_tooth_elements_theta
                                        + (slot_idx + 1) * stator_slot_elements_theta
                                        + slot_idx * stator_tooth_elements_theta
                                    )
                                ):
                                    # Searching for the layer of a slot index
                                    for layer in range(nb_layers):
                                        if (
                                            j
                                            >= (
                                                half_stator_tooth_elements_theta
                                                + slot_idx
                                                * (
                                                    stator_slot_elements_theta
                                                    + stator_tooth_elements_theta
                                                )
                                                + layer
                                                * (
                                                    stator_slot_elements_theta
                                                    / nb_layers
                                                )
                                            )
                                        ) and (
                                            j
                                            < (
                                                half_stator_tooth_elements_theta
                                                + (slot_idx + 1)
                                                * stator_slot_elements_theta
                                                + slot_idx * stator_tooth_elements_theta
                                                + (layer + 1)
                                                * (
                                                    stator_slot_elements_theta
                                                    / nb_layers
                                                )
                                            )
                                        ):

                                            cells_materials[
                                                num_element
                                            ] = material_dict[
                                                "winding"
                                                + str(slot_idx * nb_layers + layer + 1)
                                            ]
                                            geometry_disctint[num_element] = (
                                                (4 + nb_PM_per_period)
                                                + layer
                                                + slot_idx * nb_layers
                                            )
                                    break

                                # Assignment of tooth elements
                                else:
                                    cells_materials[num_element] = material_dict[
                                        "stator"
                                    ]  # stator
                                    geometry_disctint[num_element] = 1

                        # Assignment of the last half tooth element
                        else:
                            cells_materials[num_element] = material_dict[
                                "stator"
                            ]  # stator
                            geometry_disctint[num_element] = 1
            else:
                for j in range(N_element_theta_kk):
                    num_element = N_element_theta_kk * i + j
                    # Assignment of the elements in the first half tooth
                    if j < half_stator_tooth_elements_theta:
                        cells_materials[num_element] = material_dict["stator"]  # stator
                        geometry_disctint[num_element] = 1

                    elif j <= (N_element_theta_kk - half_stator_tooth_elements_theta):
                        for slot_idx in range(nb_stator_teeth_per_period):

                            # Assignement of the winding elements
                            if (
                                j
                                >= (
                                    half_stator_tooth_elements_theta
                                    + slot_idx
                                    * (
                                        stator_slot_elements_theta
                                        + stator_tooth_elements_theta
                                    )
                                )
                            ) and (
                                j
                                < (
                                    half_stator_tooth_elements_theta
                                    + (slot_idx + 1) * stator_slot_elements_theta
                                    + slot_idx * stator_tooth_elements_theta
                                )
                            ):
                                # Searching for the layer of a slot index
                                for layer in range(nb_layers):
                                    if (
                                        j
                                        >= (
                                            half_stator_tooth_elements_theta
                                            + slot_idx
                                            * (
                                                stator_slot_elements_theta
                                                + stator_tooth_elements_theta
                                            )
                                            + layer
                                            * (stator_slot_elements_theta / nb_layers)
                                        )
                                    ) and (
                                        j
                                        < (
                                            half_stator_tooth_elements_theta
                                            + (slot_idx + 1)
                                            * stator_slot_elements_theta
                                            + slot_idx * stator_tooth_elements_theta
                                            + (layer + 1)
                                            * (stator_slot_elements_theta / nb_layers)
                                        )
                                    ):

                                        cells_materials[num_element] = material_dict[
                                            "winding"
                                            + str(slot_idx * nb_layers + layer + 1)
                                        ]
                                        geometry_disctint[num_element] = (
                                            (4 + nb_PM_per_period)
                                            + layer
                                            + slot_idx * nb_layers
                                        )
                                break

                            # Assignment of tooth elements
                            else:
                                cells_materials[num_element] = material_dict[
                                    "stator"
                                ]  # stator
                                geometry_disctint[num_element] = 1

                    # Assignment of the last half tooth element
                    else:
                        cells_materials[num_element] = material_dict["stator"]  # stator
                        geometry_disctint[num_element] = 1

        # Assignment of the stator yoke material
        else:
            for j in range(N_element_theta_kk):
                num_element = N_element_theta_kk * i + j
                cells_materials[num_element] = material_dict["stator"]  # stator
                geometry_disctint[num_element] = 1

    #######################################################################################
    # Plotting the geometry mesh for validation purposes
    #######################################################################################
    # ct = plt.pcolormesh(
    #     geometry_disctint.reshape((N_point_r - 1, N_point_theta - 1)),
    #     cmap="jet",
    #     alpha=0.6,
    # )
    # plt.xlabel("N_element_theta")
    # plt.ylabel("N_element_r")
    # plt.show()

    return (
        cells_materials,
        material_dict,
        N_point_theta,
        geometry_disctint,
        mask_magnet,
        N_point_r,
        axes_r,
        index_middle_airgap,
        magnet_elements_theta,
    )
