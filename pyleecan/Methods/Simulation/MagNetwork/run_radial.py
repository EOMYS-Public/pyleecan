# -*- coding: utf-8 -*-

from re import S
import numpy as np
import meshio
import matplotlib.pyplot as plt
from pyleecan.Functions.load import load
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.CellMat import CellMat
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.SolutionMat import SolutionMat
from numpy import concatenate


def run_radial(self, axes_dict, Is_val=None, type_coord_sys=2):
    """
    Solve the MagNetwork in the case of radial coordinate system type

    Parameters
    ----------
    self : MagNetwork
        A MagNetwork object
    axes_dict : dict
        Dict containing axes for MagNetwork calculation
    Is_val: ndarray
        Stator current matrix accounting for magnetic periodicities
    type_coord_sys : integer (Default = 2)
        Type of the coordinate system : 1 for Cartesian and 2 for Radial

    Returns
    -------
    Bx : nd-array
        Flux density in the radial direction
    By: nd-array
        Flux density in the theta direction
    Bx_airgap :
        Flux density of the airgap in the radial direction
    By_airgap :
        Flux density of the airgap in the theta direction
    """
    ###############################################################################
    # Geometry inputs
    ###############################################################################
    Machine = self.parent.machine

    # Active length of the electric motor (m)
    la = Machine.rotor.L1

    # Definition of N_point_theta initial value
    if Machine.comp_periodicity_spatial()[1] == True:
        periodicity = Machine.comp_periodicity_spatial()[0]
    else:
        periodicity = Machine.comp_periodicity_spatial()[0] / 2

    angle_tp = (np.pi / periodicity) * (180 / np.pi)
    angle_elem = 2  # freeze element angular width in degrees to be reached
    N_point_theta = self.Kmesh_fineness * round(angle_tp / angle_elem) + 1

    # Definition of the discretization according to the r-axis
    N_point_r = self.geometry_motor(N_point_theta)[5]

    # Update of N_point_theta verifying condition 1
    N_point_theta = self.geometry_motor(N_point_theta)[2]

    # Material properties of PM and vaccum
    Br = Machine.rotor.magnet.mat_type.mag.Brm20

    # Material_dict from geometry_motor method
    material_dict = self.geometry_motor(N_point_theta)[1]

    ###############################################################################
    # Definition of the r- and theta- axes
    ###############################################################################
    # Definition of the r-axis
    axes_r = self.geometry_motor(N_point_theta)[6]
    if not len(axes_r["stator_isthmus"]):  # stator_isthmus = []
        r = np.concatenate(
            (
                axes_r["rotor_yoke"],
                axes_r["magnet"],
                axes_r["airgap"],
                axes_r["stator_tooth"],
                axes_r["stator_yoke"],
            )
        )
    else:
        r = np.concatenate(
            (
                axes_r["rotor_yoke"],
                axes_r["magnet"],
                axes_r["airgap"],
                axes_r["stator_isthmus"],
                axes_r["stator_tooth"],
                axes_r["stator_yoke"],
            )
        )

    # Definition of the theta-axis
    theta = axes_dict["theta_primal"].get_values(is_smallestperiod=True)

    # Definition of the theta_dual and r_dual axes
    theta_dual = axes_dict["angle"].get_values(is_smallestperiod=True)
    # theta_dual = (theta[1:] + theta[:-1]) / 2
    r_dual = (r[1:] + r[:-1]) / 2

    ###############################################################################
    # Definition of the boundary conditions
    ###############################################################################
    BC = [
        "anti_periodic_condition",
        "homogeneous_Dirichlet_condition",
        "anti_periodic_condition",
        "homogeneous_Dirichlet_condition",
    ]

    # BC = [
    #     "periodic_condition",
    #     "homogeneous_Dirichlet_condition",
    #     "periodic_condition",
    #     "homogeneous_Dirichlet_condition",
    # ]

    ###############################################################################
    # Compute current densities: TODO
    ###############################################################################
    if Is_val is not None:
        surface_active = self.parent.machine.stator.slot.comp_surface_active()
        JA = Is_val[0, :] / surface_active
        JB = Is_val[1, :] / surface_active
        JC = Is_val[2, :] / surface_active
    else:
        JA = None
        JB = None
        JC = None

    ###############################################################################
    # solving the MagNetwork simulation using the solver_linear_model method
    ###############################################################################
    (
        Phi,
        Num_unknowns,
        list_elem,
        permeability_cell,
        list_coord,
    ) = self.solver_linear_model(
        N_point_theta,
        N_point_r,
        theta,
        r,
        theta_dual,
        r_dual,
        BC,
        self.geometry_motor,
        material_dict,
        la,
        Br,
        type_coord_sys,
        JA=JA,
        JB=JB,
        JC=JC,
    )

    ###############################################################################
    #  Plotting the flux density contour of the electric motor
    ###############################################################################

    # Transfomration of radial coordinates to cartesian to plot the flux density contour
    x = (list_coord[:, 1] * np.cos(list_coord[:, 0])).reshape(N_point_r, N_point_theta)
    y = (list_coord[:, 1] * np.sin(list_coord[:, 0])).reshape(N_point_r, N_point_theta)

    list_cartesian_coord = np.zeros(list_coord.shape)
    list_cartesian_coord[:, 0] = x.flatten()
    list_cartesian_coord[:, 1] = y.flatten()

    ###############################################################################
    # Plotting the flux density contour
    ###############################################################################

    # Getting the geometry elements from the geometry_motor method
    list_geometry = self.geometry_motor(N_point_theta)[3]
    self.view_contour_flux(Phi, x, y, N_point_theta, N_point_r, list_geometry)

    ###############################################################################
    # computing the flux density B
    ###############################################################################
    Bx, By = self.compute_B(Phi, list_elem, list_coord, la, type_coord_sys)
    index_airgap = self.geometry_motor(N_point_theta)[7]
    self.Plot_B(
        Bx,
        By,
        theta,
        r,
        theta_dual,
        r_dual,
        list_geometry,
        type_coord_sys,
        list_coord,
        index_airgap,
    )

    B = np.stack((Bx, By), axis=-1)

    temp = np.zeros((list_elem.shape[0], 3))
    temp[:, 0] = Bx.flatten()
    temp[:, 1] = By.flatten()
    B = temp

    temp = np.zeros((list_coord.shape[0], 3))
    temp[:, 0:2] = list_coord

    print("mesh saved", list_coord.shape, list_elem.shape)

    # Compute 2D curve of the airgap flux density
    Bx_airgap, By_airgap = self.comp_flux_airgap_local(
        # r,
        # theta,
        r_dual,
        theta_dual,
        Phi,
        list_elem,
        list_coord,
        la,
        # Machine.comp_Rgap_mec(),
        index_airgap,
        type_coord_sys,
    )

    return Bx, By, Bx_airgap, By_airgap
