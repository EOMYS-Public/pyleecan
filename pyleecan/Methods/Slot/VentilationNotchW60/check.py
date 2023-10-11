from ....Functions.Load.import_class import import_class


def check(self):
    """Make sure that the ventilation parameters are correctly set

    Parameters
    ----------
    self : VentilationNotchW60
        A VentilationNotchW60 object

    Returns
    -------
    None

    Raises
    _______
    Exceptions

    """
    LamSlotWind = import_class("pyleecan.Classes", "LamSlotWind")
    SlotW60 = import_class("pyleecan.Classes", "SlotW60")

    if not isinstance(self.parent, LamSlotWind):
        raise Exception("VentilationNotchW60 must be set on a LamSlotWind")
    if not self.parent.is_internal:
        raise Exception("VentilationNotchW60 must be set on internal lamination")
    if not isinstance(self.parent.slot, SlotW60):
        raise Exception("VentilationNotchW60 must be set on a LamSlotWind with SlotW60")
