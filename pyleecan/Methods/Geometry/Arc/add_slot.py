from numpy import exp, angle
from ....Functions.Load.import_class import import_class

def add_slot(self, position, slot, is_outwards):
    """Add a slot on the arc

    Parameters
    ----------
    self : Arc
        An Arc object
    position : float
        Position of the slot [0=Begin, 1=end]
    slot : Slot
        Slot object to add on the arc
    is_outwards : bool
        Direction to add the slot lines

    Returns
    -------
    line_list : [Line]
        List of line to draw the arc and the slot
    """
    LamSlot = import_class("pyleecan.Classes", "LamSlot")
    if position > 1 or position < 0:
        raise Exception("Error position should be >0 and <1")

    # Create a mock lamination to make slot methods work
    lam = LamSlot(is_stator=True, is_internal=not is_outwards, slot=slot)
    if is_outwards:
        lam.Rint = self.comp_radius()
    else:
        lam.Rext = self.comp_radius()

    slot_op = slot.comp_angle_opening()
    arc_angle = self.get_angle()
    if abs(slot_op) > abs(arc_angle):
        raise Exception("Slot is larger than the arc")

    # Find rotation angle for the slot
    Zb = self.get_begin()
    Ze = self.get_end()
    Zc = self.get_center()

    Zb_c = Zb - Zc
    # Position of center of slot opening arc
    Zmid_slot_c = Zb_c * exp(1j * arc_angle * position)
    if arc_angle < 0:
        Z_slot_begin_c = Zmid_slot_c * exp(1j * slot_op / 2)
        Z_slot_end_c = Zmid_slot_c * exp(-1j * slot_op / 2)
    else:
        Z_slot_begin_c = Zmid_slot_c * exp(-1j * slot_op / 2)
        Z_slot_end_c = Zmid_slot_c * exp(1j * slot_op / 2)

    line_list = list()
    arc_begin = self.copy()
    arc_begin.split_point(Z_slot_begin_c + Zc, is_begin=True)
    line_list.append(arc_begin)

    slot_lines = slot.build_geometry()
    # Reverse the slot to match arc direction
    if arc_angle < 0:
        slot_lines = slot_lines[::-1]
        for line in slot_lines:
            line.reverse()
    # Move the slot lines on the arc
    for line in slot_lines:
        line.rotate(angle(Zmid_slot_c))
        line.translate(Zc)
        line_list.append(line)

    arc_end = self.copy()
    arc_end.split_point(Z_slot_end_c + Zc, is_begin=False)
    line_list.append(arc_end)

    return line_list
