from ....Methods.Slot.VentilationCirc import *
from ....Classes.SurfLine import SurfLine
from ....Functions.Load.import_class import import_class
import matplotlib.pyplot as plt
from ....Functions.labels import DRAW_PROP_LAB

def build_geometry(self, alpha=0, delta=0):
    """Compute the curve needed to plot the ventilations

    Parameters
    ----------
    self : VentilationNotchW60
        A VentilationNotchW60 object
    alpha : float
        Angle for rotation (Default value = 0) [rad]
    delta : complex
        Complex for translation (Default value = 0)

    Returns
    -------
    surf_list: list
        A list of lines

    """
    Arc1 = import_class("pyleecan.Classes", "Arc1")
    SlotW60 = import_class("pyleecan.Classes", "SlotW60")

    lam_label = self.parent.get_label()
    R_id, surf_type = self.get_R_id()
    RTS_id = "R" + str(R_id) + "-T0-S0"
    vent_label = lam_label + "_" + surf_type + "_" + RTS_id

    # checking if the param have good type
    if type(alpha) not in [int, float]:
        raise CircleBuildGeometryError("The parameter 'alpha' must be an int or float")
    if type(delta) not in [complex, int, float]:
        raise CircleBuildGeometryError(
            "The parameter 'delta' must be a complex or float or int number"
        )

    # This ventilation is meant to add notch on SlotW60
    slot = self.parent.slot
    assert isinstance(slot, SlotW60)

    line_dict = slot._comp_line_dict()
    top_arc = line_dict["tooth_top"]

    line_list = top_arc.add_slot(
        position=self.position, slot=self.notch_shape, is_outwards=False
    )
    # remove first and last line => remain of the original arc
    line_list = line_list[1:-1]
    # Add closing arc
    line_list.append(
        Arc1(
            begin=line_list[-1].get_end(),
            end=line_list[0].get_begin(),
            radius=-self.parent.slot.R1,
            is_trigo_direction=False,
            prop_dict= {DRAW_PROP_LAB:False}
        )
    )

    surf_list = list()
    surf_list.append(SurfLine(label=vent_label, line_list=line_list))
    surf_list[-1].comp_point_ref(is_set=True)

    return surf_list

def plot_line_list(arc, line_list, title=None):
    fig,ax = arc.plot(color="r")
    for ii, line in enumerate(line_list):
        line.plot(fig=fig,ax=ax,color="k", linestyle="--")
        mid = line.get_middle()
        ax.text(mid.real, mid.imag, str(ii))
    if title is not None:
        ax.set_title(title)
    # Axis Setup
    ax.axis("equal")
    plt.show()