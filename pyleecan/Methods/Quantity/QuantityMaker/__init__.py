# name, physic, getter, unit, type(scalar, D, VF), unit_plot?, axes?, components?

qty_dict = {  # name, physic, getter, unit
    "Is": ["Stator phase current", "elec", "elec.get_Is", "Arms"],  # unit
    "Id": ["Stator phase current along d-axis", "elec", "", "SI"],  # unit
    "Iq": ["Stator phase current along q-axis", "elec", "", "SI"],  # unit
    "If": ["Rotor current", "elec", "", "SI"],  # unit
    "J_rms": ["Current density", "elec", "", "MA/mm^2"],
    "Tem_av_ref": ["Rotor electromagnetic torque", "elec", "", "SI"],  # unit
    "U0": ["Voltage", "elec", "", "SI"],  # unit
    "slip": ["Slip", "elec", "", "SI"],  # unit
    "s.f_e": ["Slip frequency", "elec", "", "SI"],  # unit
    "U0/f_e": ["Voltage frequency", "elec", "", "SI"],  # unit
    "EEC_param": ["EEC parameter", "elec", "get_eec_data", "SI"],  # unit
    "Per": ["Airgap permeance", "mag", "mag.get_Per", "H/m^2"],
    "MMF": ["Airgap magnetomotive force", "mag", "mag.get_MMF", "SI"],  # name
    "B": ["Airgap flux density", "mag", "mag.get_B", "T"],
    "Tem": [
        "Rotor electromagnetic torque",
        "mag",
        "mag.get_Tem",
        "N.m",
    ],  # unit + symbol
    "Tem_av": ["Average electromagnetic torque", "mag", "", "N.m"],  # name + getter
    "Tem_rip_norm": ["Electromagnetic torque ripple", "mag", "", ""],  # name + getter
    "Tem_rip_pp": [
        "Peak to Peak Torque ripple",
        "mag",
        "mag.get_Tem",
        "N.m",
    ],  # name + getter
    "Phi_wind_stator": [
        "Stator winding flux",
        "mag",
        "mag.get_Phi_wind_stator",
        "Wb/m",
    ],  # unit
    "emf": ["Stator electromotive force", "mag", "mag.get_emf", "SI"],  # unit
    "ecc": ["Rotor eccentricity", "mag", "", "SI"],  # unit
    "uag": ["Uneven Airgap", "mag", "", "SI"],  # unit
    "skew": ["Rotor skew", "mag", "SI"],  # unit
    "MST": ["Airgap Maxwell Stress Tensor", "force", "force.get_AGSF", "N/m^2"],  # name
    "AGSF": [
        "Airgap Maxwell Stress Tensor",
        "force",
        "force.get_AGSF",
        "N/m^2",
    ],  # name, unit
    "LF": [
        "Stator tooth Lumped Force",
        "force",
        "force.get_LF_integrated",
        "N",
    ],
    "UMP": [
        "Unbalance Magnetic Pull",
        "force",
        "force.get_UMP",
        "N",
    ],
    "OLC": ["Stator tooth Lumped Force", "force", "force.get_LF_LC", "dB"],  # unit
    "WFRFv": [
        "Vibration Frequency Response Function",
        "struct",
        "struct.get_WFRFv_rms",
        "SI",
    ],  # unit
    "WFRFv_modal_proj": [
        "Modal Unit Force",
        "struct",
        "struct.get_WFRFv_modal_proj",
        "SI",
    ],  # unit
    "WFRFv_modal_cont": [
        "Unit load case contribution on structural modes",
        "struct",
        "struct.get_WFRFv_modal_cont",
        "SI",
    ],  # unit
    "U_rms": ["Vibration displacement", "struct", "struct.get_U_rms", "m"],  # symbol
    "V_rms": ["Vibration velocity", "struct", "struct.get_V_rms", "m/s"],  # symbol
    "A_rms": [
        "Vibration acceleration",
        "struct",
        "struct.get_A_rms",
        "m/s^2",
    ],  # symbol
    "W": ["Sound Power Level", "acoustic", "acoustic.get_W", "W"],  # name
    "p": ["Sound Pressure Level", "acoustic", "acoustic.get_p", "Pa"],  # name
    "loudness_zwst": [
        "Loudness (Zwicker method for stationary signal)",
        "out_wave",
        "out_wave.get_loudness_zwst",
        "SI",
    ],  # unit
    "specific_loudness_zwst": [
        "Specific loudness (Zwicker method for stationary signal)",
        "out_wave",
        "out_wave.get_specific_loudness_zwst",
        "SI",
    ],  # unit
    "sharpness_din": [
        "Sharpness (DIN 45692)",
        "out_wave",
        "out_wave.get_sharpness_din",
        "SI",
    ],  # unit
    "roughness_dw": [
        "Roughness (Daniel & Weber method)",
        "out_wave",
        "out_wave.get_roughness_dw",
        "SI",
    ],  # unit
    "specific_roughness_dw": [
        "Specific roughness (Daniel & Weber method)",
        "out_wave",
        "out_wave.get_specific_roughness_dw",
        "SI",
    ],  # unit
    "WFRFa": [
        "Acoustic Frequency Response Function",
        "acoustic",
        "acoustic.get_WFRFa_rms",
        "SI",
    ],  # unit
}


qty_dict = {  # Name, getter, getter_arg_dict, unit
    "U_{rms}": ["Vibration displacement", "struct.get_U_rms", "dict()", "m"],  # Idem
    "V_{rms}": ["Vibration velocity", "struct.get_V_rms", "dict()", "m/s"],  # Idem
    "A_{rms}": [
        "Vibration acceleration",
        "struct.get_A_rms",
        "dict()",
        "m/s^2",
    ],  # Idem
    "W": ["A-weighted Sound Power Level", "acoustic.get_W", "dict()", "W"],  # name
    "p": ["A-weighted Sound Pressure Level", "acoustic.get_p", "dict()", "Pa"],  # name
}
