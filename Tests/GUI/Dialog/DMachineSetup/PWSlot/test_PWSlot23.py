# -*- coding: utf-8 -*-

import sys

import pytest
from numpy import pi
from PySide2 import QtWidgets
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt, QPoint
from pyleecan.Classes.Material import Material
from pyleecan.GUI.Dialog.DMatLib.DMatLib import MACH_KEY, LIB_KEY
from Tests.GUI import gui_option  # Set unit as [m]
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.PWSlot23.PWSlot23 import PWSlot23


class TestPWSlot23(object):
    """Test that the widget PWSlot23 behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestPWSlot23")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def setup_method(self):
        """Run at the begining of every test to setup the gui"""
        self.material_dict = {LIB_KEY: list(), MACH_KEY: list()}
        self.mat1 = Material(name="Mat1")
        self.mat2 = Material(name="Mat2")
        self.mat3 = Material(name="M400-50A")
        self.mat4 = Material(name="Mat4")
        self.material_dict[LIB_KEY] = [
            self.mat1,
            self.mat2,
            self.mat3,
        ]
        self.material_dict[MACH_KEY] = [
            self.mat4,
        ]
        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2, mat_type=self.mat3)
        self.test_obj.slot = SlotW23(
            H0=0.10, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, H1_is_rad=False
        )
        self.test_obj.slot.W3 = None
        self.widget = PWSlot23(self.test_obj, self.material_dict)

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        assert self.widget.lf_H0.value() == 0.10
        assert self.widget.lf_H1.value() == 0.11
        assert self.widget.lf_H2.value() == 0.12
        assert self.widget.lf_W0.value() == 0.13
        assert self.widget.lf_W1.value() == 0.14
        assert self.widget.lf_W2.value() == 0.15
        assert not self.widget.g_wedge.isChecked()

        self.test_obj.slot = SlotW23(
            H0=0.20,
            H1=0.21,
            H2=0.22,
            W0=0.23,
            W1=0.24,
            W2=0.25,
            H1_is_rad=True,
            wedge_mat=self.mat1,
        )
        self.test_obj.slot.W3 = None
        self.widget = PWSlot23(self.test_obj, self.material_dict)
        assert self.widget.lf_H0.value() == 0.20
        assert self.widget.lf_H1.value() == 0.21
        assert self.widget.lf_H2.value() == 0.22
        assert self.widget.lf_W0.value() == 0.23
        assert self.widget.lf_W1.value() == 0.24
        assert self.widget.lf_W2.value() == 0.25
        assert self.widget.g_wedge.isChecked()
        assert self.widget.w_wedge_mat.c_mat_type.count() == 4
        assert self.widget.w_wedge_mat.c_mat_type.currentText() == "Mat1"
        # Index 1 is rad
        # self.assertEqual(self.widget.c_H1_unit.currentIndex(),1)

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        self.widget.lf_W0.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W0 == 0.31
        assert self.test_obj.slot.W0 == 0.31

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, "0.32")
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W1 == 0.32
        assert self.test_obj.slot.W1 == 0.32

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()
        QTest.keyClicks(self.widget.lf_W2, "0.33")
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W2 == 0.33
        assert self.test_obj.slot.W2 == 0.33

    def test_set_W3(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W3.setEnabled(True)

        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.99")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.W3 == 0.99
        assert self.test_obj.slot.W3 == 0.99

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H0 == 0.34
        assert self.test_obj.slot.H0 == 0.34

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot
        msg = str(self.widget.slot.H1)
        assert self.widget.slot.H1 == 0.35, msg
        assert self.test_obj.slot.H1 == 0.35

        self.widget.c_H1_unit.setCurrentIndex(2)
        assert str(self.widget.c_H1_unit.currentText()) == "[°]"

        self.widget.lf_H1.clear()  # Clear the field before writing
        value = 1.4
        QTest.keyClicks(self.widget.lf_H1, str(value))
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H1 == value / 180 * pi

    def test_set_H1_is_rad(self):
        """Check that the Widget allow to update H1_is_rad"""
        assert not self.test_obj.slot.H1_is_rad
        self.widget.c_H1_unit.setCurrentIndex(1)  # Index 1 is rad
        assert self.test_obj.slot.H1_is_rad

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        assert self.widget.slot.H2 == 0.36
        assert self.test_obj.slot.H2 == 0.36

    def test_is_cst_tooth(self):
        """Check that the Widget allow be checked"""
        assert self.widget.slot.W1 is not None
        assert self.widget.slot.W2 is not None
        QTest.mouseClick(self.widget.is_cst_tooth, Qt.LeftButton)
        assert self.widget.is_cst_tooth.isChecked() == True
        assert self.widget.slot.W1 is None
        assert self.widget.slot.W2 is None
        assert self.widget.lf_W1.isEnabled() == False
        assert self.widget.lf_W2.isEnabled() == False
        assert self.widget.lf_W3.isEnabled() == True

        QTest.mouseClick(self.widget.is_cst_tooth, Qt.LeftButton)
        assert self.widget.is_cst_tooth.isChecked() == False
        assert self.widget.lf_W1.isEnabled() == True
        assert self.widget.lf_W2.isEnabled() == True
        assert self.widget.lf_W3.isEnabled() == False

    def test_output_txt(self):
        """Check that the Output text is computed and correct"""
        self.test_obj = LamSlotWind(
            Rint=0,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=5,
            Wrvd=0.02,
        )
        self.test_obj.slot = SlotW23(
            Zs=6,
            W0=50e-3,
            W1=90e-3,
            W2=100e-3,
            H0=20e-3,
            H1=35e-3,
            H2=130e-3,
            H1_is_rad=False,
        )
        self.widget = PWSlot23(self.test_obj)
        assert self.widget.w_out.out_slot_height.text() == "Slot height: 0.1816 [m]"

    def test_check(self):
        """Check that the check function is correctly returning error messages"""
        self.test_obj = LamSlotWind(Rint=0.7, Rext=0.5)
        self.test_obj.slot = SlotW23(
            H0=0.10, H1=0.11, H2=0.12, W0=None, W1=0.14, W2=0.15, H1_is_rad=False
        )
        self.widget = PWSlot23(self.test_obj)
        assert self.widget.check(self.test_obj) == "You must set W0 !"
        self.test_obj.slot = SlotW23(
            H0=None, H1=0.11, H2=0.12, W0=0.13, W1=0.14, W2=0.15, H1_is_rad=False
        )
        assert self.widget.check(self.test_obj) == "You must set H0 !"
        self.test_obj.slot = SlotW23(
            H0=0.10, H1=None, H2=0.12, W0=0.13, W1=0.14, W2=0.15, H1_is_rad=False
        )
        assert self.widget.check(self.test_obj) == "You must set H1 !"
        self.test_obj.slot = SlotW23(
            H0=0.10, H1=0.11, H2=None, W0=0.13, W1=0.14, W2=0.15, H1_is_rad=False
        )
        assert self.widget.check(self.test_obj) == "You must set H2 !"
        self.test_obj.slot = SlotW23(
            H0=0.10, H1=0.11, H2=0.12, W0=0.0011, W1=0.14, W2=0.15, H1_is_rad=False
        )
        assert (
            self.widget.check(self.test_obj)
            == "The slot height is greater than the lamination !"
        )

    def test_set_wedge(self):
        """Check that the GUI enables to edit the wedges"""
        assert self.test_obj.slot.wedge_mat is None
        assert not self.widget.g_wedge.isChecked()
        # Add new wedge
        assert self.widget.w_wedge_mat.c_mat_type.count() == 0
        self.widget.g_wedge.setChecked(True)
        assert self.widget.w_wedge_mat.c_mat_type.count() == 4
        assert self.test_obj.slot.wedge_mat is not None
        assert self.test_obj.slot.wedge_mat.name == "M400-50A"
        # Change material
        assert self.widget.w_wedge_mat.c_mat_type.currentIndex() == 2
        self.widget.w_wedge_mat.c_mat_type.setCurrentIndex(0)
        assert self.test_obj.slot.wedge_mat is not None
        assert self.test_obj.slot.wedge_mat.name == "Mat1"
        # Remove wedge
        self.widget.g_wedge.setChecked(False)
        assert self.test_obj.slot.wedge_mat is None
        # Add wedge again
        self.widget.g_wedge.setChecked(True)
        assert self.widget.w_wedge_mat.c_mat_type.count() == 4
        assert self.test_obj.slot.wedge_mat is not None
        assert self.test_obj.slot.wedge_mat.name == "M400-50A"


if __name__ == "__main__":
    a = TestPWSlot23()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.teardown_class()
    a.test_output_txt()
    a.test_set_H1()
    print("Done")
