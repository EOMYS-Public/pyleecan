from pyleecan.Classes.Quantity import Quantity
from pyleecan.Classes.QuantityData import QuantityData
from pyleecan.Classes.QuantityScalar import QuantityScalar
from pyleecan.Classes.QuantityVectorField import QuantityVectorField
from pyleecan.Classes.QuantityMaker import QuantityMaker
from pyleecan.Classes.QuantityList import QuantityList


def test_quantityList():
    qty_list = QuantityList()
    qty_list.add_quantity("Id", "elec")
    qty_list.add_quantity(["Tem", "Tem_av"], "mag")

    phy_iterator = qty_list.get_physic_iter()
    assert phy_iterator.__next__() == qty_list.container["elec"]
    assert phy_iterator.__next__() == qty_list.container["mag"]
    try:
        phy_iterator.__next__()
        assert False
    except StopIteration:
        assert True

    qty_iterator = qty_list.get_quantity_iter()
    assert qty_iterator.__next__() == qty_list.container["elec"]["Id"]
    n = qty_iterator.__next__()
    assert n == qty_list.container["mag"]["Tem"]
    assert qty_iterator.__next__() == qty_list.container["mag"]["Tem_av"]
    try:
        phy_iterator.__next__()
        assert False
    except StopIteration:
        assert True


if __name__ == "__main__":
    test_quantityList()
