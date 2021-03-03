# -*- coding: utf-8 -*-
from numpy import pi

from ....Classes.LamSlotWind import LamSlotWind
from ....Classes.WindingCW import WindingCW


def comp_length_endwinding(self):
    """Compute the end winding conductor length on one side for a half-turn
    excluding the straight conductor length outside of the lamination (winding.Lewout).

    Parameters
    ----------
    self: EndWinding
        A EndWinding object
    Returns
    -------
    end_wind_length : float
        End-winding length on one side for a half-turn [m].
    """
    # ckeck that Endwinding is in Winding of a Lamination with slots
    if (
        self.parent is None
        or self.parent.parent is None
        or not isinstance(self.parent.parent, LamSlotWind)
        or self.parent.parent.slot is None
    ):
        self.get_logger.warning(
            "EndWindingCirc.comp_length_endwinding(): "
            + "EndWindingCirc has to be in a lamination with slot winding to calculate "
            + "the end winding length. Returning zero lenght."
        )
        return 0

    # get the middle radius of the slots active area
    Rmid = self.parent.parent.slot.comp_radius_mid_active()
    Zs = self.parent.parent.slot.Zs
    p = self.parent.p

    # get the slot pitch (with some fall backs), first from the user definition
    coil_pitch = self.coil_pitch
    if coil_pitch is None:
        # try to get coil_pitch of winding
        coil_pitch = getattr(self.parent, "coil_pitch", None)
        if coil_pitch is None:
            if isinstance(self.parent, WindingCW):
                coil_pitch = 1
            else:
                # finally use one pole pitch as coil pitch
                coil_pitch = Zs / p / 2

    # calculate the length as a half circle
    end_wind_length = pi * Rmid * coil_pitch

    return end_wind_length