# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 09:51:29 2022

@author: LAP02
"""

# from tkinter.ttk import _TreeviewColumnDict
from tkinter import *
from turtle import st
import numpy as np
from pyleecan.Functions.load import load
from scipy.fft import ifftn
import matplotlib.pyplot as plt


def geometry_linear_motor(self, size_x, size_y, pos_pm):

    # Get machine object
    Machine = self.parent.machine

    rad_to_deg = 180 / np.pi

    if Machine.comp_periodicity_spatial()[1] == True:
        periodicity = Machine.comp_periodicity_spatial()[0]
    else:
        periodicity = Machine.comp_periodicity_spatial()[0] / 2

    # Definition of the machine geometrical input parameters
    tp = (
        np.pi * Machine.stator.Rint / Machine.rotor.get_pole_pair_number()
    )  # Ref:https://www.slideshare.net/monprado1/11-basic-concepts-of-a-machine-77442134

    angle_tp = (np.pi / periodicity) * rad_to_deg

    # Number of PMs per period
    nb_PM_per_period = round(Machine.rotor.get_pole_pair_number() / periodicity)

    # Number of stator teeth per period
    nb_stator_teeth_per_period = round(Machine.stator.get_Zs() / (2 * periodicity))

    # Outer radius of the rotor + PM
    height_rotor_PM = Machine.rotor.comp_radius_mec()

    # Height of the magnet
    hm = Machine.rotor.slot.comp_height_active()

    # Compute the angular opening of the rotor magnet
    angle_magnet = Machine.rotor.slot.comp_angle_active_eq() * rad_to_deg

    # Air-gap thickness (m)
    e = Machine.comp_width_airgap_mec()

    # Stator slot height (m)
    hs = Machine.stator.slot.comp_height()

    # Stator total height (m)
    hst = Machine.stator.Rext - Machine.stator.Rint

    # Moving armature height (moving back iron height)
    hmbi = Machine.rotor.comp_height_yoke()

    # Slot opening (m)
    ws = Machine.stator.slot.comp_width()

    # Stator yoke
    sy = Machine.stator.comp_height_yoke()

    # Stator tooth width (m)
    wt = (
        Machine.stator.get_Rbo()
        * 2
        * np.sin(
            2 * np.pi / Machine.stator.get_Zs()
            - float(np.arcsin(ws / (2 * Machine.stator.get_Rbo())))
        )
    )

    # Slot pitch (m)
    ts = ws + wt

    # Number of winding layers
    nb_layers = Machine.stator.winding.Nlayer

    # Active length (m)
    la = Machine.rotor.L1

    # Material properties
    # PM remanance (T)
    Br = Machine.rotor.magnet.mat_type.mag.Brm20

    # Permeability of vacuum (H/m)
    mu0 = np.pi * 4e-7

    # Relative permeability of air
    mur1 = 1

    # Relative permeability of the stator iron
    mur2 = Machine.stator.mat_type.mag.mur_lin

    # Relative permeability of the rotor iron
    mur3 = Machine.rotor.mat_type.mag.mur_lin

    # Relative permeability of the winding
    if Machine.stator.winding.conductor.cond_mat.mag != None:
        mur_bob = Machine.stator.winding.conductor.cond_mat.mag.mur_lin
    else:
        mur_bob = 1

    # Relative permeabiltity of the PM
    mur_PM = Machine.rotor.magnet.mat_type.mag.mur_lin

    # Generalize the materials list and their linear permeabilities for a specific number of windings
    list_materials = []
    permeabilty_materials = np.array([])

    for i in range(nb_stator_teeth_per_period * nb_layers):
        # list_materials = ["bob1", "bob2", "bob3", "air", "iron1", "PM", "iron3"]
        list_materials.append("bob" + str(i + 1))
        permeabilty_materials = np.append(permeabilty_materials, [mur_bob])

    list_materials += ["air", "iron1", "PM", "iron3"]

    permeabilty_materials = np.append(permeabilty_materials, [mur1, mur2, mur_PM, mur3])

    # x and y positions
    x = angle_tp
    y = Machine.stator.Rext - Machine.rotor.Rint

    # Number of elements in the y-axis direction
    total_height = size_y - 1

    # Number of elements in the x-axis direction
    total_width = size_x - 1

    # Definition of x-axis and y-axis steps
    h_theta = (np.pi / periodicity) * rad_to_deg / (size_x - 1)
    h_y = y / (size_y - 1)

    # Number of elements in the stator armature
    # Compute the angular opening of the stator slot
    angle_slot = round(
        Machine.stator.slot.comp_angle_active_eq() * rad_to_deg / h_theta
    )
    angle_slot = nb_layers * round(
        angle_slot / nb_layers
    )  # angle slot is multiple of number of layers

    # Number of elements in the stator tooth
    angle_tooth = (
        total_width - nb_stator_teeth_per_period * angle_slot
    ) / nb_stator_teeth_per_period

    # Number of elements in half a tooth
    Half_tooth_width = round(angle_tooth / 2)

    # Number of elements in a total tooth
    tooth_width = round(angle_tooth)

    # Number of elements in the stator back-iron in y-axis direction, generalized
    stator_iron_height = round(sy / h_y)

    # Total number of elements of the stator in x direction
    # m = round(
    #     (Machine.stator.get_Zs() / (2 * Machine.rotor.comp_periodicity_spatial()[0]))
    #     * (tooth_width + Half_tooth_width1)
    # )

    # Total number of element of stator in y direction
    stator_height = round((Machine.stator.Rext - Machine.stator.Rint) / h_y)

    # Number of elements in the magnet in the theta direction
    PM_width = round(angle_magnet / h_theta)

    # Number of elements in half the air-gap between two adjacent PMs in the theta direction
    half_airgap_PM_width = round(
        (total_width - PM_width * nb_PM_per_period) / (2 * nb_PM_per_period)
    )

    # Number of elements in the airgap between 2 adjacent PMs in the theta direction
    airgap_PM_width = half_airgap_PM_width * 2

    # Number of elements in the air-gap in y direction
    airgap_height = round(e / h_y)

    # Number of elements in the moving armature iron in y direction
    rotor_height = round(hmbi / h_y)

    # Number of elements in the magnetic air-gap (hm + e) in y direction
    airgap_and_Pm_height = round((hm + e) / h_y)
    # airgap_and_Pm_height = round(Machine.rotor.comp_radius_mec() / h_y)

    # Total number of elements
    nn = total_height * total_width

    # Attribute an array of nn size of zeros to cells_materials
    cells_materials = np.zeros(nn, dtype=np.uint16)

    # Mask magnets
    mask_magnet = np.zeros(nn, dtype=np.bool_)
    mask_magnet[
        total_width * airgap_and_Pm_height
        - total_width : total_width
        * (airgap_and_Pm_height + rotor_height - airgap_height)
        + total_width
    ] = True

    # Assignment of geometry elements
    for i in range(total_height):

        # Assigning rotor elements
        if i <= rotor_height:
            for j in range(total_width):
                num_elem = total_width * i + j
                cells_materials[num_elem] = len(permeabilty_materials)  # rotor material

        # Assignment of PM and the airgap between PMs elements
        elif i <= (rotor_height + airgap_and_Pm_height - airgap_height):

            for j in range(total_width):
                num_elem = total_width * i + j

                # Assignment of the first half of the airgap elements
                if j <= half_airgap_PM_width:
                    cells_materials[num_elem] = (
                        len(permeabilty_materials) - 3
                    )  # air material

                elif j <= (total_width - half_airgap_PM_width):
                    for PM_idx in range(nb_PM_per_period):
                        # Assignment of PM elements
                        if (
                            j
                            >= (
                                half_airgap_PM_width
                                + PM_idx * (PM_width + airgap_PM_width)
                            )
                        ) and (
                            j
                            <= (
                                half_airgap_PM_width
                                + (PM_idx + 1) * PM_width
                                + PM_idx * airgap_PM_width
                            )
                        ):
                            cells_materials[num_elem] = (
                                len(permeabilty_materials) - 1
                            )  # PM material
                        # Assignment of the airgaps between PMs elements

                        if (
                            j
                            >= (
                                half_airgap_PM_width
                                + PM_idx * PM_width
                                + (PM_idx - 1) * airgap_PM_width
                            )
                        ) and (
                            j
                            <= (
                                half_airgap_PM_width
                                + PM_idx * (PM_width + airgap_PM_width)
                            )
                        ):
                            cells_materials[num_elem] = (
                                len(permeabilty_materials) - 3
                            )  # air material between the PMs

                # Assignment of the last half of the airgap
                else:
                    cells_materials[num_elem] = (
                        len(permeabilty_materials) - 3
                    )  # air material

        # Assignment of the airgap between the PMs and the stator
        elif i <= (rotor_height + airgap_and_Pm_height):
            for j in range(total_width):
                num_elem = total_width * i + j
                cells_materials[num_elem] = len(permeabilty_materials) - 3  # air

        elif i <= total_height - stator_iron_height:
            for j in range(total_width):
                num_elem = total_width * i + j

                # Assignment of the elements in the first half tooth
                if j <= Half_tooth_width:
                    cells_materials[num_elem] = len(permeabilty_materials) - 2  # stator

                elif j <= (total_width - Half_tooth_width):
                    for slot_idx in range(nb_stator_teeth_per_period):

                        # Assignement of the winding elements
                        if (
                            j
                            >= (
                                Half_tooth_width + slot_idx * (angle_slot + tooth_width)
                            )
                        ) and (
                            j
                            <= (
                                Half_tooth_width
                                + (slot_idx + 1) * angle_slot
                                + slot_idx * tooth_width
                            )
                        ):
                            # Searching for the layer of a slot index
                            for layer in range(nb_layers):
                                if (
                                    j
                                    >= (
                                        Half_tooth_width
                                        + slot_idx * (angle_slot + tooth_width)
                                        + layer * (angle_slot / nb_layers)
                                    )
                                ) and (
                                    j
                                    <= (
                                        Half_tooth_width
                                        + (slot_idx + 1) * angle_slot
                                        + slot_idx * tooth_width
                                        + (layer + 1) * (angle_slot / nb_layers)
                                    )
                                ):

                                    cells_materials[num_elem] = (
                                        1 + layer + slot_idx * nb_layers
                                    )  # winding layers
                            break

                        # Assignment of tooth elements
                        else:
                            cells_materials[num_elem] = (
                                len(permeabilty_materials) - 2
                            )  # stator

                # Assignment of the last half tooth element
                else:
                    cells_materials[num_elem] = len(permeabilty_materials) - 2  # stator

        # Assignment of the back-iron layer
        else:
            for j in range(total_width):
                num_elem = total_width * i + j
                cells_materials[num_elem] = len(permeabilty_materials) - 2  # stator

    ct = plt.pcolormesh(
        cells_materials.reshape((size_y - 1, size_x - 1)),
        # cmap="gnuplot",
        cmap="jet",
        # cmap="nipy_spectral",
        # cmap="rainbow",
        # edgecolors=None,
        # facecolors="none",
        alpha=0.6,
    )

    plt.show()

    return cells_materials, permeabilty_materials