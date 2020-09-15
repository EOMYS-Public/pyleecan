# -*- coding: utf-8 -*-

import sys
from random import uniform

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest

from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.WindingCW1L import WindingCW1L
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.WindingCW2LR import WindingCW2LR
from pyleecan.Classes.WindingSC import WindingSC

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.MachineWRSM import MachineWRSM
from pyleecan.Classes.SlotW22 import SlotW22
from pyleecan.GUI.Dialog.DMachineSetup.SWindPat.SWindPat import SWindPat


from numpy.linalg import norm
from pyleecan.Functions.Winding.comp_wind_sym import comp_wind_sym

import numpy as np
import pytest


@pytest.mark.Functions
class Test_comp_wind_sym(object):
    """Test that comp_wind_sym work as it should"""

    def test_comp_wind_sym(self):

        arr = np.array([[[
         [ 9.,  0.,  0.],
         [ 9.,  0.,  0.],
         [ 0., -9.,  0.],
         [ 0., -9.,  0.],
         [ 0.,  0.,  9.],
         [ 0.,  0.,  9.],
         [-9.,  0.,  0.],
         [-9.,  0.,  0.],
         [ 0.,  9.,  0.],
         [ 0.,  9.,  0.],
         [ 0.,  0., -9.],
         [ 0.,  0., -9.],
         [ 9.,  0.,  0.],
         [ 9.,  0.,  0.],
         [ 0., -9.,  0.],
         [ 0., -9.,  0.],
         [ 0.,  0.,  9.],
         [ 0.,  0.,  9.],
         [-9.,  0.,  0.],
         [-9.,  0.,  0.],
         [ 0.,  9.,  0.],
         [ 0.,  9.,  0.],
         [ 0.,  0., -9.],
         [ 0.,  0., -9.],
         [ 9.,  0.,  0.],
         [ 9.,  0.,  0.],
         [ 0., -9.,  0.],
         [ 0., -9.,  0.],
         [ 0.,  0.,  9.],
         [ 0.,  0.,  9.],
         [-9.,  0.,  0.],
         [-9.,  0.,  0.],
         [ 0.,  9.,  0.],
         [ 0.,  9.,  0.],
         [ 0.,  0., -9.],
         [ 0.,  0., -9.],
         [ 9.,  0.,  0.],
         [ 9.,  0.,  0.],
         [ 0., -9.,  0.],
         [ 0., -9.,  0.],
         [ 0.,  0.,  9.],
         [ 0.,  0.,  9.],
         [-9.,  0.,  0.],
         [-9.,  0.,  0.],
         [ 0.,  9.,  0.],
         [ 0.,  9.,  0.],
         [ 0.,  0., -9.],
         [ 0.,  0., -9.]]]])

        print(arr.shape)
        assert (4*2, True) == comp_wind_sym(arr)   # 4*2 because there is 4 period but asym is true so *2


        arr = np.array([[[
            [ 0.,  0.,  0.],
            [ 1.,  1.,  1.],
            [ 2.,  2.,  2.],
            [ 0.,  0.,  0.],
            [ 1.,  1.,  1.],
            [ 2.,  2.,  2.],
            [ 0.,  0.,  0.],
            [ 1.,  1.,  1.],
            [ 2.,  2.,  2.]
        ]]])
        assert (3, False) == comp_wind_sym(arr)

        arr = np.array([[[
            [ 0.,  0.,  0.],
            [ 0.,  0.,  0.],
            [ 2.,  2.,  2.],
            [ 0.,  0.,  0.],
            [ 0.,  0.,  0.],
            [ 2.,  2.,  2.],
            [ 0.,  0.,  0.],
            [ 1.,  1.,  1.],
            [ 2.,  2.,  2.]
        ]]])
        assert (0, False) == comp_wind_sym(arr)