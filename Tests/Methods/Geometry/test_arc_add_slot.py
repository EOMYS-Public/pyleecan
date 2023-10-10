
from numpy import exp, pi
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.SlotM10 import SlotM10
import matplotlib.pyplot as plt

def test_Arc_centered():
    """Rectangular slot on an Arc centered on Ox + centre 0
    """

    arc = Arc1(begin=exp(1j*pi/4), end=exp(-1j*pi/4), radius=-1,is_trigo_direction=False)
    assert arc.get_center() == 0
    assert arc.get_angle() == -pi/2

    slot = SlotM10(Zs=4, W0=0.1, H0=0.2)

    line_list = arc.add_slot(position=0.5,slot=slot,is_outwards=True)
    plot_line_list(arc, line_list, "alpha<0, pos=0.5")

    # Change slot position
    line_list = arc.add_slot(position=0.25,slot=slot,is_outwards=True)
    plot_line_list(arc, line_list, "alpha<0, pos=0.25")

    # Same arc but reversed
    arc.reverse()
    assert arc.get_center() == 0
    assert arc.get_angle() == pi/2
    line_list = arc.add_slot(position=0.5,slot=slot,is_outwards=False)
    plot_line_list(arc, line_list, "alpha>0, pos=0.5")

    # Change slot position
    line_list = arc.add_slot(position=0.25,slot=slot,is_outwards=False)
    plot_line_list(arc, line_list, "alpha>0, pos=0.25")
    pass

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

if __name__ == "__main__":
    test_Arc_centered()
    print("Done")
