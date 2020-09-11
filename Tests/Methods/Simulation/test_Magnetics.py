# -*- coding: utf-8 -*-

import pytest
from numpy import pi
from os.path import join
from pyleecan.Functions.load import load
from pyleecan.Classes.Magnetics import Magnetics
from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Methods.Simulation.Input import InputError

@pytest.mark.METHODS
class Test_Magnetics(object):

    def test_comp_emf(self):
        sim = Simu1(mag=Magnetics())
        with pytest.raises(InputError) as context:
            sim.mag.comp_emf()

