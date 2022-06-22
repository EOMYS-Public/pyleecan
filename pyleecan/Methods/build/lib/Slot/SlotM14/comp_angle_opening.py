# -*- coding: utf-8 -*-

from numpy import arcsin


def comp_angle_opening(self):
    """Compute the average opening angle of the Slot

    Parameters
    ----------
    self : SlotM14
        A SlotM14 object

    Returns
    -------
    alpha: float
        Average opening angle of the slot [rad]

    """

    return self.W0
