# -*- coding: utf-8 -*-

import numpy as np


def get_node2element(self, node_indice):
    """Return all element indices of elements containing a node.

    Parameters
    ----------
    self : MeshMat
        an MeshMat object
    node_indice : int
        a node indice

    Returns
    -------
    node_to_element: ndarray
        Indices of elements containing the node

    """
    element_indices = np.concatenate(
        [element.get_node2element(node_indice) for element in self.element.values()]
    )

    return element_indices