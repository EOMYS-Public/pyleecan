# -*- coding: utf-8 -*-
import time
import numpy as np
from scipy.sparse import coo_matrix


def assembly(
    self,
    reluc_list,
    Num_Unknowns,
    list_elem,
    permeability_element,
    boundary_condition_list,
):
    """Matrix assembler for the motor different elements (rotor + stator + airgap)

    Parameters
    ----------
    self : MagNetwork
        A MagNetwork object
    reluc_list : nd-array (size: m * 4 of floats)
        Values of each reluctance per cell
    Num_Unknowns : nd-array (size: n of integers)
        Unknowns in the linear system
    list_elem : nd-array (size: m of integers)
        Mesh cells in the motor geometry
    permeability_element : nd-array (size: m of floats)
        Permeability values of each cell
    boundary_condition_list : nd-array (size: n of integers)
        Data-strurture for boundary conditions evaluation

    Returns
    -------
    graph : Scipy CSR matrix
        sparse representation of the matrix

    """

    N_unknowns = Num_Unknowns.max() + 1

    # permeabilit_element is the relative permeability mu_r
    reluc_upper = reluc_list[:, 0] / permeability_element
    reluc_right = reluc_list[:, 1] / permeability_element
    reluc_down = reluc_list[:, 2] / permeability_element
    reluc_left = reluc_list[:, 3] / permeability_element

    # Select indices of each vertices of this elements (square)
    index_unknown_1 = Num_Unknowns[list_elem[:, 0]]
    mask_index_unknown_1 = index_unknown_1 != -1
    index_unknown_2 = Num_Unknowns[list_elem[:, 1]]
    mask_index_unknown_2 = index_unknown_2 != -1
    index_unknown_3 = Num_Unknowns[list_elem[:, 2]]
    mask_index_unknown_3 = index_unknown_3 != -1
    index_unknown_4 = Num_Unknowns[list_elem[:, 3]]
    mask_index_unknown_4 = index_unknown_4 != -1

    t1 = time.perf_counter()

    # Add tirangular part
    if np.all(boundary_condition_list != 3):

        mask = mask_index_unknown_1 * mask_index_unknown_2
        I = index_unknown_1[mask]
        J = index_unknown_2[mask]
        data = -reluc_down[mask]
        graph = coo_matrix((data, (I, J)), shape=(N_unknowns, N_unknowns))

        mask = mask_index_unknown_2 * mask_index_unknown_3
        I = index_unknown_2[mask]
        J = index_unknown_3[mask]
        data = -reluc_right[mask]
        graph += coo_matrix((data, (I, J)), shape=(N_unknowns, N_unknowns))

        mask = mask_index_unknown_3 * mask_index_unknown_4
        I = index_unknown_3[mask]
        J = index_unknown_4[mask]
        data = -reluc_upper[mask]
        graph += coo_matrix((data, (I, J)), shape=(N_unknowns, N_unknowns))

        mask = mask_index_unknown_4 * mask_index_unknown_1
        I = index_unknown_4[mask]
        J = index_unknown_1[mask]
        data = -reluc_left[mask]
        graph += coo_matrix((data, (I, J)), shape=(N_unknowns, N_unknowns))
    else:
        mask_BC1 = boundary_condition_list[list_elem[:, 0]] == 3
        mask_BC2 = boundary_condition_list[list_elem[:, 1]] == 3
        mask_BC3 = boundary_condition_list[list_elem[:, 2]] == 3
        mask_BC4 = boundary_condition_list[list_elem[:, 3]] == 3

        plus_minus = np.array([-1, 1])

        mask = mask_index_unknown_1 * mask_index_unknown_2
        I = index_unknown_1[mask]
        J = index_unknown_2[mask]
        data = (
            reluc_down[mask]
            * plus_minus[(np.logical_xor(mask_BC1, mask_BC2)).astype(np.int32)][mask]
        )
        graph = coo_matrix((data, (I, J)), shape=(N_unknowns, N_unknowns))

        mask = mask_index_unknown_2 * mask_index_unknown_3
        I = index_unknown_2[mask]
        J = index_unknown_3[mask]
        data = (
            reluc_right[mask]
            * plus_minus[(np.logical_xor(mask_BC2, mask_BC3)).astype(np.int32)][mask]
        )
        graph += coo_matrix((data, (I, J)), shape=(N_unknowns, N_unknowns))

        mask = mask_index_unknown_3 * mask_index_unknown_4
        I = index_unknown_3[mask]
        J = index_unknown_4[mask]
        data = (
            reluc_upper[mask]
            * plus_minus[(np.logical_xor(mask_BC3, mask_BC4)).astype(np.int32)][mask]
        )
        graph += coo_matrix((data, (I, J)), shape=(N_unknowns, N_unknowns))

        mask = mask_index_unknown_4 * mask_index_unknown_1
        I = index_unknown_4[mask]
        J = index_unknown_1[mask]
        data = (
            reluc_left[mask]
            * plus_minus[(np.logical_xor(mask_BC4, mask_BC1)).astype(np.int32)][mask]
        )
        graph += coo_matrix((data, (I, J)), shape=(N_unknowns, N_unknowns))

    t2 = time.perf_counter()
    print("time assembly matrix without diag", t2 - t1)
    # add the symetric part
    graph += graph.T

    # Add diagonal
    Diag = np.zeros(N_unknowns, dtype=np.float64)

    Diag[index_unknown_1[mask_index_unknown_1]] += (
        reluc_down[mask_index_unknown_1] + reluc_left[mask_index_unknown_1]
    )
    Diag[index_unknown_2[mask_index_unknown_2]] += (
        reluc_right[mask_index_unknown_2] + reluc_down[mask_index_unknown_2]
    )
    Diag[index_unknown_3[mask_index_unknown_3]] += (
        reluc_upper[mask_index_unknown_3] + reluc_right[mask_index_unknown_3]
    )
    Diag[index_unknown_4[mask_index_unknown_4]] += (
        reluc_upper[mask_index_unknown_4] + reluc_left[mask_index_unknown_4]
    )

    I = np.arange(N_unknowns)
    graph += coo_matrix((Diag, (I, I)), shape=(N_unknowns, N_unknowns))
    # graph.setdiag(Diag)
    t3 = time.perf_counter()
    print("time assembly diag", t3 - t2)

    return graph
