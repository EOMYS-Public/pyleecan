from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW29 import SlotW29


def select_slot_rules(self, is_stator):
    """select step to add rules for slot and converts slot

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    # Single set
    # Single type

    # select slot type and add it to obj machine or in dict
    if self.is_P_to_other:
        self.convert_slot_to_other()
    else:
        self.convert_slot_to_P()

    slot = self.machine.stator.slot
    # add the correct rule depending on the slot
    if isinstance(slot, SlotW11):
        self.add_rule_slotW11(is_stator)
    elif isinstance(slot, SlotW14):
        self.add_rule_slotW14(is_stator)
    elif isinstance(slot, SlotW21):
        self.add_rule_slotW21(is_stator)
    elif isinstance(slot, SlotW23):
        self.add_rule_slotW23(is_stator)
    elif isinstance(slot, SlotW29):
        self.add_rule_slotW29(is_stator)