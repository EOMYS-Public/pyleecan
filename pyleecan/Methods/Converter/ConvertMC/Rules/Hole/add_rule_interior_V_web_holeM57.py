from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_interior_V_web_holeM57(self, is_stator, hole_id):
    """Create and adapt all the rules related to Hole
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    hole_id : int
        A int to know the number of hole
    """

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"BridgeThickness_Array[{hole_id}]"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].H1",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"BridgeThickness_Array[{hole_id}]"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].H2",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"PoleVAngle_Array[{hole_id}]"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].W0",
            unit_type="rad",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"MagnetPost_Array[{hole_id}]"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].1",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"MagnetVWidth_Array[{hole_id}]"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].W2",
            unit_type="rad",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"WebThickness_Array[{hole_id}]"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].W3",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"MagnetBarWidth_Array[{hole_id}]"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].W4",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )