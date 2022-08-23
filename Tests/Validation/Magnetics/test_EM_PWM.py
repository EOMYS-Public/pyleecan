from os.path import join
from matplotlib.colors import get_named_colors_mapping
from matplotlib import pyplot as plt

import pytest
from numpy.testing import assert_array_almost_equal
from numpy import cos, pi, repeat, where, array, ones

from Tests import save_plot_path as save_path
from pyleecan.Classes.ImportData import ImportData
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
#from pyleecan.Classes.MagPMMF import MagPMMF
from pyleecan.Classes.ImportGenPWM import ImportGenPWM
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_PMSM import EEC_PMSM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Functions.Winding.gen_phase_list import gen_name

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D, dict_3D
from pyleecan.definitions import DATA_DIR

is_show_fig = False
SVPWM = 7
SPWM = 8


@pytest.mark.long_5s
@pytest.mark.IPMSM
@pytest.mark.MagFEMM
@pytest.mark.MagPMMF
def test_EM_PWM():
    """Test to compare PWM calculated with PMMF and FEMM"""

    # machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    machine = load(join(DATA_DIR, "Machine", "LSRPM_005.json"))
    fig=plt.subplot()
    machine.plot()
    #plt.savefig('hah.png',bbox_inches='tight',dpi=fig.dpi,pad_inches=0.0)

    name = "test_EM_PWM"

    simu = Simu1(name=name + "", machine=machine)

    Vdc1 = 500
    fswi = 10
    freq_max=10
    N0=15
    Phi0=pi

    # Definition of the input
    simu.input = InputCurrent(
        OP=OPdq(N0=N0, Id_ref=0, Iq_ref=6), ##4.64
        Na_tot=10,
        Nt_tot=10,
        # Na_tot=256 * 8,
        # Nt_tot=256 * 8,
        PWM=ImportGenPWM(fmax=2 * freq_max,fswi=fswi, Vdc1=Vdc1, typePWM=SPWM, Phi0=Phi0),
    )

    # simu.input = InputVoltage(
    #     OP=OPdq(N0=N0, Ud_ref=0, Uq_ref=169),
    #     Na_tot=500 * 10,
    #     Nt_tot=500 * 50,
    #     # Na_tot=256 * 8,
    #     # Nt_tot=256 * 8,
    #     PWM=ImportGenPWM(fmax=2 * freq_max, fswi=fswi, Vdc1=Vdc1, typePWM=SPWM,Phi0=Phi0),
    # )

    simu.elec = Electrical(
        eec=EEC_PMSM(
                Ld= 20.8*1e-3,
                Lq= 20.8*1e-3,
  
        ),
        freq_max=freq_max
    )
    FEMM_dict = dict()
    FEMM_dict["mesh"] = dict()
    # rotor yoke region mesh and segments max element size parameter
    FEMM_dict["mesh"]["meshsize_yokeR"] = 0.005
    FEMM_dict["mesh"]["elementsize_yokeR"] = 0.005

    FEMM_dict["mesh"]["elementsize_slotR"] = 0.0001
    FEMM_dict["mesh"]["elementsize_slotS"] = 0.0005
    # FEMM_dict["arcspan"] = 5  # max span of arc element in degrees

    # airgap region mesh and segments max element size parameter
    FEMM_dict["mesh"]["meshsize_airgap"] = 0.0001
    FEMM_dict["mesh"]["elementsize_airgap"] = 0.0001

    # Definition of the magnetic simulation (permeance mmf / FEA)
    #simu.mag = MagPMMF(is_periodicity_a=True, is_periodicity_t=True)
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True, nb_worker=5,FEMM_dict_enforced=FEMM_dict,)


    out = simu.run()
    out.save("D:/StageSijie/PrototypeEOMYS/Test_data/test_29_07_2022.h5")

    #out = load("D:/StageSijie/PrototypeEOMYS/Test_data/test_23_02_2022.h5")

    # out.elec.Is.plot_2D_Data(
    #     "time=axis_data",
    #     "phase[]",
    #     axis_data={"time": out.elec.axes_dict["time"].get_values()},
    # )

    # out.elec.Is.plot_2D_Data("freqs=[0, 20000]", "phase[0]", is_auto_range=False)

    # Is_dqh = out.elec.get_Is(is_freq=True, is_dqh=True)
    # out.elec.Us.plot_2D_Data(     "time=axis_data",
    #     "phase[0]",
    #     axis_data={"time": out.elec.axes_dict["time"].get_values()},)

    # Is_dqh.plot_2D_Data(
    #     "time=axis_data",
    #     "phase[]",
    #     axis_data={"time": out.elec.axes_dict["time"].get_values()},
    # )

    # out.mag.B.plot_2D_Data(
    #     "time",
    #     # data_list=[out.mag.B, out.mag.B_harm],
    #     # legend_list=["B", "B_fund", "B_harm"],
    #     # save_path=join(save_path, "test_harm_IPMSM.png"),
    #     # is_show_fig=False,
    #     **dict_2D
    # )

    # out.mag.B.plot_2D_Data(
    #     "angle",
    #     # data_list=[out.mag.B, out.mag.B_harm],
    #     # legend_list=["B", "B_fund", "B_harm"],
    #     # save_path=join(save_path, "test_harm_IPMSM.png"),
    #     # is_show_fig=False,
    #     **dict_2D
    # )

    out.mag.B.plot_3D_Data("time", "angle", **dict_3D)

    out.mag.B.plot_3D_Data("freqs=[0,20000]", "wavenumber", **dict_3D)
    #out.elec.Is.plot_2D_Data("freqs=[0, 20000]", "phase[0]", is_auto_range=False,barwidth=600)
    out.mag.B.plot_2D_Data("freqs=[0,20000]", barwidth=600)
    #out.elec.Us.plot_2D_Data("freqs=[0,20000]", barwidth=600)

    return out

    # # Calculate PWM current
    # simu_ref = simu.copy()
    # simu_ref.input = InputCurrent(
    #     Ir=None,
    #     Na_tot=2048,
    #     Nt_tot=Nt_tot,
    #     OP=OPdq(N0=5000, Id_ref=0, Iq_ref=0),
    #     angle_rotor_initial=0,
    # )

    # out_ref = simu_ref.run()
    # axes = simu_ref.input.comp_axes(axes_list=["time"])

    # time_val = axes["time"].get_values()
    # fs = out_ref.elec.felec

    # Is_val = cos(2 * pi * fs * time_val)
    # # Is_val = cos(2*pi*1 * fs * time_val)
    # Is = ImportMatrixVal(value=repeat(Is_val[:, None], 3, axis=1))

    # qs = simu_ref.machine.stator.winding.qs
    # Freqs = ImportData(
    #     field=ImportMatrixVal(value=array([5 * fs, 15 * fs])), name="freqs", unit="Hz"
    # )
    # Phase = ImportData(field=ImportMatrixVal(value=gen_name(qs)), name="phase")

    # I_harm = ImportData(
    #     axes=[Freqs, Phase],
    #     field=ImportMatrixVal(value=1 * ones((2, 3))),
    #     unit="A",
    #     name="Harmonic current",
    #     symbol="I_{harm}",
    # )

    # simu.input = InputCurrent(Is=Is, OP=OPdq(N0=2504), Nt_tot=Nt_tot, Is_harm=I_harm)

    # simu.elec = None
    # simu.force = None
    # simu.struct = None
    # simu.acoustic = None

    # # Definition of the magnetic simulation (permeance mmf)
    # simu.mag = MagPMMF(
    #     is_periodicity_a=True,
    #     is_periodicity_t=True,
    #     is_current_harm=False,
    #     model_harm=MagPMMF(),
    #     is_mmfr=False,
    # )

    # out = simu.run()

    # # Second simu without convolution
    # Is_val2 = (
    #     cos(2 * pi * fs * time_val)
    #     + cos(2 * pi * 5 * fs * time_val)
    #     + cos(2 * pi * 15 * fs * time_val)
    # )
    # # Is_val = cos(2*pi*1 * fs * time_val)
    # Is2 = ImportMatrixVal(value=repeat(Is_val2[:, None], 3, axis=1))

    # simu2 = simu.copy()
    # simu2.input = InputCurrent(Is=Is2, OP=OPdq(N0=2504), Nt_tot=Nt_tot)
    # simu2.mag = MagPMMF(
    #     is_periodicity_a=True,
    #     is_periodicity_t=True,
    #     is_current_harm=True,
    #     model_harm=None,
    #     is_mmfr=False,
    # )

    # out2 = simu2.run()

    # out2.mag.B.plot_2D_Data(
    #     "freqs",
    #     data_list=[out.mag.B, out.mag.B_harm],
    #     legend_list=["B", "B_fund", "B_harm"],
    #     save_path=join(save_path, "test_harm_IPMSM.png"),
    #     is_show_fig=False,
    #     **dict_2D
    # )

    # return out, out2


# To run it without pytest
if __name__ == "__main__":
    out = test_EM_PWM()



    plt.show()


