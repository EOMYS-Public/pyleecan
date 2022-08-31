# -*- coding: utf-8 -*-

from pyleecan.Methods.Machine.Lamination.build_geometry import build_geometry
from pyleecan.Functions.load import load
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.OPdq import OPdq

# Testing cases file paths
# file_path = "C:/Users/pc/Downloads/SPMSM_val.json"
file_path = "C:/Users/pc/Downloads/SPMSM_val_H0_isth.json"
# file_path = "C:/Users/pc/Downloads/SPMSM_val_isth.json"
machine = load(file_path)

# Machine get_lam_list method
machine.stator.build_geometry_polar(sym=1)

# Verify one surface
# surf = machine.stator.build_geometry_polar()[0]
# fig, ax = surf.plot()

# Plot the stator yoke
surf_list = machine.stator.build_geometry_polar(sym=12)
fig, ax = surf_list[0].plot(is_disp_point_ref=True)
for surf in surf_list:
    surf.plot(fig=fig, ax=ax, is_disp_point_ref=True)

# Simulation using FEMM
simu = Simu1(name="test_FEMM", machine=machine)

simu.input = InputCurrent(
    OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
    Na_tot=60 * 4,
    Nt_tot=1,
    # Periodicity
    is_periodicity_t=False,
    is_periodicity_a=True,
    angle_rotor_initial=0.000001,
)

simu.mag = MagFEMM(
    is_periodicity_a=True,
    is_periodicity_t=False,
    nb_worker=4,  # number of FEMM windows to be opened
    is_get_meshsolution=True,  # Get the mesh solution
    is_fast_draw=True,
    is_calc_torque_energy=False,
    Kmesh_fineness=2,  # Define the mesh fineness
    is_polar_geo=True,
)

out = simu.run()

pass