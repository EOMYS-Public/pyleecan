# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Quanttity/Quantity.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Quantity/Quantity
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
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Quantity.Quantity.is_scalar import is_scalar
except ImportError as error:
    is_scalar = error

try:
    from ..Methods.Quantity.Quantity.is_vectorField import is_vectorField
except ImportError as error:
    is_vectorField = error

try:
    from ..Methods.Quantity.Quantity.is_data import is_data
except ImportError as error:
    is_data = error

try:
    from ..Methods.Quantity.Quantity.__eq__ import __eq__
except ImportError as error:
    __eq__ = error


from numpy import isnan
from ._check import InitUnKnowClassError


class Quantity(FrozenClass):
    """Class for defining the physic quantities"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Quantity.Quantity.is_scalar
    if isinstance(is_scalar, ImportError):
        is_scalar = property(
            fget=lambda x: raise_(
                ImportError("Can't use Quantity method is_scalar: " + str(is_scalar))
            )
        )
    else:
        is_scalar = is_scalar
    # cf Methods.Quantity.Quantity.is_vectorField
    if isinstance(is_vectorField, ImportError):
        is_vectorField = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Quantity method is_vectorField: " + str(is_vectorField)
                )
            )
        )
    else:
        is_vectorField = is_vectorField
    # cf Methods.Quantity.Quantity.is_data
    if isinstance(is_data, ImportError):
        is_data = property(
            fget=lambda x: raise_(
                ImportError("Can't use Quantity method is_data: " + str(is_data))
            )
        )
    else:
        is_data = is_data
    # cf Methods.Quantity.Quantity.__eq__
    if isinstance(__eq__, ImportError):
        __eq__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use Quantity method __eq__: " + str(__eq__))
            )
        )
    else:
        __eq__ = __eq__
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
        self.parent = None
        self.symbol = symbol
        self.name = name
        self.physic = physic
        self.unit = unit
        self.unit_plot = unit_plot
        self.getter = getter

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Quantity_str = ""
        if self.parent is None:
            Quantity_str += "parent = None " + linesep
        else:
            Quantity_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Quantity_str += 'symbol = "' + str(self.symbol) + '"' + linesep
        Quantity_str += 'name = "' + str(self.name) + '"' + linesep
        Quantity_str += 'physic = "' + str(self.physic) + '"' + linesep
        Quantity_str += 'unit = "' + str(self.unit) + '"' + linesep
        Quantity_str += 'unit_plot = "' + str(self.unit_plot) + '"' + linesep
        Quantity_str += 'getter = "' + str(self.getter) + '"' + linesep
        return Quantity_str

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._symbol != self._symbol:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._symbol)
                    + ", other="
                    + str(other._symbol)
                    + ")"
                )
                diff_list.append(name + ".symbol" + val_str)
            else:
                diff_list.append(name + ".symbol")
        if other._name != self._name:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._name) + ", other=" + str(other._name) + ")"
                )
                diff_list.append(name + ".name" + val_str)
            else:
                diff_list.append(name + ".name")
        if other._physic != self._physic:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._physic)
                    + ", other="
                    + str(other._physic)
                    + ")"
                )
                diff_list.append(name + ".physic" + val_str)
            else:
                diff_list.append(name + ".physic")
        if other._unit != self._unit:
            if is_add_value:
                val_str = (
                    " (self=" + str(self._unit) + ", other=" + str(other._unit) + ")"
                )
                diff_list.append(name + ".unit" + val_str)
            else:
                diff_list.append(name + ".unit")
        if other._unit_plot != self._unit_plot:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._unit_plot)
                    + ", other="
                    + str(other._unit_plot)
                    + ")"
                )
                diff_list.append(name + ".unit_plot" + val_str)
            else:
                diff_list.append(name + ".unit_plot")
        if other._getter != self._getter:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._getter)
                    + ", other="
                    + str(other._getter)
                    + ")"
                )
                diff_list.append(name + ".getter" + val_str)
            else:
                diff_list.append(name + ".getter")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.symbol)
        S += getsizeof(self.name)
        S += getsizeof(self.physic)
        S += getsizeof(self.unit)
        S += getsizeof(self.unit_plot)
        S += getsizeof(self.getter)
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

        Quantity_dict = dict()
        Quantity_dict["symbol"] = self.symbol
        Quantity_dict["name"] = self.name
        Quantity_dict["physic"] = self.physic
        Quantity_dict["unit"] = self.unit
        Quantity_dict["unit_plot"] = self.unit_plot
        Quantity_dict["getter"] = self.getter
        # The class name is added to the dict for deserialisation purpose
        Quantity_dict["__class__"] = "Quantity"
        return Quantity_dict

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

        self.symbol = None
        self.name = None
        self.physic = None
        self.unit = None
        self.unit_plot = None
        self.getter = None

    def _get_symbol(self):
        """getter of symbol"""
        return self._symbol

    def _set_symbol(self, value):
        """setter of symbol"""
        check_var("symbol", value, "str")
        self._symbol = value

    symbol = property(
        fget=_get_symbol,
        fset=_set_symbol,
        doc=u"""Symbol of the Quantity

        :Type: str
        """,
    )

    def _get_name(self):
        """getter of name"""
        return self._name

    def _set_name(self, value):
        """setter of name"""
        check_var("name", value, "str")
        self._name = value

    name = property(
        fget=_get_name,
        fset=_set_name,
        doc=u"""name of the quantity

        :Type: str
        """,
    )

    def _get_physic(self):
        """getter of physic"""
        return self._physic

    def _set_physic(self, value):
        """setter of physic"""
        check_var("physic", value, "str")
        self._physic = value

    physic = property(
        fget=_get_physic,
        fset=_set_physic,
        doc=u"""Physic of the quantity

        :Type: str
        """,
    )

    def _get_unit(self):
        """getter of unit"""
        return self._unit

    def _set_unit(self, value):
        """setter of unit"""
        check_var("unit", value, "str")
        self._unit = value

    unit = property(
        fget=_get_unit,
        fset=_set_unit,
        doc=u"""SI unit of the quantity

        :Type: str
        """,
    )

    def _get_unit_plot(self):
        """getter of unit_plot"""
        return self._unit_plot

    def _set_unit_plot(self, value):
        """setter of unit_plot"""
        check_var("unit_plot", value, "str")
        self._unit_plot = value

    unit_plot = property(
        fget=_get_unit_plot,
        fset=_set_unit_plot,
        doc=u"""Default unit when ploting the quantity

        :Type: str
        """,
    )

    def _get_getter(self):
        """getter of getter"""
        return self._getter

    def _set_getter(self, value):
        """setter of getter"""
        check_var("getter", value, "str")
        self._getter = value

    getter = property(
        fget=_get_getter,
        fset=_set_getter,
        doc=u"""Name of the getter method

        :Type: str
        """,
    )
