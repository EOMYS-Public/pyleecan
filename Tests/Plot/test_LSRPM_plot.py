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


from pyleecan.Classes.CondType12 import CondType12
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

    stator.winding = WindingUD(wind_mat=wind_mat_LSRPM*58, qs=3, p=4, Npcp=1,) #qs=6 (Stator + auxiliary)
    #Warning: if wind_mat is active, Ntcoil should be included in the matrix

    # Conductor setup
    stator.winding.conductor = CondType12(
        Nwppc=1,  # stator winding number of preformed wires (strands)
        # in parallel per coil along tangential (horizontal) direction
        Wwire=0.001,  # single wire width without insulation [m]
        Wins_cond=0.001,
        #Hwire=0.001,  # single wire height without insulation [m]
        Wins_wire=0,  # winding strand insulation thickness [m]
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
    rotor.bore = BoreLSRPM(N=8, Rarc=0.0375, alpha=22.5/180*pi)
    
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
    stator.winding.conductor.plot()


    # Set magnets in the rotor hole
    rotor.hole[0].magnet_0.mat_type = MagnetLSRPM

    rotor.hole[0].magnet_0.type_magnetization = 3 # Radial magnet

    #Ventilation holes
    Hold_round_shaft = load(join(DATA_DIR, "Machine", "Hold_round_shaft.json"))
    #Hold_round_shaft.plot()
    Screw_Hole = load(join(DATA_DIR, "Machine", "Screw_Hole.json"))
    #Screw_Hole.plot()
    rotor.axial_vent = [Hold_round_shaft, Screw_Hole]
 


    # matplotlib notebook
    LSRPM = MachineIPMSM(
        name="LSRPM LSEE", stator=stator, rotor=rotor, shaft=shaft, frame=None
    )

    LSRPM.save(join(DATA_DIR, "Machine", "LSRPM_004.json"))

    LSRPM.plot(is_show_fig=True, save_path=join(save_path, "test_LSRPM.png"))
    stator.plot(is_lam_only=True)
    Surface.plot
    plt.show()

if __name__ == "__main__":
    test_LSRPM()
