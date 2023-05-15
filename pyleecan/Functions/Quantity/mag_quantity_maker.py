from ...Classes.QuantityScalar import QuantityScalar
from ...Classes.QuantityData import QuantityData
from ...Classes.QuantityVectorField import QuantityVectorField


def B__quantity_maker(**kwarg):
    return QuantityVectorField(
        symbol="B",
        name="Airgap flux density",
        physic="mag",
        unit="T",
        unit_plot="T",
        getter="mag.get_B()",
        axes=["time", "angle", "z"],
        components=["rad", "circ", "ax"],
    )


def B_rad__quantity_maker(**kwarg):
    return QuantityData(
        symbol="B_rad",
        name="Airgap radial flux density",
        physic="mag",
        unit="T",
        unit_plot="T",
        getter="mag.get_B(component = 'radial')",
        axes=["time", "angle", "z"],
    )


def B_circ__quantity_maker(**kwarg):
    return QuantityData(
        symbol="B_circ",
        name="Airgap circumferential flux density",
        physic="mag",
        unit="T",
        unit_plot="T",
        getter="mag.get_B(component = 'tangential')",
        axes=["time", "angle", "z"],
    )


def B_ax__quantity_maker(**kwarg):
    return QuantityData(
        symbol="B_ax",
        name="Airgap axial flux density",
        physic="mag",
        unit="T",
        unit_plot="T",
        getter="mag.get_B(component = 'axial')",
        axes=["time", "angle", "z"],
    )


def Tem__quantity_maker(**kwarg):
    return QuantityData(
        symbol="Tem",
        name="Rotor electromagnetic torque",
        physic="mag",
        unit="N.m",
        unit_plot="N.m",
        getter="mag.get_Tem()",
        axes=["time"],
    )


def Tem_av__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Tem_av",
        name="Average electromagnetic torque",
        physic="mag",
        unit="N.m",
        unit_plot="N.m",
        getter="mag.Tem_av",
    )


def Tem_rip_norm__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Tem_rip_norm",
        name="Peak to Peak Torque ripple normalized",
        physic="mag",
        unit="",
        unit_plot="",
        getter="mag.Tem_rip_norm",
    )


def Tem_rip_pp__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Tem_rip_pp",
        name="Peak to Peak Torque ripple",
        physic="mag",
        unit="N.m",
        unit_plot="N.m",
        getter="mag.Tem_rip_pp",
    )


def Phi_wind_stator__quantity_maker(**kwarg):
    return QuantityData(
        symbol="Phi_wind_stator",
        name="Stator winding flux",
        physic="mag",
        unit="Wb/m",
        unit_plot="Wb/m",
        getter="mag.get_Phi_wind_stator()",
        axes=["time", "phase"],
    )
