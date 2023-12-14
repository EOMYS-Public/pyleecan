# -*- coding: utf-8 -*-

from ....Methods.Slot.SlotW63 import *


def check(self):
    """Check that the SlotW63 object is correct

    Parameters
    ----------
    self : SlotW63
        A SlotW63 object

    Returns
    -------
    None
    Raises
    -------
    S63_InnerCheckError
        Slot 63 is for inner lamination only

    """
    if self.is_outwards():
        raise S63_InnerCheckError("Slot 63 is for inner lamination only")

    if self.W0 > self.W1:
        raise S63_WindHError("You must have W1 > W0")