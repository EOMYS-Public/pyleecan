# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Quantity/QuantityIterator.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Quantity/QuantityIterator
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
    from ..Methods.Quantity.QuantityIterator.__iter__ import __iter__
except ImportError as error:
    __iter__ = error

try:
    from ..Methods.Quantity.QuantityIterator.__next__ import __next__
except ImportError as error:
    __next__ = error

try:
    from ..Methods.Quantity.QuantityIterator.init_iterator import init_iterator
except ImportError as error:
    init_iterator = error


from numpy import isnan
from ._check import InitUnKnowClassError


class QuantityIterator(FrozenClass):
    """Class for iterate throw the quantity of a QuantityList"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Quantity.QuantityIterator.__iter__
    if isinstance(__iter__, ImportError):
        __iter__ = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityIterator method __iter__: " + str(__iter__)
                )
            )
        )
    else:
        __iter__ = __iter__
    # cf Methods.Quantity.QuantityIterator.__next__
    if isinstance(__next__, ImportError):
        __next__ = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityIterator method __next__: " + str(__next__)
                )
            )
        )
    else:
        __next__ = __next__
    # cf Methods.Quantity.QuantityIterator.init_iterator
    if isinstance(init_iterator, ImportError):
        init_iterator = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityIterator method init_iterator: "
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
        self,
        container=None,
        remaining_qty=None,
        phy_dict=None,
        physic_iter=None,
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
            if "container" in list(init_dict.keys()):
                container = init_dict["container"]
            if "remaining_qty" in list(init_dict.keys()):
                remaining_qty = init_dict["remaining_qty"]
            if "phy_dict" in list(init_dict.keys()):
                phy_dict = init_dict["phy_dict"]
            if "physic_iter" in list(init_dict.keys()):
                physic_iter = init_dict["physic_iter"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.container = container
        self.remaining_qty = remaining_qty
        self.phy_dict = phy_dict
        self.physic_iter = physic_iter

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        QuantityIterator_str = ""
        if self.parent is None:
            QuantityIterator_str += "parent = None " + linesep
        else:
            QuantityIterator_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        QuantityIterator_str += "container = " + str(self.container) + linesep
        QuantityIterator_str += (
            "remaining_qty = "
            + linesep
            + str(self.remaining_qty).replace(linesep, linesep + "\t")
            + linesep
        )
        QuantityIterator_str += "phy_dict = " + str(self.phy_dict) + linesep
        if self.physic_iter is not None:
            tmp = (
                self.physic_iter.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            QuantityIterator_str += "physic_iter = " + tmp
        else:
            QuantityIterator_str += "physic_iter = None" + linesep + linesep
        return QuantityIterator_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.container != self.container:
            return False
        if other.remaining_qty != self.remaining_qty:
            return False
        if other.phy_dict != self.phy_dict:
            return False
        if other.physic_iter != self.physic_iter:
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
        if other._remaining_qty != self._remaining_qty:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._remaining_qty)
                    + ", other="
                    + str(other._remaining_qty)
                    + ")"
                )
                diff_list.append(name + ".remaining_qty" + val_str)
            else:
                diff_list.append(name + ".remaining_qty")
        if other._phy_dict != self._phy_dict:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._phy_dict)
                    + ", other="
                    + str(other._phy_dict)
                    + ")"
                )
                diff_list.append(name + ".phy_dict" + val_str)
            else:
                diff_list.append(name + ".phy_dict")
        if (other.physic_iter is None and self.physic_iter is not None) or (
            other.physic_iter is not None and self.physic_iter is None
        ):
            diff_list.append(name + ".physic_iter None mismatch")
        elif self.physic_iter is not None:
            diff_list.extend(
                self.physic_iter.compare(
                    other.physic_iter,
                    name=name + ".physic_iter",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.container is not None:
            for key, value in self.container.items():
                S += getsizeof(value) + getsizeof(key)
        if self.remaining_qty is not None:
            for value in self.remaining_qty:
                S += getsizeof(value)
        if self.phy_dict is not None:
            for key, value in self.phy_dict.items():
                S += getsizeof(value) + getsizeof(key)
        S += getsizeof(self.physic_iter)
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

        QuantityIterator_dict = dict()
        QuantityIterator_dict["container"] = (
            self.container.copy() if self.container is not None else None
        )
        QuantityIterator_dict["remaining_qty"] = (
            self.remaining_qty.copy() if self.remaining_qty is not None else None
        )
        QuantityIterator_dict["phy_dict"] = (
            self.phy_dict.copy() if self.phy_dict is not None else None
        )
        if self.physic_iter is None:
            QuantityIterator_dict["physic_iter"] = None
        else:
            QuantityIterator_dict["physic_iter"] = self.physic_iter.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        # The class name is added to the dict for deserialisation purpose
        QuantityIterator_dict["__class__"] = "QuantityIterator"
        return QuantityIterator_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.container is None:
            container_val = None
        else:
            container_val = self.container.copy()
        if self.remaining_qty is None:
            remaining_qty_val = None
        else:
            remaining_qty_val = self.remaining_qty.copy()
        if self.phy_dict is None:
            phy_dict_val = None
        else:
            phy_dict_val = self.phy_dict.copy()
        if self.physic_iter is None:
            physic_iter_val = None
        else:
            physic_iter_val = self.physic_iter.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            container=container_val,
            remaining_qty=remaining_qty_val,
            phy_dict=phy_dict_val,
            physic_iter=physic_iter_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.container = None
        self.remaining_qty = None
        self.phy_dict = None
        if self.physic_iter is not None:
            self.physic_iter._set_None()

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

    def _get_remaining_qty(self):
        """getter of remaining_qty"""
        return self._remaining_qty

    def _set_remaining_qty(self, value):
        """setter of remaining_qty"""
        if type(value) is int and value == -1:
            value = list()
        check_var("remaining_qty", value, "list")
        self._remaining_qty = value

    remaining_qty = property(
        fget=_get_remaining_qty,
        fset=_set_remaining_qty,
        doc=u"""Remaining qty to iter throw

        :Type: list
        """,
    )

    def _get_phy_dict(self):
        """getter of phy_dict"""
        return self._phy_dict

    def _set_phy_dict(self, value):
        """setter of phy_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("phy_dict", value, "dict")
        self._phy_dict = value

    phy_dict = property(
        fget=_get_phy_dict,
        fset=_set_phy_dict,
        doc=u"""Dict of quantities of the current physic

        :Type: dict
        """,
    )

    def _get_physic_iter(self):
        """getter of physic_iter"""
        return self._physic_iter

    def _set_physic_iter(self, value):
        """setter of physic_iter"""
        if isinstance(value, str):  # Load from file
            try:
                value = load_init_dict(value)[1]
            except Exception as e:
                self.get_logger().error(
                    "Error while loading " + value + ", setting None instead"
                )
                value = None
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "physic_iter"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            PhysicIterator = import_class(
                "pyleecan.Classes", "PhysicIterator", "physic_iter"
            )
            value = PhysicIterator()
        check_var("physic_iter", value, "PhysicIterator")
        self._physic_iter = value

        if self._physic_iter is not None:
            self._physic_iter.parent = self

    physic_iter = property(
        fget=_get_physic_iter,
        fset=_set_physic_iter,
        doc=u"""Physic iterator

        :Type: PhysicIterator
        """,
    )
