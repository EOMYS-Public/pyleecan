def other_to_P(self, machine, other_dict, other_unit_dict):
    """Adapt the rule complex slotW11_H1

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A obj machine
    other_dict : dict
        A dict with the conversion obj machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    Return
    ---------
    machine : Machine
        A obj machine
    """
    H1 = machine.stator.slot.get_H1()
    machine.stator.slot.H1_is_rad = False
    machine.stator.slot.H1 = H1

    return machine


def P_to_other(self, machine, other_dict):
    """Adapt the rule complex slotW11_H1

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    machine : Machine
        A obj machine
    other_dict : dict
        A dict

    Return
    ---------
    other_dict : dict
        A dict
    """
    print("other_to_P")
    return other_dict