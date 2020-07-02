# -*- coding: utf-8 -*-

import pyvistaqt as pv

from ....Classes.MeshMat import MeshMat


def plot_mesh(self, label=None, index=None, indices=None):
    """Plot the mesh using pyvista plotter.

    Parameters
    ----------
    self : MeshSolution
        a MeshSolution object
    label : str
        a label
    index : int
        an index
    indices : list
        list of the points to extract (optional)

    Returns
    -------
    """

    # Get the mesh
    mesh_obj = self.get_mesh(label=label, index=index)
    if isinstance(mesh_obj, MeshMat):
        mesh = mesh_obj.get_mesh_pv(indices=indices)
    else:
        mesh = mesh_obj.get_mesh(indices=indices)

    # Configure plot
    p = pv.BackgroundPlotter()
    p.set_background("white")
    p.add_mesh(
        mesh, color="grey", opacity=1, show_edges=True, edge_color="white", line_width=1
    )
    p.show()