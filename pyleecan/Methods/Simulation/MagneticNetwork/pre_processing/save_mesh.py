# -*- coding: utf-8 -*-

import numpy as np


def save_mesh(self, permeabiltiy_materials, Num_Unknowns, list_elem, x, y, BC_list):
    """
    SAve mesh

    Parameters
    ----------
    permeability_materials : nd-array, size: (foat)
        permabilty of each materials.
    Num_Unknowns : nd-array, size: n (int)
        Numerotation in the linear system.
    list_elem : nd-array, size: m (integers)
        tab of elements
    x : nd-array, size: size_x (float)
        x coordinate.
    y : nd-array, size: size_x (float)
        y coordinate.
    BC_list : nd-array, size: n (integers)
        data-strurture for BC evaluation.

    Returns
    -------
    None.

    """
    f_handle = open("mesh.txt", "w")
    np.savetxt(
        f_handle,
        np.column_stack((list_elem, permeabiltiy_materials)),
        fmt="%u",
        header=str(permeabiltiy_materials.size) + " " + str(Num_Unknowns.size),
    )
    list_coord = np.zeros((Num_Unknowns.size, 2))
    for i in range(x.size):
        for j in range(y.size):
            list_coord[x.size * j + i, :] = np.array([x[i], y[j]])
    f_handle.close()
    f_handle = open("mesh.txt", "a")
    np.savetxt(
        f_handle,
        np.column_stack((list_coord, Num_Unknowns, BC_list)),
        fmt="%f %f %d %d",
    )
    f_handle.close()
    print("mesh is saved")
