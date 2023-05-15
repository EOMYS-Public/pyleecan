# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Quanttity/PhysicIterator.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Quantity/PhysicIterator
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
    from ..Methods.Quantity.PhysicIterator.__iter__ import __iter__
except ImportError as error:
    __iter__ = error

try:
    from ..Methods.Quantity.PhysicIterator.__next__ import __next__
except ImportError as error:
    __next__ = error

try:
    from ..Methods.Quantity.PhysicIterator.init_iterator import init_iterator
except ImportError as error:
    init_iterator = error


from numpy import isnan
from ._check import InitUnKnowClassError


class PhysicIterator(FrozenClass):
    """Class for iterate throw the physics of a QuantityList"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Quantity.PhysicIterator.__iter__
    if isinstance(__iter__, ImportError):
        __iter__ = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use PhysicIterator method __iter__: " + str(__iter__)
                )
            )
        )
    else:
        __iter__ = __iter__
    # cf Methods.Quantity.PhysicIterator.__next__
    if isinstance(__next__, ImportError):
        __next__ = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use PhysicIterator method __next__: " + str(__next__)
                )
            )
        )
    else:
        __next__ = __next__
    # cf Methods.Quantity.PhysicIterator.init_iterator
    if isinstance(init_iterator, ImportError):
        init_iterator = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use PhysicIterator method init_iterator: "
                    + str(init_iterator)
                )
            )
        )
    else:
        init_iterator = init_iterator
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self, container=None, remaining_phy=None, init_dict=None, init_str=None
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
            if "container" in list(init_dict.keys()):
                container = init_dict["container"]
            if "remaining_phy" in list(init_dict.keys()):
                remaining_phy = init_dict["remaining_phy"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.container = container
        self.remaining_phy = remaining_phy

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        PhysicIterator_str = ""
        if self.parent is None:
            PhysicIterator_str += "parent = None " + linesep
        else:
            PhysicIterator_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        PhysicIterator_str += "container = " + str(self.container) + linesep
        PhysicIterator_str += (
            "remaining_phy = "
            + linesep
            + str(self.remaining_phy).replace(linesep, linesep + "\t")
            + linesep
        )
        return PhysicIterator_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.container != self.container:
            return False
        if other.remaining_phy != self.remaining_phy:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._container != self._container:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._container)
                    + ", other="
                    + str(other._container)
                    + ")"
                )
                diff_list.append(name + ".container" + val_str)
            else:
                diff_list.append(name + ".container")
        if other._remaining_phy != self._remaining_phy:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._remaining_phy)
                    + ", other="
                    + str(other._remaining_phy)
                    + ")"
                )
                diff_list.append(name + ".remaining_phy" + val_str)
            else:
                diff_list.append(name + ".remaining_phy")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.container is not None:
            for key, value in self.container.items():
                S += getsizeof(value) + getsizeof(key)
        if self.remaining_phy is not None:
            for value in self.remaining_phy:
                S += getsizeof(value)
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

        PhysicIterator_dict = dict()
        PhysicIterator_dict["container"] = (
            self.container.copy() if self.container is not None else None
        )
        PhysicIterator_dict["remaining_phy"] = (
            self.remaining_phy.copy() if self.remaining_phy is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        PhysicIterator_dict["__class__"] = "PhysicIterator"
        return PhysicIterator_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.container is None:
            container_val = None
        else:
            container_val = self.container.copy()
        if self.remaining_phy is None:
            remaining_phy_val = None
        else:
            remaining_phy_val = self.remaining_phy.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(container=container_val, remaining_phy=remaining_phy_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.container = None
        self.remaining_phy = None

    def _get_container(self):
        """getter of container"""
        return self._container

    def _set_container(self, value):
        """setter of container"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("container", value, "dict")
        self._container = value

    container = property(
        fget=_get_container,
        fset=_set_container,
        doc=u"""Dict of Dict of Quantity (pointer to a QuantityList container) 

        :Type: dict
        """,
    )

    def _get_remaining_phy(self):
        """getter of remaining_phy"""
        return self._remaining_phy

    def _set_remaining_phy(self, value):
        """setter of remaining_phy"""
        if type(value) is int and value == -1:
            value = list()
        check_var("remaining_phy", value, "list")
        self._remaining_phy = value

    remaining_phy = property(
        fget=_get_remaining_phy,
        fset=_set_remaining_phy,
        doc=u"""Remaining physics to iter throw

        :Type: list
        """,
    )
