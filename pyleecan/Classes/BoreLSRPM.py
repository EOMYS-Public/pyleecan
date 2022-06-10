# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/BoreLSRPM.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/BoreLSRPM
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from copy import deepcopy
from .Bore import Bore

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.BoreLSRPM.get_bore_line import get_bore_line
except ImportError as error:
    get_bore_line = error


from numpy import isnan
from ._check import InitUnKnowClassError


class BoreLSRPM(Bore):
    """Class for Bore LSRPM"""

    VERSION = 1

    # cf Methods.Machine.BoreLSRPM.get_bore_line
    if isinstance(get_bore_line, ImportError):
        get_bore_line = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use BoreLSRPM method get_bore_line: " + str(get_bore_line)
                )
            )
        )
    else:
        get_bore_line = get_bore_line
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, N=8, Rarc=0.0375, W1=0.0035, alpha=0, init_dict=None, init_str=None
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "N" in list(init_dict.keys()):
                N = init_dict["N"]
            if "Rarc" in list(init_dict.keys()):
                Rarc = init_dict["Rarc"]
            if "W1" in list(init_dict.keys()):
                W1 = init_dict["W1"]
            if "alpha" in list(init_dict.keys()):
                alpha = init_dict["alpha"]
        # Set the properties (value check and convertion are done in setter)
        self.N = N
        self.Rarc = Rarc
        self.W1 = W1
        self.alpha = alpha
        # Call Bore init
        super(BoreLSRPM, self).__init__()
        # The class is frozen (in Bore init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        BoreLSRPM_str = ""
        # Get the properties inherited from Bore
        BoreLSRPM_str += super(BoreLSRPM, self).__str__()
        BoreLSRPM_str += "N = " + str(self.N) + linesep
        BoreLSRPM_str += "Rarc = " + str(self.Rarc) + linesep
        BoreLSRPM_str += "W1 = " + str(self.W1) + linesep
        BoreLSRPM_str += "alpha = " + str(self.alpha) + linesep
        return BoreLSRPM_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Bore
        if not super(BoreLSRPM, self).__eq__(other):
            return False
        if other.N != self.N:
            return False
        if other.Rarc != self.Rarc:
            return False
        if other.W1 != self.W1:
            return False
        if other.alpha != self.alpha:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Bore
        diff_list.extend(
            super(BoreLSRPM, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._N != self._N:
            if is_add_value:
                val_str = " (self=" + str(self._N) + ", other=" + str(other._N) + ")"
                diff_list.append(name + ".N" + val_str)
            else:
                diff_list.append(name + ".N")
        if (
            other._Rarc is not None
            and self._Rarc is not None
            and isnan(other._Rarc)
            and isnan(self._Rarc)
        ):
            pass
        elif other._Rarc != self._Rarc:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._Rarc) + ", other=" + str(other._Rarc) + ")"
                )
                diff_list.append(name + ".Rarc" + val_str)
            else:
                diff_list.append(name + ".Rarc")
        if (
            other._W1 is not None
            and self._W1 is not None
            and isnan(other._W1)
            and isnan(self._W1)
        ):
            pass
        elif other._W1 != self._W1:
            if is_add_value:
                val_str = " (self=" + str(self._W1) + ", other=" + str(other._W1) + ")"
                diff_list.append(name + ".W1" + val_str)
            else:
                diff_list.append(name + ".W1")
        if (
            other._alpha is not None
            and self._alpha is not None
            and isnan(other._alpha)
            and isnan(self._alpha)
        ):
            pass
        elif other._alpha != self._alpha:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._alpha) + ", other=" + str(other._alpha) + ")"
                )
                diff_list.append(name + ".alpha" + val_str)
            else:
                diff_list.append(name + ".alpha")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Bore
        S += super(BoreLSRPM, self).__sizeof__()
        S += getsizeof(self.N)
        S += getsizeof(self.Rarc)
        S += getsizeof(self.W1)
        S += getsizeof(self.alpha)
        return S

    def as_dict(self, type_handle_ndarray=0, keep_function=False, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        type_handle_ndarray: int
            How to handle ndarray (0: tolist, 1: copy, 2: nothing)
        keep_function : bool
            True to keep the function object, else return str
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        # Get the properties inherited from Bore
        BoreLSRPM_dict = super(BoreLSRPM, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        BoreLSRPM_dict["N"] = self.N
        BoreLSRPM_dict["Rarc"] = self.Rarc
        BoreLSRPM_dict["W1"] = self.W1
        BoreLSRPM_dict["alpha"] = self.alpha
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        BoreLSRPM_dict["__class__"] = "BoreLSRPM"
        return BoreLSRPM_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        N_val = self.N
        Rarc_val = self.Rarc
        W1_val = self.W1
        alpha_val = self.alpha
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(N=N_val, Rarc=Rarc_val, W1=W1_val, alpha=alpha_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.N = None
        self.Rarc = None
        self.W1 = None
        self.alpha = None
        # Set to None the properties inherited from Bore
        super(BoreLSRPM, self)._set_None()

    def _get_N(self):
        """getter of N"""
        return self._N

    def _set_N(self, value):
        """setter of N"""
        check_var("N", value, "int", Vmin=0)
        self._N = value

    N = property(
        fget=_get_N,
        fset=_set_N,
        doc=u"""Number of flower arc

        :Type: int
        :min: 0
        """,
    )

    def _get_Rarc(self):
        """getter of Rarc"""
        return self._Rarc

    def _set_Rarc(self, value):
        """setter of Rarc"""
        check_var("Rarc", value, "float", Vmin=0)
        self._Rarc = value

    Rarc = property(
        fget=_get_Rarc,
        fset=_set_Rarc,
        doc=u"""Radius of the flower arc

        :Type: float
        :min: 0
        """,
    )

    def _get_W1(self):
        """getter of W1"""
        return self._W1

    def _set_W1(self, value):
        """setter of W1"""
        check_var("W1", value, "float")
        self._W1 = value

    W1 = property(
        fget=_get_W1,
        fset=_set_W1,
        doc=u"""Width of segement

        :Type: float
        """,
    )

    def _get_alpha(self):
        """getter of alpha"""
        return self._alpha

    def _set_alpha(self, value):
        """setter of alpha"""
        check_var("alpha", value, "float")
        self._alpha = value

    alpha = property(
        fget=_get_alpha,
        fset=_set_alpha,
        doc=u"""Angular offset

        :Type: float
        """,
    )
