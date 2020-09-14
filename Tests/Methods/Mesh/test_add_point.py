# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.MeshMat import MeshMat
from pyleecan.Classes.PointMat import PointMat
import numpy as np

@pytest.mark.MeshSol
@pytest.mark.METHODS
class Test_add_point(object):
    """unittest for points getter methods"""

    @classmethod
    def setup_method(self, method):
        self.mesh = MeshMat()
        self.mesh.point = PointMat()
        self.mesh.point.add_point(np.array([0, 0]))
        self.mesh.point.add_point(np.array([1, 0]))
        self.mesh.point.add_point(np.array([1, 2]))
        self.mesh.point.add_point(np.array([2, 3]))
        self.mesh.point.add_point(np.array([3, 3]))

    def test_add_point(self):
        """unittest with CellMat and PointMat objects, only Triangle3 elements are defined"""

        assert self.mesh.point.add_point(np.array([1, 2])) == None

    
