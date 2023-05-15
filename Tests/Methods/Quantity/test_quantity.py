from pyleecan.Classes.Quantity import Quantity
from pyleecan.Classes.QuantityData import QuantityData
from pyleecan.Classes.QuantityScalar import QuantityScalar
from pyleecan.Classes.QuantityVectorField import QuantityVectorField
from pyleecan.Classes.QuantityMaker import QuantityMaker


def test_quantityScalar():
    qty = QuantityMaker()
    qty = qty.create_quantity("Id", "elec")
    qty_ref = QuantityScalar(
        symbol="Id",
        name="Stator phase current along d-axis",
        physic="elec",
        unit="Arms",
        unit_plot="Arms",
        getter="elec.OP.get_Id_Iq()['Id']",
    )

    assert qty == qty_ref


def test_quantityData():
    qty_ref = QuantityData(
        symbol="MST_rad",
        name="Airgap radial Maxwell Stress Tensor",
        physic="force",
        unit="N/m^2",
        unit_plot="N/m^2",
        getter="force.get_AGSF(component = 'radial')",
        axes_name=["time", "angle", "z"],
    )

    qty = QuantityMaker().create_quantity("MST_rad", "force")
    assert qty == qty_ref


def test_quantityVectorField():
    qty_ref = QuantityVectorField(
        symbol="B",
        name="Airgap flux density",
        physic="mag",
        unit="T",
        unit_plot="T",
        getter="mag.get_B()",
        axes_name=["time", "angle", "z"],
        components=["rad", "circ", "ax"],
    )

    qty = QuantityMaker().create_quantity("B", "mag")
    qty_rad = QuantityMaker().create_quantity("B_rad", "mag")
    assert qty == qty_ref
    assert qty_rad == qty.get_component_quantity("rad")


if __name__ == "__main__":
    test_quantityScalar()
    test_quantityData()
    test_quantityVectorField()
