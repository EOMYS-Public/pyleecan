# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Quantity/QuantityList.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Quantity/QuantityList
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
    from ..Methods.Quantity.QuantityList.add_quantity import add_quantity
except ImportError as error:
    add_quantity = error

try:
    from ..Methods.Quantity.QuantityList.filter import filter
except ImportError as error:
    filter = error

try:
    from ..Methods.Quantity.QuantityList.create_datakeeper import create_datakeeper
except ImportError as error:
    create_datakeeper = error

try:
    from ..Methods.Quantity.QuantityList.__getitem__ import __getitem__
except ImportError as error:
    __getitem__ = error

try:
    from ..Methods.Quantity.QuantityList.get_quantity_iter import get_quantity_iter
except ImportError as error:
    get_quantity_iter = error

try:
    from ..Methods.Quantity.QuantityList.get_physic_iter import get_physic_iter
except ImportError as error:
    get_physic_iter = error

try:
    from ..Methods.Quantity.QuantityList.__iter__ import __iter__
except ImportError as error:
    __iter__ = error

try:
    from ..Methods.Quantity.QuantityList.is_in import is_in
except ImportError as error:
    is_in = error


from numpy import isnan
from ._check import InitUnKnowClassError


class QuantityList(FrozenClass):
    """Container of Quantity"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Quantity.QuantityList.add_quantity
    if isinstance(add_quantity, ImportError):
        add_quantity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityList method add_quantity: " + str(add_quantity)
                )
            )
        )
    else:
        add_quantity = add_quantity
    # cf Methods.Quantity.QuantityList.filter
    if isinstance(filter, ImportError):
        filter = property(
            fget=lambda x: raise_(
                ImportError("Can't use QuantityList method filter: " + str(filter))
            )
        )
    else:
        filter = filter
    # cf Methods.Quantity.QuantityList.create_datakeeper
    if isinstance(create_datakeeper, ImportError):
        create_datakeeper = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityList method create_datakeeper: "
                    + str(create_datakeeper)
                )
            )
        )
    else:
        create_datakeeper = create_datakeeper
    # cf Methods.Quantity.QuantityList.__getitem__
    if isinstance(__getitem__, ImportError):
        __getitem__ = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityList method __getitem__: " + str(__getitem__)
                )
            )
        )
    else:
        __getitem__ = __getitem__
    # cf Methods.Quantity.QuantityList.get_quantity_iter
    if isinstance(get_quantity_iter, ImportError):
        get_quantity_iter = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityList method get_quantity_iter: "
                    + str(get_quantity_iter)
                )
            )
        )
    else:
        get_quantity_iter = get_quantity_iter
    # cf Methods.Quantity.QuantityList.get_physic_iter
    if isinstance(get_physic_iter, ImportError):
        get_physic_iter = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityList method get_physic_iter: "
                    + str(get_physic_iter)
                )
            )
        )
    else:
        get_physic_iter = get_physic_iter
    # cf Methods.Quantity.QuantityList.__iter__
    if isinstance(__iter__, ImportError):
        __iter__ = property(
            fget=lambda x: raise_(
                ImportError("Can't use QuantityList method __iter__: " + str(__iter__))
            )
        )
    else:
        __iter__ = __iter__
    # cf Methods.Quantity.QuantityList.is_in
    if isinstance(is_in, ImportError):
        is_in = property(
            fget=lambda x: raise_(
                ImportError("Can't use QuantityList method is_in: " + str(is_in))
            )
        )
    else:
        is_in = is_in
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, container=-1, init_dict=None, init_str=None):
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
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.container = container

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        QuantityList_str = ""
        if self.parent is None:
            QuantityList_str += "parent = None " + linesep
        else:
            QuantityList_str += (
                "parent = " + str(type(self.parent)) + " object" + linesep
            )
        QuantityList_str += "container = " + str(self.container) + linesep
        return QuantityList_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.container != self.container:
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
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        if self.container is not None:
            for key, value in self.container.items():
                S += getsizeof(value) + getsizeof(key)
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

        QuantityList_dict = dict()
        QuantityList_dict["container"] = (
            self.container.copy() if self.container is not None else None
        )
        # The class name is added to the dict for deserialisation purpose
        QuantityList_dict["__class__"] = "QuantityList"
        return QuantityList_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.container is None:
            container_val = None
        else:
            container_val = self.container.copy()
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(container=container_val)
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.container = None

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
        doc=u"""Dict of Dict of Quantity

        :Type: dict
        """,
    )
