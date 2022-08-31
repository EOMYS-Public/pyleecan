# Load the machine
from os.path import join
from pyleecan.Classes.MagNetwork import MagNetwork
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
import matplotlib.pyplot as plt
import pytest
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Functions.Plot import dict_2D

is_show_fig = True


@pytest.mark.MagNetwork
def test_MagNetwork_initial_validation():
    """Test MagNetwork simulation with of a 1/4 article-based SPMSM equipped with
    12 slots and 4 poles. Its windings are single layer.
    Ref: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9473194"""

    # Case 0 : Load the machine and create the Simulation
    file_path0 = "C:/Users/pc/Downloads/SPMSM_val.json"
    SPMSM_12s_4p_initial = load(file_path0)

    simu = Simu1(name="test_magnetwork_case0", machine=SPMSM_12s_4p_initial)

    # Defining Simulation Input
    simu.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=180 * 4,
        Nt_tot=1,
    )

    # Defining the magnetic simulation of MagNetwork
    simu.mag = MagNetwork(
        is_periodicity_a=True,
        is_periodicity_t=False,
        type_model=1,
        type_coord_sys=2,
        stator_yoke_elements_r=2,
        airgap_elements_r=2,
        rotor_yoke_elements_r=2,
        stator_isthmus_elements_r=1,
        stator_tooth_elements_r=11,
        magnet_elements_r=11,  ###
        Kmesh_fineness=2,
        rotor_shift=8,
    )

    # Initializing the harmonics calculation for simu
    simu.force = ForceMT()

    # Creating the simulation object of the FEMM
    simu2 = Simu1(name="test_FEMM_case0", machine=SPMSM_12s_4p_initial)

    # FEMM simulation
    simu2.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=180 * 4,
        Nt_tot=1,
        is_periodicity_t=False,
        is_periodicity_a=True,
        angle_rotor_initial=1.0e-12,
    )

    # Defining the magnetic simulation of MagFEMM
    simu2.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=4,  # number of FEMM windows to be opened
        is_get_meshsolution=True,  # Get the mesh solution
        is_fast_draw=True,
        is_calc_torque_energy=False,
        Kmesh_fineness=2,  # Define the mesh fineness
    )

    # Initializing the harmonics calculation for simu3
    simu2.force = ForceMT()

    # Running both simulations
    out = simu.run()  # MagNetwork
    out2 = simu2.run()  # FEMM

    # Comparison of the radial 2D flux density curve between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "angle[smallestperiod]{°}",
        component_list=["radial"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )

    # Comparison of the tangential 2D flux density curve between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "angle[smallestperiod]{°}",
        component_list=["tangential"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )

    # Comparison of the fft between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "wavenumber=[0,10]",
        component_list=["radial"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )
    return


def test_MagNetwork_Kmesh_fineness():
    """Test MagNetwork simulation with of a 1/4 SPMSM equipped with
    12 slots and 4 poles and modify Kmesh_fineness values = {1,2}"""

    # Case 1 : Load the machine and create the Simulation
    file_path1 = "C:/Users/pc/Downloads/easy_test_MagNetwork.json"
    SPMSM_12s_4p_fourth_k1 = load(file_path1)

    simu = Simu1(name="test_magnetwork_k1_case1", machine=SPMSM_12s_4p_fourth_k1)

    # Defining Simulation Input
    simu.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=45 * 4,
        Nt_tot=1,
    )

    # Defining the magnetic simulation of MagNetwork
    simu.mag = MagNetwork(
        is_periodicity_a=True,
        is_periodicity_t=False,
        type_model=1,
        type_coord_sys=2,
        N_point_r=65,
        Kmesh_fineness=1,
        rotor_shift=8,
    )

    # Initializing the harmonics calculation for simu
    simu.force = ForceMT()

    # Define the machine with Kmesh_fineness = 2
    # SPMSM_12s_4p_fourth_k2 = SPMSM_12s_4p_fourth_k1.copy()
    simu2 = Simu1(name="test_magnetwork_k2_case1", machine=SPMSM_12s_4p_fourth_k1)

    # Defining Simulation Input, Kmesh_fineness=2
    simu2.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=90 * 4,
        Nt_tot=1,
    )

    # Defining the magnetic simulation of MagNetwork, Kmesh_fineness=2
    simu2.mag = MagNetwork(
        is_periodicity_a=True,
        is_periodicity_t=False,
        type_model=1,
        type_coord_sys=2,
        N_point_r=65,
        Kmesh_fineness=2,
        rotor_shift=8,
    )

    # Initializing the harmonics calculation for simu2
    simu2.force = ForceMT()

    # Creating the simulation object of the FEMM
    simu3 = Simu1(name="test_FEMM_case1", machine=SPMSM_12s_4p_fourth_k1)

    # FEMM simulation
    simu3.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=45 * 4,
        Nt_tot=1,
        is_periodicity_t=False,
        is_periodicity_a=True,
        angle_rotor_initial=1.0e-12,
    )

    # Defining the magnetic simulation of MagFEMM
    simu3.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=4,  # number of FEMM windows to be opened
        is_get_meshsolution=True,  # Get the mesh solution
        is_fast_draw=True,
        is_calc_torque_energy=False,
        Kmesh_fineness=2,  # Define the mesh fineness
    )

    # Initializing the harmonics calculation for simu3
    simu3.force = ForceMT()

    # Running both simulations
    out = simu.run()  # MagNetwork, Kmesh_fineness=1
    out2 = simu2.run()  # MagNetwork, Kmesh_fineness=2
    out3 = simu3.run()  # FEMM

    # Comparison of the radial 2D flux density curve between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "angle[smallestperiod]{°}",
        component_list=["radial"],
        data_list=[out2.mag.B, out3.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=1",
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )

    # Comparison of the tangential 2D flux density curve between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "angle[smallestperiod]{°}",
        component_list=["tangential"],
        data_list=[out2.mag.B, out3.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=1",
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )

    # Comparison of the fft between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "wavenumber=[0,10]",
        component_list=["radial"],
        data_list=[out2.mag.B, out3.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=1",
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )
    return


def test_MagNetwork_double_layer_2magnets():
    """Test MagNetwork simulation with of a 1/4 SPMSM equipped with
    12 slots and 8 poles. Its windings are single layer."""

    # Case 2 : Load the machine and create the Simulation
    # file_path2 = "C:/Users/pc/Downloads/easy_test_MagNetwork2.json"
    file_path2 = "C:/Users/pc/Downloads/validation_2pms.json"
    SPMSM_12s_8p_fourth = load(file_path2)

    simu = Simu1(name="test_magnetwork_case2", machine=SPMSM_12s_8p_fourth)

    # Defining Simulation Input
    simu.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=180 * 4,
        Nt_tot=1,
    )

    # Defining the magnetic simulation of MagNetwork
    simu.mag = MagNetwork(
        is_periodicity_a=True,
        is_periodicity_t=False,
        type_model=1,
        type_coord_sys=2,
        stator_yoke_elements_r=2,
        airgap_elements_r=2,
        rotor_yoke_elements_r=2,
        stator_isthmus_elements_r=1,
        stator_tooth_elements_r=11,
        magnet_elements_r=10,
        Kmesh_fineness=2,
        rotor_shift=8,
    )

    # Initializing the harmonics calculation for simu
    simu.force = ForceMT()

    # Creating the simulation object of the FEMM
    simu2 = Simu1(name="test_FEMM_case2", machine=SPMSM_12s_8p_fourth)

    # FEMM simulation
    simu2.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=180 * 4,
        Nt_tot=1,
        is_periodicity_t=False,
        is_periodicity_a=True,
        angle_rotor_initial=1.0e-12,
    )

    # Defining the magnetic simulation of MagFEMM
    simu2.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=4,  # number of FEMM windows to be opened
        is_get_meshsolution=True,  # Get the mesh solution
        is_fast_draw=True,
        is_calc_torque_energy=False,
        Kmesh_fineness=2,  # Define the mesh fineness
    )

    # Initializing the harmonics calculation for simu3
    simu2.force = ForceMT()

    # Running both simulations
    out = simu.run()  # MagNetwork
    out2 = simu2.run()  # FEMM

    # Comparison of the radial 2D flux density curve between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "angle[smallestperiod]{°}",
        component_list=["radial"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )

    # Comparison of the tangential 2D flux density curve between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "angle[smallestperiod]{°}",
        component_list=["tangential"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )

    # Comparison of the fft between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "wavenumber=[0,10]",
        component_list=["radial"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )
    return


def test_MagNetwork_fractional_periodicity():
    """Test MagNetwork simulation with of a 1/3 SPMSM equipped with
    12 slots and 16 poles. Its windings are double layer and the periodicity = 1.5"""

    # Case 3 : Load the machine and create the Simulation
    file_path3 = "C:/Users/pc/Downloads/easy_test_MagNetwork3.json"
    SPMSM_12s_16p_fractional = load(file_path3)

    simu = Simu1(name="test_magnetwork_case3", machine=SPMSM_12s_16p_fractional)

    # Defining Simulation Input
    simu.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=120 * 3,
        Nt_tot=1,
    )

    # Defining the magnetic simulation of MagNetwork
    simu.mag = MagNetwork(
        is_periodicity_a=True,
        is_periodicity_t=False,
        type_model=1,
        type_coord_sys=2,
        N_point_r=57,
        Kmesh_fineness=2,
        rotor_shift=8,
    )

    # Initializing the harmonics calculation for simu
    simu.force = ForceMT()

    # Creating the simulation object of the FEMM
    simu2 = Simu1(name="test_FEMM_case3", machine=SPMSM_12s_16p_fractional)

    # FEMM simulation
    simu2.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=120 * 3,
        Nt_tot=1,
        is_periodicity_t=False,
        is_periodicity_a=True,
        angle_rotor_initial=1.0e-12,
    )

    # Defining the magnetic simulation of MagFEMM
    simu2.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=4,  # number of FEMM windows to be opened
        is_get_meshsolution=True,  # Get the mesh solution
        is_fast_draw=True,
        is_calc_torque_energy=False,
        Kmesh_fineness=2,  # Define the mesh fineness
    )

    # Initializing the harmonics calculation for simu3
    simu2.force = ForceMT()

    # Running both simulations
    out = simu.run()  # MagNetwork
    out2 = simu2.run()  # FEMM

    # Comparison of the radial 2D flux density curve between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "angle[smallestperiod]{°}",
        component_list=["radial"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )

    # Comparison of the tangential 2D flux density curve between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "angle[smallestperiod]{°}",
        component_list=["tangential"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )

    # Comparison of the fft between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "wavenumber=[0,10]",
        component_list=["radial"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )
    return


def test_MagNetwork_benchmark():
    """Test MagNetwork simulation with of a 1/2 benchmark SPMSM equipped with
    12 slots and 10 poles. Its windings are double layer and the periodicity = 1"""

    # Case 4 : Load the machine and create the Simulation
    file_path4 = "C:/Users/pc/AppData/Roaming/pyleecan/Machine/Benchmark.json"
    SPMSM_12s_10p_benchmark = load(file_path4)

    simu = Simu1(name="test_magnetwork_case4", machine=SPMSM_12s_10p_benchmark)

    # Defining Simulation Input
    simu.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=540 * 2,
        Nt_tot=1,
    )

    # Defining the magnetic simulation of MagNetwork
    simu.mag = MagNetwork(
        is_periodicity_a=True,
        is_periodicity_t=False,
        type_model=1,
        type_coord_sys=2,
        N_point_r=33,
        Kmesh_fineness=2,
        rotor_shift=8,
    )

    # Initializing the harmonics calculation for simu
    simu.force = ForceMT()

    # Creating the simulation object of the FEMM
    simu2 = Simu1(name="test_FEMM_case4", machine=SPMSM_12s_10p_benchmark)

    # FEMM simulation
    simu2.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=540 * 2,
        Nt_tot=1,
        is_periodicity_t=False,
        is_periodicity_a=True,
        angle_rotor_initial=1.0e-12,
    )

    # Defining the magnetic simulation of MagFEMM
    simu2.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=4,  # number of FEMM windows to be opened
        is_get_meshsolution=True,  # Get the mesh solution
        is_fast_draw=True,
        is_calc_torque_energy=False,
        Kmesh_fineness=2,  # Define the mesh fineness
    )

    # Initializing the harmonics calculation for simu3
    simu2.force = ForceMT()

    # Running both simulations
    out = simu.run()  # MagNetwork
    out2 = simu2.run()  # FEMM

    # Comparison of the radial 2D flux density curve between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "angle[smallestperiod]{°}",
        component_list=["radial"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )

    # Comparison of the tangential 2D flux density curve between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "angle[smallestperiod]{°}",
        component_list=["tangential"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )

    # Comparison of the fft between MagNetwork and FEMM
    out.mag.B.plot_2D_Data(
        "wavenumber=[0,10]",
        component_list=["radial"],
        data_list=[out2.mag.B],
        legend_list=[
            "MagNetwork, Kmesh_fineness=2",
            "FEMM",
        ],
        is_show_fig=True,
    )
    return


if __name__ == "__main__":
    test_MagNetwork_initial_validation()
    # test_MagNetwork_Kmesh_fineness()
    # test_MagNetwork_double_layer_2magnets()
    # test_MagNetwork_fractional_periodicity()
    # test_MagNetwork_benchmark()