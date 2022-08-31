# -*- coding: utf-8 -*-

import numpy as np


def init_reluc(self, list_elem, list_coord, mu0, la, type_coord_sys):
    """
    Parameters
    ----------
    list_elem : nd-array of integers ( m * 4 )
        list of the element
    list_coord : nd-array of coordinate ( n * 2 )
        coordinate of each vertices

    Returns
    -------
    Reluc_list : Reluc_list (m * 4 )
        Reluctance of each elements
    """
    print(type_coord_sys)
    Reluc_list = np.zeros((list_elem.shape[0], 4))

    # Reluctances in the case of the cartesian coordiante system
    if type_coord_sys == 1:
        # length and width
        h_x = np.linalg.norm(
            list_coord[list_elem[:, 0]] - list_coord[list_elem[:, 1]],
            axis=1,
            ord=2,
        )
        h_y = np.linalg.norm(
            list_coord[list_elem[:, 1]] - list_coord[list_elem[:, 2]],
            axis=1,
            ord=2,
        )

        Reluc_list[:, 0] = 0.5 / (mu0 * la) * h_y / h_x
        Reluc_list[:, 1] = 0.5 / (mu0 * la) * h_x / h_y
        Reluc_list[:, 2] = 0.5 / (mu0 * la) * h_y / h_x
        Reluc_list[:, 3] = 0.5 / (mu0 * la) * h_x / h_y

    # Reluctances in the case of the polar coordiante system
    # Ref : http://lib.tkk.fi/Diss/2002/isbn9512260905/isbn9512260905.pdf (p24)
    elif type_coord_sys == 2:

        # Ref : https://www.researchgate.net/publication/321237892_Reluctance_network_-_Lumped_mechanical_thermal_models_for_the_modeling_of_concentrated_flux_synchronous_machine
        theta = np.abs(list_coord[list_elem[:, 0], 0] - list_coord[list_elem[:, 1], 0])
        R1 = list_coord[list_elem[:, 0], 1]
        R2 = R1 + (list_coord[list_elem[:, 2], 1] - list_coord[list_elem[:, 0], 1]) / 2
        R3 = list_coord[list_elem[:, 3], 1]

        Reluc_list[:, 0] = np.log(R2 / R1) / (mu0 * theta * la)
        Reluc_list[:, 1] = 0.5 * theta / (mu0 * la * np.log(R3 / R1))
        Reluc_list[:, 2] = np.log(R3 / R2) / (mu0 * theta * la)
        Reluc_list[:, 3] = Reluc_list[:, 1]

    else:
        raise NameError("Wrong type_coord_sys, choice between 'cartesian' and 'polar'")

    return Reluc_list
