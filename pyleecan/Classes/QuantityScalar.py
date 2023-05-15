# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Quanttity/QuantityScalar.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Quantity/QuantityScalar
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
from .Quantity import Quantity

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Quantity.QuantityScalar.is_scalar import is_scalar
except ImportError as error:
    is_scalar = error

try:
    from ..Methods.Quantity.QuantityScalar.create_datakeeper import create_datakeeper
except ImportError as error:
    create_datakeeper = error


from numpy import isnan
from ._check import InitUnKnowClassError


class QuantityScalar(Quantity):
    """Class for defining a scalar physics quantity"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Quantity.QuantityScalar.is_scalar
    if isinstance(is_scalar, ImportError):
        is_scalar = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityScalar method is_scalar: " + str(is_scalar)
                )
            )
        )
    else:
        is_scalar = is_scalar
    # cf Methods.Quantity.QuantityScalar.create_datakeeper
    if isinstance(create_datakeeper, ImportError):
        create_datakeeper = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityScalar method create_datakeeper: "
                    + str(create_datakeeper)
                )
            )
        )
    else:
        create_datakeeper = create_datakeeper
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        symbol="",
        name="",
        physic="",
        unit="",
        unit_plot="",
        getter="",
        init_dict=None,
        init_str=None,
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
            if "symbol" in list(init_dict.keys()):
                symbol = init_dict["symbol"]
            if "name" in list(init_dict.keys()):
                name = init_dict["name"]
            if "physic" in list(init_dict.keys()):
                physic = init_dict["physic"]
            if "unit" in list(init_dict.keys()):
                unit = init_dict["unit"]
            if "unit_plot" in list(init_dict.keys()):
                unit_plot = init_dict["unit_plot"]
            if "getter" in list(init_dict.keys()):
                getter = init_dict["getter"]
        # Set the properties (value check and convertion are done in setter)
        # Call Quantity init
        super(QuantityScalar, self).__init__(
            symbol=symbol,
            name=name,
            physic=physic,
            unit=unit,
            unit_plot=unit_plot,
            getter=getter,
        )
        # The class is frozen (in Quantity init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        QuantityScalar_str = ""
        # Get the properties inherited from Quantity
        QuantityScalar_str += super(QuantityScalar, self).__str__()
        return QuantityScalar_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Quantity
        if not super(QuantityScalar, self).__eq__(other):
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Quantity
        diff_list.extend(
            super(QuantityScalar, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Quantity
        S += super(QuantityScalar, self).__sizeof__()
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

        # Get the properties inherited from Quantity
        QuantityScalar_dict = super(QuantityScalar, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        QuantityScalar_dict["__class__"] = "QuantityScalar"
        return QuantityScalar_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        symbol_val = self.symbol
        name_val = self.name
        physic_val = self.physic
        unit_val = self.unit
        unit_plot_val = self.unit_plot
        getter_val = self.getter
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            symbol=symbol_val,
            name=name_val,
            physic=physic_val,
            unit=unit_val,
            unit_plot=unit_plot_val,
            getter=getter_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        # Set to None the properties inherited from Quantity
        super(QuantityScalar, self)._set_None()
