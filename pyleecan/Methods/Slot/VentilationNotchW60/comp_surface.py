from ....Functions.Load.import_class import import_class


def comp_surface(self):
    """Compute the surface of all the axial ventilation ducts

    Parameters
    ----------
    self : VentilationCirc
        A VentilationCirc object

    Returns
    -------
    Svent:
        Axial ventilation ducts total surface [m**2]

    """
    LamSlot = import_class("pyleecan.Classes", "LamSlot")
    self.check()
    lam = LamSlot(Rint=self.parent.slot.R1, is_internal=True, slot=self.notch_shape)
    return lam.slot.comp_surface()
