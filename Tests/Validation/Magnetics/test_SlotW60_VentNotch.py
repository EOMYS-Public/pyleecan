from os.path import join, isdir
from os import makedirs
from multiprocessing import cpu_count
import matplotlib.pyplot as plt
import pytest
from Tests import save_validation_path as save_path

from numpy import exp, sqrt, pi, max as np_max
from numpy.testing import assert_array_almost_equal

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.SlotCirc import SlotCirc
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.VentilationNotchW60 import VentilationNotchW60
from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D

from pyleecan.definitions import DATA_DIR


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_VentNotchW60():
    """Validation of LamHoleNS in FEMM"""
    res_path = join(save_path, "VentNotchW60")
    if not isdir(res_path):
        makedirs(res_path)
    Zoe = load(join(DATA_DIR, "Machine", "Renault_Zoe.json"))

    # Add notches as ventilation
    vent_circ = VentilationNotchW60(Zh=Zoe.rotor.slot.Zs,position=0.5,notch_shape=SlotCirc(W0=10e-3,H0=5e-3,Zs=8))
    vent_rect_25 = VentilationNotchW60(Zh=Zoe.rotor.slot.Zs,position=0.25,notch_shape=SlotM10(W0=10e-3,H0=5e-3,Zs=8))
    vent_rect_75 = VentilationNotchW60(Zh=Zoe.rotor.slot.Zs,position=0.75,notch_shape=SlotM10(W0=10e-3,H0=20e-3,Zs=8))
    Zoe.rotor.axial_vent = [vent_circ, vent_rect_25, vent_rect_75]

    # Check plot machine
    fig, ax = Zoe.plot(
        sym=4,
        is_clean_plot=True,
        is_show_fig=False,
    )
    fig.savefig(join(res_path, "machine_sym.png"))
    fig.savefig(join(res_path, "machine_sym.svg"), format="svg")

    fig, ax = Zoe.plot(
        save_path=join(res_path, "machine_full.png"),
        is_clean_plot=True,
        is_show_fig=False,
    )
    fig.savefig(join(res_path, "machine_full.png"))
    fig.savefig(join(res_path, "machine_full.svg"), format="svg")
    plt.show()
    # Check periodicity
    assert Zoe.comp_periodicity_spatial() == (2, True)

    # Check machine in FEMM with sym
    simu = Simu1(name="test_FEMM_VentNotchW60", machine=Zoe)
    simu.path_result = join(save_path, simu.name)
    simu.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=2048,
        Nt_tot=1,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=cpu_count(),
        # Kmesh_fineness=2,
    )
    simu.path_result = join(res_path, simu.name)

    # Same simu without symetry
    simu2 = simu.copy()
    simu2.name = simu.name + "_Full"
    simu2.path_result = join(res_path, simu2.name)
    simu2.mag.is_periodicity_a = False

    # Run simulations
    out = simu.run()
    out2 = simu2.run()

    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[0]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    # Compare both simu
    Bflux = out.mag.B
    arg_list = ["angle"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]
    angle = result["angle"]

    Bflux2 = out2.mag.B
    arg_list = ["angle"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]

    assert_array_almost_equal(Brad, Brad2, decimal=1)
    return out


# To run it without pytest
if __name__ == "__main__":

    out = test_FEMM_VentNotchW60()
    print("Done")
