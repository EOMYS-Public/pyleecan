import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM13 import SlotM13


rule_list = list()

# add equation rules

other_dict = {}
other_dict["[Dimensions]"] = {}
other_dict["[Dimensions]"]["Magnet_Thickness"] = 4
other_dict["[Dimensions]"]["Magnet_Arc_[ED]"] = 120
other_dict["[Dimensions]"]["Magnet_Reduction"] = 1


class Test_converter_mot(object):
    def test_surface_breadloaf_slotM13(self):
        """test rule complex"""
        machine = MachineSIPMSM()
        machine.rotor = LamSlotMag()
        machine.rotor.slot = SlotM13()

        machine.rotor.slot.H0 = 0.01
        machine.rotor.slot.H1 = 0.02

        rule = RuleComplex(fct_name="surface_breadloaf_slotM13", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / 8) * (pi / 180), "m": 0.001}
        )

        assert machine.rotor.slot.W0 == pytest.approx(0.5197086425658616)
        assert machine.rotor.slot.W1 == pytest.approx(0.5197086425658616)
        assert machine.rotor.slot.Rtopm == pytest.approx(0.9726990498218554)


if __name__ == "__main__":
    a = Test_converter_mot()
    a.test_surface_breadloaf_slotM13()
    print("Test Done")