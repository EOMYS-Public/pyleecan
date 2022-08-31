# -*- coding: utf-8 -*-
import time
from threadpoolctl import threadpool_info
import os
import numpy as np
import matplotlib.pyplot as plt

threads = "1"
os.environ["OMP_NUM_THREADS"] = threads  # export OMP_NUM_THREADS=4
os.environ["OPENBLAS_NUM_THREADS"] = threads  # export OPENBLAS_NUM_THREADS=4
os.environ["MKL_NUM_THREADS"] = threads  # export MKL_NUM_THREADS=6
# export VECLIB_MAXIMUM_THREADS=4
os.environ["VECLIB_MAXIMUM_THREADS"] = threads
os.environ["NUMEXPR_NUM_THREADS"] = threads  # export NUMEXPR_NUM_THREADS=6
# export MKL_DOMAIN_NUM_THREADS="MKL_BLAS=2"
os.environ["MKL_DOMAIN_NUM_THREADS"] = "MKL_DOMAIN_ALL=1"

os.environ["MKL_DYNAMIC"] = "FALSE"
os.environ["OMP_DYNAMIC"] = "FALSE"

# Choose beetween chol-mod and scipy sparse linear solver
Have_cholmod = False
try:
    from sksparse.cholmod import cholesky

    Have_cholmod = True
except:
    from scipy.sparse.linalg import spsolve


def solver_linear_model(
    self,
    N_point_theta,
    N_point_r,
    theta,
    r,
    x_dual,
    y_dual,
    boundary_condition,
    geometry,
    material_dict,
    la,
    Br,
    type_coord_sys,
    JA=None,
    JB=None,
    JC=None,
):
    """Compute the MagNetwork of a defined electric motor

    Parameters
    ----------
    self: MagNetwork
        A MagNetwork object
    N_point_theta : integer
        Discretization point in the theta direction
    N_point_r : integer
        Discretization points in the r direction
    r: array
        Values of r coordinates
    theta: array
        Values of theta coordinates
    rotor_shift : integer (Default = 8)
        Number of rotor mesh cells to be shifted with respect to the stator
    boundary_condition : list of strings
        Boundary conditions of the simulation
    geometry : method
        Initialize the geometry
    material_dict : dict
        The material dict containing the permeabilities of the motor elements
    la : integer
        Active length of the motor
    Br : float
        Remeanance flux density of the permanent magnet
    type_coord_sys : integer (Default = 2)
        Type of the coordinate system : 1 for cartesian, 2 for Radial
    JA, JB, JC : ndarray
        Currents of the phase A, B and C respectively of the stator
    Returns
    -------
    Phi : ndarrya (size : N_point_theta of floats)
        Flux Phi in each point of the mesh.
    Num_Unknowns : nd-array (size : N_point_theta of integers)
        List of unknowns in the linear system
    list_elem : nd-array, size: m (integers)
        Mesh cells of the motor geometry
    list_geomerty: nd-array (size : m of integers)
        Material of each geometry cell
    list_elem_permability : nd-array (size : m of floats)
        Permeability of each geometry cell
    list_coord : nd-array (size : N_point_theta * N_point_r theta * 2 of floats)
        Coordinates of the geometry
    """

    ###############################################################################
    # Initialization of the grid and the MagNetwork simulation parameters
    ###############################################################################

    # Starting the couting time
    t0 = time.perf_counter()

    (
        list_coord,
        list_elem,
        list_elem_permability,
        list_boundary_condition,
        Num_Unknowns,
    ) = self.init_mesh(
        N_point_theta,
        N_point_r,
        theta,
        r,
        boundary_condition,
    )

    # Ending the couting time
    t1 = time.perf_counter()

    # Measuring the performance time
    print("Initialization of the problem:", np.round(t1 - t0, 5), "seconds")

    ###############################################################################
    # Saving the mesh
    ###############################################################################

    list_elem_materials = self.geometry_motor(N_point_theta)[3]

    self.save_mesh(
        list_elem_materials, Num_Unknowns, list_elem, theta, r, list_boundary_condition
    )

    t2 = time.perf_counter()

    # Saving the mesh time
    print("Save mesh:", np.round(t2 - t1, 5), "secondes")

    ###############################################################################
    # Assemblying all the matrices
    ###############################################################################

    mu0 = material_dict["vacuum"]
    reluc_list = self.init_reluc(list_elem, list_coord, mu0, la, type_coord_sys)

    M_csr = self.assembly(
        reluc_list,
        Num_Unknowns,
        list_elem,
        list_elem_permability,
        list_boundary_condition,
    )

    t3 = time.perf_counter()
    print("Assembly matrix", np.round(t3 - t2, 5), "secondes")

    ###############################################################################
    # Assemblying the RHS containing the sources
    ###############################################################################

    mask_magnet = self.geometry_motor(N_point_theta)[4]
    magnet_elements_theta = self.geometry_motor(N_point_theta)[8]

    RHS = self.right_member_assembly(
        list_elem_permability,
        Num_Unknowns,
        list_elem,
        list_coord,
        reluc_list,
        Br,
        material_dict,
        mask_magnet,
        la,
        type_coord_sys,
        magnet_elements_theta,
        JA=JA,
        JB=JB,
        JC=JC,
    )

    t4 = time.perf_counter()

    print("Assembly vector:", np.round(t4 - t3, 5), "secondes")
    print("Total :", np.round(t4 - t2, 5))

    ###############################################################################
    # Computing the solution Phi
    ###############################################################################

    t3 = time.perf_counter()
    if Have_cholmod:

        # Compute the solution
        factor = cholesky(M_csr.tocsc())
        Phi = factor(RHS)
        t4 = time.perf_counter()
        print(
            "Time to solve (CholMod):",
            np.round(t4 - t3, 5),
            "secondes, res:",
            np.linalg.norm(M_csr @ Phi - RHS, ord=2),
        )
    else:
        Phi = spsolve(M_csr, RHS, permc_spec="MMD_AT_PLUS_A", use_umfpack=True)
        t4 = time.perf_counter()
        print(
            "Time to solve (direct,UMF):",
            np.round(t4 - t3, 5),
            "secondes, res:",
            np.linalg.norm(M_csr @ Phi - RHS, ord=2),
        )

    # Adding the oundary conditions to the solution Phi
    Phi = self.add_BC_to_Phi(
        Phi,
        Num_Unknowns,
        list_elem,
        list_boundary_condition,
    )

    return (
        Phi,
        Num_Unknowns,
        list_elem,
        list_elem_permability,
        list_coord,
    )
