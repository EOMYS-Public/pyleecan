# Method to compute the air gap magnetic flux density localy
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# def comp_flux_airgap(self, output, axes_dict, Is_val=None, Ir_val=None):
def comp_flux_airgap_local(self, r, theta, Phi, list_elem, list_coord, la, Rgap,N_point_r,N_point_theta,type_coord_sys):

    # Computing the radial and tangential flux density
    Bx, By = self.compute_B(Phi, list_elem, list_coord, la,type_coord_sys)

    # Reshaping B in a 2D array
    Bx = Bx.reshape((N_point_r-1,N_point_theta-1))
    By = By.reshape((N_point_r-1,N_point_theta-1))

    # Looking for the position in the center of the mecanical airgap
    position = Rgap

    # Getting the index of the line i from the position in the center of the mecanical airgap
    index_airgap = (int)((position - r.min()) * ((r.size - 1) / (r.max() - r.min())))

    # print("The horizental line in the airgap is: ", position, i)

    return Bx[index_airgap, :], By[index_airgap, :]
