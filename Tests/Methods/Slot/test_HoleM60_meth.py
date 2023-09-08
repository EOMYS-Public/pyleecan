# -*- coding: utf-8 -*-

from numpy import pi, angle
import matplotlib.pyplot as plt
import pytest
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM60 import HoleM60
from pyleecan.Functions.Geometry.inter_line_line import inter_line_line
HoleM60_test = list()
test_obj = LamHole(is_internal=True, Rint=0.021, Rext=0.75, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM60(
        Zh=4,
        W0=pi * 0.8,
        W1=10e-3,
        W2=10e-2,
        W3=5e-3,
        H0=3e-3,
        H1=5e-3,
    )
)
HoleM60_test.append(
    {
        "test_obj": test_obj,
    }
)

# For AlmostEqual
DELTA = 1e-4


class Test_HoleM60_meth(object):
    """Test machine plot hole 60"""

    @pytest.mark.parametrize("test_dict", HoleM60_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.hole[0]._comp_point_coordinate()
        print("Z sec=", point_dict["Z"])
        print("Z0=", point_dict["Z0"])
        test_obj.plot()
        test_obj.hole[0].plot()
        plt.show()
        for i in range(1, 7):
            print("Z%d=" % (i), point_dict["Z%d" % i])
            print("Z%ds=" % (i), point_dict["Z%ds" % i])
                    
        # Check width
        assert abs(point_dict["Z2"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].W2 - test_obj.hole[0].H0
        )
        assert abs(point_dict["Z1s"] - point_dict["Z2s"]) == pytest.approx(
            test_obj.hole[0].W2 - test_obj.hole[0].H0
        )
        assert abs(point_dict["Z5"] - point_dict["Z4"]) == pytest.approx(
            test_obj.hole[0].W2 - test_obj.hole[0].H0
        )
        assert abs(point_dict["Z5s"] - point_dict["Z4s"]) == pytest.approx(
            test_obj.hole[0].W2 - test_obj.hole[0].H0
        )
        assert point_dict["Z1"].imag == pytest.approx(
            test_obj.hole[0].W3/2
        )
        assert abs(point_dict["Z1s"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].W3
        )
        assert abs(point_dict["Z3"] - point_dict["Z6"]) == pytest.approx(
            test_obj.hole[0].W2
        )
        assert abs(point_dict["Z3s"] - point_dict["Z6s"]) == pytest.approx(
            test_obj.hole[0].W2
        )
        
        # Check height
        assert abs(point_dict["Z4"] - point_dict["Z2"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["Z4s"] - point_dict["Z2s"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["Z5"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["Z5s"] - point_dict["Z1s"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        
        assert abs(point_dict["Z3"]) == pytest.approx(
            test_obj.hole[0].get_Rbo() - test_obj.hole[0].H1
        )
        
        # Compute P
        Z = inter_line_line(point_dict["Z3"], point_dict["Z6"], point_dict["Z3s"], point_dict["Z6s"])[0]
        assert abs(point_dict["Z"]) == pytest.approx(
            abs(Z)
        )
        
        assert angle(point_dict["Z6"] - Z) == pytest.approx(
            test_obj.hole[0].W0 / 2
        )
        assert angle(point_dict["Z3"] - Z) == pytest.approx(
            test_obj.hole[0].W0 / 2
        )
        assert angle(point_dict["Z6s"] - Z) == pytest.approx(
            - test_obj.hole[0].W0 / 2
        )
        assert angle(point_dict["Z3s"] - Z) == pytest.approx(
            - test_obj.hole[0].W0 / 2
        )
        
        # Magnets dimensions
        assert abs(point_dict["ZM1"] - point_dict["ZM2"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        assert abs(point_dict["ZM3"] - point_dict["ZM4"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        assert abs(point_dict["ZM1s"] - point_dict["ZM2s"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        assert abs(point_dict["ZM3s"] - point_dict["ZM4s"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        
        assert abs(point_dict["ZM1"] - point_dict["ZM4"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["ZM3"] - point_dict["ZM2"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["ZM1s"] - point_dict["ZM4s"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["ZM3s"] - point_dict["ZM2s"]) == pytest.approx(
            test_obj.hole[0].H0
        )

if __name__ == "__main__":
    a = Test_HoleM60_meth()
    for test_dict in HoleM60_test:
        a.test_schematics(test_dict)
    print("Done")