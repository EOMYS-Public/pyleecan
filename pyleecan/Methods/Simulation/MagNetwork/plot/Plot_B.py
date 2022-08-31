# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 10:02:37 2022
@author: LAP02
"""

from turtle import color, width
import matplotlib.pyplot as plt
import numpy as np


def Plot_B(
    self,
    Bx,
    By,
    x,
    y,
    x_dual,
    y_dual,
    list_geometry,
    type_coord_sys,
    list_coord,
    pos_aigap=None,
):
    """
    Parameters
    ----------
    Bx : TYPE
        DESCRIPTION.
    By : TYPE
        DESCRIPTION.
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.
    x_dual : TYPE
        DESCRIPTION.
    y_dual : TYPE
        DESCRIPTION.
    list_geometry : TYPE
        DESCRIPTION.
    m : TYPE
        DESCRIPTION.
    n : TYPE
        DESCRIPTION.
    Returns
    -------
    None.
    """
    # Getting the norm of the magnetix flux density B

    norm = np.sqrt(Bx ** 2 + By ** 2)
    if type_coord_sys == 1:
        k = 1
        skip = (slice(None, None, k), slice(None, None, k))

        # Defining the mesh grid (x, y)
        X, Y = np.meshgrid(x, y)

        # Plotting list_geometry
        plt.pcolormesh(
            X[skip],
            Y[skip],
            list_geometry.reshape((y.size - 1, x.size - 1))[skip],
            cmap="Paired",
            edgecolors=None,
            facecolors="none",
            alpha=0.6,
            linewidths=0.005,
        )

        # Defining the mesh grid (x_dual, y_dual)
        X, Y = np.meshgrid(x_dual, y_dual)

        # Plotting the magnetic flux density B
        plt.quiver(
            X[skip],
            Y[skip],
            Bx[skip] / norm[skip],
            By[skip] / norm[skip],
            norm[skip],
            cmap="cool",
            units="width",
            angles="xy",
            scale=30,
            width=0.01,
        )
    else:
        X = (list_coord[:, 1] * np.cos(list_coord[:, 0])).reshape(y.size, x.size)
        Y = (list_coord[:, 1] * np.sin(list_coord[:, 0])).reshape(y.size, x.size)

        X, Y = X.reshape((y.size, x.size)), Y.reshape((y.size, x.size))

        plt.pcolormesh(
            X,
            Y,
            norm.reshape(y_dual.size, x_dual.size),
        )

        # Defining the colorbar
        cbar = plt.colorbar()
        # Plotting list_geometry
        plt.pcolormesh(
            X,
            Y,
            list_geometry.reshape((y.size - 1, x.size - 1)),
            cmap="Paired",
            edgecolors=None,
            facecolors="none",
            alpha=0.6,
            linewidths=0.005,
        )

        # X, Y = np.meshgrid(x_dual, y_dual)
        # X, Y = Y * np.cos(X), Y * np.sin(X)
        # plt.contour(X, Y, norm.reshape(y_dual.size, x_dual.size))

        if pos_aigap != None:
            plt.plot(
                y_dual[pos_aigap] * np.cos(x_dual),
                y_dual[pos_aigap] * np.sin(x_dual),
                linewidth=2,
                color="black",
            )

    # Defining the graph title
    cbar.ax.set_title("B (Tesla)")

    # Showing the final plot
    plt.show()
    return
