# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets

from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.DAVDuct import DAVDuct
from pyleecan.GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.PVentCirc.PVentCirc import (
    PVentCirc,
)
from pyleecan.GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.PVentPolar.PVentPolar import (
    PVentPolar,
)
from pyleecan.GUI.Dialog.DMachineSetup.SLamParam.DAVDuct.PVentTrap.PVentTrap import (
    PVentTrap,
)
import pytest

@pytest.mark.GUI
class TestDAVDuct(object):
    """Test that the widget DAVDuct behave like it should"""

    def setup_method(self, method):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = Lamination(Rint=0.1, Rext=1, is_stator=True, is_internal=True)
        self.test_obj.axial_vent.append(
            VentilationCirc(Zh=8, H0=10e-3, D0=40e-3, Alpha0=0)
        )
        self.test_obj.axial_vent.append(
            VentilationCirc(Zh=9, H0=20e-3, D0=50e-3, Alpha0=0)
        )

        self.widget = DAVDuct(self.test_obj)

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test DAVDuct")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init_circ(self):
        """Check that the Widget initialise for circular ventilations"""
        assert self.widget.tab_vent.count() == 2
        assert self.widget.tab_vent.currentIndex() == 0

        # First set
        assert type(self.widget.tab_vent.widget(0).w_vent) == PVentCirc
        assert self.widget.tab_vent.widget(0).c_vent_type.currentIndex() == 0
        assert self.widget.tab_vent.widget(0).w_vent.si_Zh.value() == 8
        assert self.widget.tab_vent.widget(0).w_vent.lf_H0.value() == 10e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_D0.value() == 40e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_Alpha0.value() == 0
        
        # Second set
        assert type(self.widget.tab_vent.widget(1).w_vent) == PVentCirc
        assert self.widget.tab_vent.widget(1).c_vent_type.currentIndex() == 0
        assert self.widget.tab_vent.widget(1).w_vent.si_Zh.value() == 9
        assert self.widget.tab_vent.widget(1).w_vent.lf_H0.value() == 20e-3
        assert self.widget.tab_vent.widget(1).w_vent.lf_D0.value() == 50e-3
        assert self.widget.tab_vent.widget(1).w_vent.lf_Alpha0.value() == 0

    def test_init_trap(self):
        """Check that the Widget initialise for polar ventilations"""
        # Init the widget with Polar vent

        self.test_obj.axial_vent = [    
            VentilationTrap(Zh=4, H0=24e-3, D0=34e-3, W1=44e-3, W2=54e-3, Alpha0=0)    
        ]
        self.widget = DAVDuct(self.test_obj)

        assert self.widget.tab_vent.count() == 1
        assert self.widget.tab_vent.currentIndex() == 0

        # First set
        assert type(self.widget.tab_vent.widget(0).w_vent) == PVentTrap
        assert self.widget.tab_vent.widget(0).c_vent_type.currentIndex() == 1
        assert self.widget.tab_vent.widget(0).w_vent.si_Zh.value() == 4
        assert self.widget.tab_vent.widget(0).w_vent.lf_H0.value() == 24e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_D0.value() == 34e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_W1.value() == 44e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_W2.value() == 54e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_Alpha0.value() == 0

    def test_init_polar(self):
        """Check that the Widget initialise for polar ventilations
            """
        # Init the widget with Polar vent
        vent = list()
        vent.append(VentilationPolar(Zh=1, H0=21e-3, D0=31e-3, W1=41e-3, Alpha0=0))
        vent.append(VentilationPolar(Zh=2, H0=22e-3, D0=32e-3, W1=42e-3, Alpha0=0))
        vent.append(VentilationPolar(Zh=3, H0=23e-3, D0=33e-3, W1=43e-3, Alpha0=0))
        
        self.test_obj.axial_vent = vent
        self.widget = DAVDuct(self.test_obj)

        assert self.widget.tab_vent.count() == 3
        assert self.widget.tab_vent.currentIndex() == 0

        # First set
        assert type(self.widget.tab_vent.widget(0).w_vent) == PVentPolar
        assert self.widget.tab_vent.widget(0).c_vent_type.currentIndex() == 2
        assert self.widget.tab_vent.widget(0).w_vent.si_Zh.value() == 1
        assert self.widget.tab_vent.widget(0).w_vent.lf_H0.value() == 21e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_D0.value() == 31e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_W1.value() == 41e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_Alpha0.value() == 0
        
        # 2nd set
        assert type(self.widget.tab_vent.widget(1).w_vent) == PVentPolar
        assert self.widget.tab_vent.widget(1).c_vent_type.currentIndex() == 2
        assert self.widget.tab_vent.widget(1).w_vent.si_Zh.value() == 2
        assert self.widget.tab_vent.widget(1).w_vent.lf_H0.value() == 22e-3
        assert self.widget.tab_vent.widget(1).w_vent.lf_D0.value() == 32e-3
        assert self.widget.tab_vent.widget(1).w_vent.lf_W1.value() == 42e-3
        assert self.widget.tab_vent.widget(1).w_vent.lf_Alpha0.value() == 0
        
        # 3rd set
        assert type(self.widget.tab_vent.widget(2).w_vent) == PVentPolar
        assert self.widget.tab_vent.widget(2).c_vent_type.currentIndex() == 2
        assert self.widget.tab_vent.widget(2).w_vent.si_Zh.value() == 3
        assert self.widget.tab_vent.widget(2).w_vent.lf_H0.value() == 23e-3
        assert self.widget.tab_vent.widget(2).w_vent.lf_D0.value() == 33e-3
        assert self.widget.tab_vent.widget(2).w_vent.lf_W1.value() == 43e-3
        assert self.widget.tab_vent.widget(2).w_vent.lf_Alpha0.value() == 0

    def test_init_all_type(self):
        """Check that you can combine several kind of ventilations
            """
        self.test_obj = Lamination(Rint=0.1, Rext=1, is_stator=True, is_internal=True)
        self.test_obj.axial_vent.append(    
            VentilationCirc(Zh=8, H0=10e-3, D0=40e-3, Alpha0=0)    
        )
        self.test_obj.axial_vent.append(    
            VentilationTrap(Zh=4, H0=24e-3, D0=34e-3, W1=44e-3, W2=54e-3, Alpha0=0)    
        )
        self.test_obj.axial_vent.append(    
            VentilationPolar(Zh=3, H0=23e-3, D0=33e-3, W1=43e-3, Alpha0=0)    
        )
        self.widget = DAVDuct(self.test_obj)

        assert self.widget.tab_vent.count() == 3
        assert self.widget.tab_vent.currentIndex() == 0

        # First set
        assert type(self.widget.tab_vent.widget(0).w_vent) == PVentCirc
        assert self.widget.tab_vent.widget(0).c_vent_type.currentIndex() == 0
        assert self.widget.tab_vent.widget(0).w_vent.si_Zh.value() == 8
        
        # 2nd set
        assert type(self.widget.tab_vent.widget(1).w_vent) == PVentTrap
        assert self.widget.tab_vent.widget(1).c_vent_type.currentIndex() == 1
        assert self.widget.tab_vent.widget(1).w_vent.si_Zh.value() == 4
        
        # 3rd set
        assert type(self.widget.tab_vent.widget(2).w_vent) == PVentPolar
        assert self.widget.tab_vent.widget(2).c_vent_type.currentIndex() == 2
        assert self.widget.tab_vent.widget(2).w_vent.si_Zh.value() == 3

    def test_add_circ(self):
        """Test that you can add circ ventilation"""
        self.widget.b_new.clicked.emit(True)

        assert self.widget.tab_vent.count() == 3
        assert self.widget.tab_vent.currentIndex() == 0

        # First set
        assert type(self.widget.tab_vent.widget(0).w_vent) == PVentCirc
        assert self.widget.tab_vent.widget(0).c_vent_type.currentIndex() == 0
        assert self.widget.tab_vent.widget(0).w_vent.si_Zh.value() == 8
        assert self.widget.tab_vent.widget(0).w_vent.lf_H0.value() == 10e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_D0.value() == 40e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_Alpha0.value() == 0
        
        # Second set
        assert type(self.widget.tab_vent.widget(1).w_vent) == PVentCirc
        assert self.widget.tab_vent.widget(1).c_vent_type.currentIndex() == 0
        assert self.widget.tab_vent.widget(1).w_vent.si_Zh.value() == 9
        assert self.widget.tab_vent.widget(1).w_vent.lf_H0.value() == 20e-3
        assert self.widget.tab_vent.widget(1).w_vent.lf_D0.value() == 50e-3
        assert self.widget.tab_vent.widget(1).w_vent.lf_Alpha0.value() == 0
        
        # Third set
        assert type(self.widget.tab_vent.widget(2).w_vent) == PVentCirc
        assert self.widget.tab_vent.widget(2).c_vent_type.currentIndex() == 0
        assert self.widget.tab_vent.widget(2).w_vent.si_Zh.value() == 8
        assert self.widget.tab_vent.widget(2).w_vent.lf_H0.value() == None
        assert self.widget.tab_vent.widget(2).w_vent.lf_D0.value() == None
        assert self.widget.tab_vent.widget(2).w_vent.lf_Alpha0.value() == None

    def test_remove_circ(self):
        """Test that you can remove circ ventilation"""
        self.widget.b_remove.clicked.emit(True)
        assert self.widget.tab_vent.count() == 1
        assert self.widget.tab_vent.currentIndex() == 0
        
        # First set
        assert type(self.widget.tab_vent.widget(0).w_vent) == PVentCirc
        assert self.widget.tab_vent.widget(0).c_vent_type.currentIndex() == 0
        assert self.widget.tab_vent.widget(0).w_vent.si_Zh.value() == 8
        assert self.widget.tab_vent.widget(0).w_vent.lf_H0.value() == 10e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_D0.value() == 40e-3
        assert self.widget.tab_vent.widget(0).w_vent.lf_Alpha0.value() == 0