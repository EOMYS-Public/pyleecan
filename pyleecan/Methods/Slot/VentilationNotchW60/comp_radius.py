from ....Functions.Load.import_class import import_class


def comp_radius(self):
    """Compute the radius of the two circle that contains all the ventilation
    ducts

    Parameters
    ----------
    self : VentilationNotchW60
        A VentilationNotchW60 object

    Returns
    -------
    (Rmin, Rmax): tuple
        Tuple of circle radius [m]

    """
    LamSlot = import_class("pyleecan.Classes", "LamSlot")
    self.check()

    lam = LamSlot(Rint=self.parent.slot.R1, is_internal=True, slot=self.notch_shape)
    Rmin = self.parent.get_Rbo() - lam.slot.comp_height()
    Rmax = self.parent.get_Rbo()

    return (Rmin, Rmax)
