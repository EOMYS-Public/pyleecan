
import pandas as pd

# import SciDataTool objects
from SciDataTool import Data1D, DataLinspace, DataPattern, DataTime, DataFreq, VectorField
# Load the machine
from os.path import join
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
import matplotlib.pyplot as plt

from pyleecan.Functions.Plot import dict_2D

from os.path import join

from numpy import ones, pi, array, linspace, cos, sqrt, zeros, exp
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from SciDataTool.Functions.Plot.plot_2D import plot_2D

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_PMSM import EEC_PMSM
from pyleecan.Classes.FluxLinkFEMM import FluxLinkFEMM
from pyleecan.Classes.IndMagFEMM import IndMagFEMM
#%run -m pip install plotly # Uncomment this line to install plotly
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode


@pytest.mark.skip(reason="Work in progress")
def test_LSRPM_simulation():
    # Create the Simulation

    LSRPM = load(join(DATA_DIR, "Machine", "LSRPM_004.json"))
    # LSRPM.plot()

    # Create a simultion
    simu_femm = Simu1(name="FEMM_simulation", machine=LSRPM)

    p = simu_femm.machine.stator.winding.p
    qs = simu_femm.machine.stator.winding.qs

    # Defining Simulation Input
    simu_femm.input = InputCurrent()

    # Rotor speed [rpm]
    simu_femm.input.OP = OPdq(N0=750)

    # # time discretization [s]
    time = linspace(
        start=0, stop=60 / simu_femm.input.OP.N0, num=32 * p, endpoint=False
    )  # 32*p timesteps
    simu_femm.input.time = time

    # # Angular discretization along the airgap circonference for flux density calculation
    simu_femm.input.angle = linspace(
        start=0, stop=2 * pi, num=2048, endpoint=False
    )  # 2048 steps

    # Stator currents as a function of time, each column correspond to one phase [A]
    I0_rms = 6.85
    felec = p * simu_femm.input.OP.N0 / 60  # [Hz]
    rot_dir = simu_femm.machine.stator.comp_mmf_dir()
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    # Phi0 = 0  # Maximum Torque Per Amp

    # Ia = (

    #     I0_rms
    #     * sqrt(2)
    #     * cos(2 * pi * felec * time + 0 * rot_dir * 2 * pi / qs + Phi0)
    # )
    # Ib = (
    #     I0_rms
    #     * sqrt(2)
    #     * cos(2 * pi * felec * time + 1 * rot_dir * 2 * pi / qs + Phi0)
    # )
    # Ic = (
    #     I0_rms
    #     * sqrt(2)
    #     * cos(2 * pi * felec * time + 2 * rot_dir * 2 * pi / qs + Phi0)
    # )
    #Auxiliary
    # Id = zeros(time.shape)
    # Ie = zeros(time.shape)
    # If = zeros(time.shape)
    # simu_femm.input.Is = array([Ia, Ib, Ic, Id, Ie, If]).transpose()
    # simu_femm.input.Is = array([Ia, Ib, Ic]).transpose()

    FEMM_dict = dict()
    # rotor yoke region mesh and segments max element size parameter
    FEMM_dict["meshsize_yokeR"] = 0.005
    FEMM_dict["elementsize_yokeR"] = 0.005

    FEMM_dict["elementsize_slotR"] = 0.0001
    FEMM_dict["elementsize_slotS"] = 0.0005
    # FEMM_dict["arcspan"] = 5  # max span of arc element in degrees

    # airgap region mesh and segments max element size parameter    
    FEMM_dict["meshsize_airgap"] = 0.0001
    FEMM_dict["elementsize_airgap"] = 0.0001

    simu_femm.mag = MagFEMM(
        type_BH_stator=0,  # 0 to use the material B(H) curve,
        # 1 to use linear B(H) curve according to mur_lin,
        # 2 to enforce infinite permeability (mur_lin =100000)
        type_BH_rotor=0,  # 0 to use the material B(H) curve,
        # 1 to use linear B(H) curve according to mur_lin,
        # 2 to enforce infinite permeability (mur_lin =100000)
        file_name="",  # Name of the file to save the FEMM model
        FEMM_dict_enforced=FEMM_dict,
    )

    # Definition of a sinusoidal current
 
    #I0, Phi0 to set
    I0_rms =0# Maximum current [Arms]
    Phi0 = pi  # MATP 
    # Compute corresponding Id/Iq
    Id_ref = (I0_rms*exp(1j*(Phi0))).real
    Iq_ref = (I0_rms*exp(1j*(Phi0))).imag
 

    # Setting the values
    simu_femm.input.Id_ref = Id_ref # [Arms]
    simu_femm.input.Iq_ref = Iq_ref # [Arms]

    # setting I0_rms and Phi0 directly in simulation
    # simu_op.input.set_Id_Iq(I0=I0_rms, Phi0=Phi0)
    # print("Id: "+str(simu_op.input.Id_ref))
    # print("Iq: "+str(simu_op.input.Iq_ref))

    print(Id_ref,Iq_ref)

    # simu_femm.input.Nt_tot = 128*3 # Number of time step
    # simu_femm.input.Na_tot = 2048 # Spatial discretization
    simu_femm.input.N0 = 750 # Rotor speed [rpm]

    # Only the magnetic module is defined
    # simu_femm.elec = None
    simu_femm.force = None
    simu_femm.struct = None
    simu_femm.mag.is_periodicity_a = False
    simu_femm.mag.is_periodicity_t = True
    simu_femm.mag.nb_worker = (
        16  # Number of FEMM instances to run at the same time (1 by default)
    )
    simu_femm.mag.is_get_meshsolution = (
        True  # To get FEA mesh for latter post-procesing
    )
    simu_femm.mag.is_save_meshsolution_as_file = (
        False  # To save FEA results in a dat file
    )

    #ref flux2D 

    B_flux = pd.read_excel (r'D:/StageSijie/LSRPM/B_675_V2.xls')
    B_radial=pd.DataFrame(B_flux, columns= ['Magnetic flux density / Normal component'])
    Ang_ref=linspace(0,2*pi, B_radial.size)
    Angle_ref = DataLinspace(
    name="angle",
    unit="rad",
    initial=0,
    final=2*pi,
    include_endpoint=True,
    number=B_radial.size
    )
    B_radial = DataTime(name="Airgap radial flux density", symbol="Br", unit="T", axes=[Angle_ref], values=B_radial.values)
    B_radial.plot_2D_Data("angle{°}")

    B_tange=pd.DataFrame(B_flux, columns= ['Magnetic flux density / Tangential component'])
    B_tange = DataTime(name="Airgap radial flux density", symbol="Br", unit="T", axes=[Angle_ref], values=B_tange.values*-1)

    out_femm = simu_femm.run()


    # Radial magnetic flux


    out_femm.mag.B.plot_2D_Data("angle", "time[0]",component_list=["radial"])
    B_radial.plot_2D_Data("angle")
    
    out_femm.mag.B.plot_2D_Data("wavenumber=[0,76]", "time[0]", component_list=["radial"])
    B_radial_pyleecan=out_femm.mag.B.components['radial']
    B_radial_pyleecan.plot_2D_Data("angle{°}",data_list=[B_radial],legend_list=["Pyleecan", "Flux2D"] )
    # Tangential magnetic flux
    out_femm.mag.B.plot_2D_Data("angle{°}","time[0]",component_list=["tangential"])
    out_femm.mag.B.plot_2D_Data("wavenumber=[0,76]","time[0]",component_list=["tangential"])
    B_tange_pyleecan=out_femm.mag.B.components['tangential']
    B_tange_pyleecan.plot_2D_Data("angle{°}",data_list=[B_tange],legend_list=["Pyleecan", "Flux2D"] )

    # print(out_femm.mag.Tem.values.shape)
    # print(simu_femm.input.Nt_tot)

    # out_femm.mag.meshsolution.plot_contour(label="B", group_names=["stator core","rotor core"])
    # out_femm.mag.meshsolution.plot_contour(label="B", group_names="rotor core")
    # out_femm.elec.get_Is().plot_2D_Data("time", "phase", **dict_2D)
    # print(out_femm.simu.machine.stator.comp_resistance_wind())


    #########################################################################################
    ## Several Operating Point
#     Tem_av_ref = array([79, 125, 160, 192, 237, 281, 319, 343, 353, 332, 266, 164, 22]) # Yang et al, 2013 (reference)
#     Phi0_ref = linspace(60 * pi / 180, 180 * pi / 180, Tem_av_ref.size)
#     N_simu = Tem_av_ref.size

#     varload = VarLoadCurrent(is_torque=True)
#     varload.type_OP_matrix = 0 # Matrix N0, I0, Phi0,  (N0, Id, Iq) if type_OP_matrix==1

#     # Creating the Operating point matrix
#     OP_matrix = zeros((N_simu,4))

#     # Set N0 = 2000 [rpm] for all simulation
#     OP_matrix[:,0] = 2000 * ones((N_simu))

#     # Set I0 = 250 / sqrt(2) [A] (RMS) for all simulation
#     OP_matrix[:,1] = I0_rms * ones((N_simu))

#     # Set Phi0 from 60? to 180?
#     OP_matrix[:,2] = Phi0_ref

#     # Set reference torque from Yang et al, 2013
#     OP_matrix[:,3] = Tem_av_ref

#     varload.OP_matrix = OP_matrix
#     print(OP_matrix)

#     # All the simulation use the same machine
#     # No need to draw the machine for all OP
#     varload.is_reuse_femm_file=True

#     simu_vop = simu_femm.copy()
#     simu_vop.var_simu = varload

#     # Speed-up computation (set reference simu as first OP)
#     simu_vop.input.set_OP_from_array(varload.OP_matrix, varload.type_OP_matrix)

#     Xout = simu_vop.run()

#     print("Values available in XOutput:")
#     print(Xout.xoutput_dict.keys())

#     print("\nI0 for each simulation:")
#     print(Xout["I0"].result)
#     print("\nPhi0 for each simulation:")
#     print(Xout["Phi0"].result)

#     fig = Xout.plot_multi("Phi0", "Tem_av")
#     fig = Xout.plot_multi("Id", "Iq")
#     plot_2D(
#     array([x*180/pi for x in Xout.xoutput_dict["Phi0"].result]),
#     [Xout.xoutput_dict["Tem_av"].result, Xout.xoutput_dict["Tem_av_ref"].result],
#     legend_list=["Pyleecan", "Yang et al, 2013"],
#     xlabel="Current angle [?]",
#     ylabel="Electrical torque [N.m]",
#     title="Electrical torque vs current angle",
#     **dict_2D
# )

    #########################################################################################
    ##Electrical module
    #Definition of the magnetic simulation (FEMM with symmetry and sliding band)
    # simu_femm.elec = Electrical(
    # eec=EEC_PMSM(
    #     indmag=IndMagFEMM(is_periodicity_a=None, Nt_tot=50),
    #     fluxlink=FluxLinkFEMM(is_periodicity_a=None, Nt_tot=50),
    #     )
    # )
    # # Run only Electrical module

    # simu_femm.force = None
    # simu_femm.struct = None

    # out = simu_femm.run()
    # out.elec.Us.plot_2D_Data("time", "phase", **dict_2D)
    # print("Ld: "+str(out.elec.Ld))
    # print("Lq: "+str(out.elec.Lq))

    # print("Ud: "+str(out.elec.Ud_ref))
    # print("Uq: "+str(out.elec.Uq_ref))
    # print("Tem: "+str(out.elec.Tem_av_ref))

    plt.show()

if __name__ == "__main__":
    test_LSRPM_simulation()
