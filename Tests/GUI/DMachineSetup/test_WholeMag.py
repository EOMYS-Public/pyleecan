# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.MachineSyRM import MachineSyRM
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.HoleM51 import HoleM51
from pyleecan.Classes.HoleM52 import HoleM52
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.HoleM54 import HoleM54
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.Classes.HoleM58 import HoleM58
from pyleecan.GUI.Dialog.DMatLib.MatLib import MatLib
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.SMHoleMag import SMHoleMag
from pyleecan.GUI.Dialog.DMachineSetup.SMHoleMag.WHoleMag import WHoleMag
from pyleecan.Classes.Material import Material


import pytest


@pytest.mark.GUI
class Test_WholeMag(object):
    """Test that the widget SMHoleMag behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = MachineIPMSM(type_machine=8)
        self.test_obj.stator = LamSlotWind()
        self.test_obj.stator.winding.p = 4
        self.test_obj.rotor = LamHole(Rint=0.1, Rext=0.2)
        self.test_obj.rotor.hole = list()
        self.test_obj.rotor.hole.append(HoleM50(Zh=8, W1=0.003, W0=0.050, H2=0.01, H3=0.02))
        self.test_obj.rotor.hole[0].magnet_0.mat_type.name = "Magnet3"

        self.matlib = MatLib()
        self.matlib.list_mat = [
            Material(name="Magnet1"),
            Material(name="Magnet2"),
            Material(name="Magnet3"),
        ]
        self.matlib.index_first_mat_mach = 3

        self.widget = SMHoleMag(
            machine=self.test_obj, matlib=self.matlib, is_stator=False
        )

        self.tab = WHoleMag.WHoleMag(parent = self.widget, is_mag=True, index=0, matlib=self.matlib)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test SWSlot")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_WholeMag_check(self):
        self.tab.emit_save()
        assert None == self.tab.check()
        