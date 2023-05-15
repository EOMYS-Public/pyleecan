from ...Classes.QuantityScalar import QuantityScalar
from ...Classes.QuantityData import QuantityData
from ...Classes.QuantityVectorField import QuantityVectorField


def MST__quantity_maker(**kwarg):
    return QuantityVectorField(
        symbol="MST",
        name="Airgap Maxwell Stress Tensor",
        physic="force",
        unit="N/m^2",
        unit_plot="N.m^2",
        getter="force.get_AGSF()",
        axes_name=["time", "angle", "z"],
        components=["rad", "circ", "ax"],
    )


def MST_rad__quantity_maker(**kwarg):
    return QuantityData(
        symbol="MST_rad",
        name="Airgap radial Maxwell Stress Tensor",
        physic="force",
        unit="N/m^2",
        unit_plot="N/m^2",
        getter="force.get_AGSF(component = 'radial')",
        axes_name=["time", "angle", "z"],
    )


def MST_circ__quantity_maker(**kwarg):
    return QuantityData(
        symbol="MST_circ",
        name="Airgap circumferential Maxwell Stress Tensor",
        physic="force",
        unit="N/m^2",
        unit_plot="N/m^2",
        getter="force.get_AGSF(component = 'tangential')",
        axes_name=["time", "angle", "z"],
    )


def MST_ax__quantity_maker(**kwarg):
    return QuantityData(
        symbol="MST_ax",
        name="Airgap axial Maxwell Stress Tensor",
        physic="force",
        unit="N/m^2",
        unit_plot="N/m^2",
        getter="force.get_AGSF(component = 'axial')",
        axes_name=["time", "angle", "z"],
    )
