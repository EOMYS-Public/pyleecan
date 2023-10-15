# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from numpy import pi
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM15 import SlotM15
from pyleecan.GUI.Dialog.DMachineSetup.SMSlot.PMSlot15.PMSlot15 import PMSlot15
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import LIB_KEY, MACH_KEY


import pytest


class TestPMSlot15(object):
    """Test that the widget PMSlot15 behave like it should"""

    def setup_method(self):
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotM15(H0=0.10, W0=0.13, Wmag=0.14, Hmag=0.15, Rtopm=0.16)

        material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        material_dict[LIB_KEY] = [
            Material(name="test1"),
            Material(name="test2"),
            Material(name="test3"),
        ]
        material_dict[LIB_KEY][0].elec.rho = 0.31
        material_dict[LIB_KEY][1].elec.rho = 0.32
        material_dict[LIB_KEY][2].elec.rho = 0.33

        self.material_dict = material_dict

        self.widget = PMSlot15(self.test_obj, self.material_dict)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPMSlot15")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_Hmag.value() == 0.15
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_Wmag.value() == 0.14
        assert self.widget.lf_Rtopm.value() == 0.16

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        # Check Unit
        assert self.widget.unit_W0.text() == "[rad]"
        # Change value in GUI
        self.widget.lf_W0.clear()
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W0 == 0.31
        assert self.test_obj.slot.W0 == 0.31

    def test_set_Wmag(self):
        """Check that the Widget allow to update Wmag"""
        # Check Unit
        assert self.widget.unit_Wmag.text() == "[m]"
        # Change value in GUI
        self.widget.lf_Wmag.clear()
        QTest.keyClicks(self.widget.lf_Wmag, "0.33")
        self.widget.lf_Wmag.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.Wmag == 0.33
        assert self.test_obj.slot.Wmag == 0.33

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        # Check Unit
        assert self.widget.unit_H0.text() == "[m]"
        # Change value in GUI
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H0 == 0.34
        assert self.test_obj.slot.H0 == 0.34

    def test_set_Hmag(self):
        """Check that the Widget allow to update Hmag"""
        # Check Unit
        assert self.widget.unit_Hmag.text() == "[m]"
        # Change value in GUI
        self.widget.lf_Hmag.clear()
        QTest.keyClicks(self.widget.lf_Hmag, "0.36")
        self.widget.lf_Hmag.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.Hmag == pytest.approx(0.36)
        assert self.test_obj.slot.Hmag == pytest.approx(0.36)

    def test_set_Rtopm(self):
        """Check that the Widget allow to update Rtopm"""
        # Check Unit
        assert self.widget.unit_Rtopm.text() == "[m]"
        # Change value in GUI
        self.widget.lf_Rtopm.clear()
        QTest.keyClicks(self.widget.lf_Rtopm, "0.34")
        self.widget.lf_Rtopm.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.Rtopm == 0.34
        assert self.test_obj.slot.Rtopm == 0.34

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj.slot = SlotM15(
            H0=0.005, Hmag=0.005, W0=0.01, Wmag=0.01, Rtopm=0.02
        )
        self.widget = PMSlot15(self.test_obj, self.material_dict)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.005 [m]"

    def test_check(self):
        """Check that the check is working correctly"""
        self.test_obj = LamSlotMag(Rint=0.1, Rext=0.2)
        # H0
        self.test_obj.slot = SlotM15(H0=None, Hmag=0.10, W0=0.10, Wmag=0.10, Rtopm=0.1)
        self.widget = PMSlot15(self.test_obj, self.material_dict)
        assert self.widget.check(self.test_obj) == "You must set H0 !"
        # Hmag
        self.test_obj.slot = SlotM15(H0=0.10, Hmag=None, W0=0.10, Wmag=0.10, Rtopm=0.1)
        assert self.widget.check(self.test_obj) == "You must set Hmag !"
        # W0
        self.test_obj.slot = SlotM15(H0=0.10, Hmag=0.10, W0=None, Wmag=0.10, Rtopm=0.1)
        assert self.widget.check(self.test_obj) == "You must set W0 !"
        # Wmag
        self.test_obj.slot = SlotM15(H0=0.10, Hmag=0.10, W0=0.10, Wmag=None, Rtopm=0.1)
        assert self.widget.check(self.test_obj) == "You must set Wmag !"
        # Rtopm
        self.test_obj.slot = SlotM15(H0=0.10, Hmag=0.10, W0=0.10, Wmag=0.1, Rtopm=None)
        assert self.widget.check(self.test_obj) == "You must set Rtopm !"

    def test_set_material(self):
        """Check that you can change the material"""
        self.widget.w_mag.w_mat.c_mat_type.setCurrentIndex(0)
        assert self.test_obj.magnet.mat_type.name == "test1"
        assert self.test_obj.magnet.mat_type.elec.rho == 0.31
        self.widget.w_mag.w_mat.c_mat_type.setCurrentIndex(2)
        assert self.test_obj.magnet.mat_type.name == "test3"
        assert self.test_obj.magnet.mat_type.elec.rho == 0.33

    def test_set_type_magnetization(self):
        """Check that you can change tha magnetization"""
        # type_magnetization set test
        self.widget.w_mag.c_type_magnetization.setCurrentIndex(2)
        assert self.test_obj.magnet.type_magnetization == 2
        self.widget.w_mag.c_type_magnetization.setCurrentIndex(0)
        assert self.test_obj.magnet.type_magnetization == 0


if __name__ == "__main__":
    a = TestPMSlot15()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.teardown_class()
    print("Done")
