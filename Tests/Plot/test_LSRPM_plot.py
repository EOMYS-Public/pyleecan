from os.path import join

import json
from pyleecan.Classes.Surface import Surface
import pytest
import matplotlib.pyplot as plt

from numpy import array, pi, zeros
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamHole import LamHole

from pyleecan.Classes.LamSlotWind import LamSlotWind

from pyleecan.Classes.BoreLSRPM import BoreLSRPM

from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.HoleMLSRPM import HoleMLSRPM
from Tests import save_plot_path as save_path
from pyleecan.Classes.SlotWLSRPM import SlotWLSRPM
from pyleecan.Classes.WindingUD import WindingUD


from pyleecan.Classes.CondType11 import CondType11
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Material import Material
from pyleecan.Classes.MatMagnetics import MatMagnetics

from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load


def test_LSRPM():
    mm = 1e-3  # Millimeter

    # Lamination setup
    stator = LamSlotWind(
        Rint=50.7 * mm,  # internal radius [m]
        Rext=72.5 * mm,  # external radius [m]
        L1=105
        * mm,  # Lamination stack active length [m] without radial ventilation airducts
        # but including insulation layers between lamination sheets
        Kf1=1,  # Lamination stacking / packing factor
        is_internal=False,
        is_stator=True,

    )

    # Slot setup
    stator.slot = SlotWLSRPM(
        Zs=12, W1=8e-3, W3=11.6e-3, H2=14.8e-3, R1=0.75e-3, H3=2e-3, # Slot number
    )

    # Winding setup (6 phases, stator + auxiliary)
    # wind_mat_LSRPM = zeros((2, 2, 12, 6))  # Nrad, Ntan, Zs, qs
    # wind_mat_LSRPM[0, 0, :, :] = array(
    #     [
    #         [-1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0],
    #         [0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0],
    #         [0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     ]
    # ).T

    # wind_mat_LSRPM[1, 0, :, :] = array(
    #     [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [-1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0],
    #         [0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0],
    #         [0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1],
    #     ]
    # ).T

    # wind_mat_LSRPM[0, 1, :, :] = array(
    #     [
    #         [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    #         [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    #         [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     ]
    # ).T

    # wind_mat_LSRPM[1, 1, :, :] = array(
    #     [
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    #         [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    #         [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    #     ]
    # ).T

    # Winding setup (only stator)
    wind_mat_LSRPM = zeros((1, 2, 12, 3))  # Nrad, Ntan, Zs, qs

    wind_mat_LSRPM[0, 1, :, :] = array(
        [
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        ]
    ).T
    wind_mat_LSRPM[0, 0, :, :] = array(
        [   
            [-1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0],
            [0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0],
            [0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1],
        ]
    ).T




    stator.winding = WindingUD(wind_mat=wind_mat_LSRPM, qs=3, p=4) #qs=6 (Stator + auxiliary)

    # Conductor setup
    stator.winding.conductor = CondType11(
        Nwppc_tan=1,  # stator winding number of preformed wires (strands)
        # in parallel per coil along tangential (horizontal) direction
        Nwppc_rad=1,  # stator winding number of preformed wires (strands)
        # in parallel per coil along radial (vertical) direction
        Wwire=0.001,  # single wire width without insulation [m]
        Hwire=0.001,  # single wire height without insulation [m]
        Wins_wire=1e-6,  # winding strand insulation thickness [m]
        type_winding_shape=1,  # type of winding shape for end winding length calculation
        # 0 for hairpin windings
        # 1 for normal windings
    )

    # Rotor setup
    # rotor = LamHole(
    #         Rint=14e-3, Rext=50e-3, is_stator=False, is_internal=True, L1=0.95
    # )

    rotor = LamHole(
        Rint=14e-3,
        Rext=50e-3,
        is_internal=True,
        is_stator=False,
        L1=0.105,
    )

    # Magnet setup
    rotor.hole = list()
    rotor.hole.append(
        HoleMLSRPM(
            Zh=8,
            W0=3.88e-3,
            W1=12.6 / 180 * pi,
            W2=0.0007,
            H1=0.0023515058436089,
            R1=0.0003,
            R2=0.019327,
            R3=0.0165,
        )
    )
    rotor.mat_type
    rotor.bore = BoreLSRPM(N=8, Rarc=0.0375, alpha=0)

    # Set shaft
    shaft = Shaft(
        Drsh=rotor.Rint * 2,  # Diamater of the rotor shaft [m]
        # used to estimate bearing diameter for friction losses
        Lshaft=1.2,  # length of the rotor shaft [m]
    )

    # Loading Materials
    M600_65A_50Hz = load(join(DATA_DIR, "Material", "M600-65A-50Hz.json"))
    Copper1 = load(join(DATA_DIR, "Material", "Copper1.json"))
    MagnetLSRPM = load(join(DATA_DIR, "Material", "CY-N28AH-20DEG.json"))

    # Set Materials
    stator.mat_type = M600_65A_50Hz
    rotor.mat_type = M600_65A_50Hz
    stator.winding.conductor.cond_mat = Copper1

    # Set magnets in the rotor hole
    rotor.hole[0].magnet_0.mat_type = MagnetLSRPM
    rotor.hole[0].magnet_0.type_magnetization = 0 # Radial magnet

    # matplotlib notebook
    LSRPM = MachineIPMSM(
        name="LSRPM LSEE", stator=stator, rotor=rotor, shaft=shaft, frame=None
    )
    LSRPM.save(join(DATA_DIR, "Machine", "LSRPM_003.json"))

    LSRPM.plot(is_show_fig=True, save_path=join(save_path, "test_LSRPM.png"))
    stator.plot(is_lam_only=True)
    Surface.plot
    plt.show()

if __name__ == "__main__":
    test_LSRPM()
