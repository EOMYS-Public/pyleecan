# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Quantity/QuantityVectorField.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Quantity/QuantityVectorField
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
    from ..Methods.Quantity.QuantityVectorField.is_vectorField import is_vectorField
except ImportError as error:
    is_vectorField = error

try:
    from ..Methods.Quantity.QuantityVectorField.get_component_quantity import (
        get_component_quantity,
    )
except ImportError as error:
    get_component_quantity = error

try:
    from ..Methods.Quantity.QuantityVectorField.__eq__ import __eq__
except ImportError as error:
    __eq__ = error


from numpy import isnan
from ._check import InitUnKnowClassError


class QuantityVectorField(Quantity):
    """Class for defining a vector field physics quantity"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Quantity.QuantityVectorField.is_vectorField
    if isinstance(is_vectorField, ImportError):
        is_vectorField = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityVectorField method is_vectorField: "
                    + str(is_vectorField)
                )
            )
        )
    else:
        is_vectorField = is_vectorField
    # cf Methods.Quantity.QuantityVectorField.get_component_quantity
    if isinstance(get_component_quantity, ImportError):
        get_component_quantity = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityVectorField method get_component_quantity: "
                    + str(get_component_quantity)
                )
            )
        )
    else:
        get_component_quantity = get_component_quantity
    # cf Methods.Quantity.QuantityVectorField.__eq__
    if isinstance(__eq__, ImportError):
        __eq__ = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use QuantityVectorField method __eq__: " + str(__eq__)
                )
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
        axes_name=None,
        components=-1,
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
            if "axes_name" in list(init_dict.keys()):
                axes_name = init_dict["axes_name"]
            if "components" in list(init_dict.keys()):
                components = init_dict["components"]
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
        self.axes_name = axes_name
        self.components = components
        # Call Quantity init
        super(QuantityVectorField, self).__init__(
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

        QuantityVectorField_str = ""
        # Get the properties inherited from Quantity
        QuantityVectorField_str += super(QuantityVectorField, self).__str__()
        if len(self.axes_name) == 0:
            QuantityVectorField_str += "axes_name = []" + linesep
        for ii in range(len(self.axes_name)):
            tmp = (
                self.axes_name[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            QuantityVectorField_str += (
                "axes_name[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        if len(self.components) == 0:
            QuantityVectorField_str += "components = []" + linesep
        for ii in range(len(self.components)):
            tmp = (
                self.components[ii].__str__().replace(linesep, linesep + "\t") + linesep
            )
            QuantityVectorField_str += (
                "components[" + str(ii) + "] =" + tmp + linesep + linesep
            )
        return QuantityVectorField_str

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Quantity
        diff_list.extend(
            super(QuantityVectorField, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.axes_name is None and self.axes_name is not None) or (
            other.axes_name is not None and self.axes_name is None
        ):
            diff_list.append(name + ".axes_name None mismatch")
        elif self.axes_name is None:
            pass
        elif len(other.axes_name) != len(self.axes_name):
            diff_list.append("len(" + name + ".axes_name)")
        else:
            for ii in range(len(other.axes_name)):
                diff_list.extend(
                    self.axes_name[ii].compare(
                        other.axes_name[ii],
                        name=name + ".axes_name[" + str(ii) + "]",
                        ignore_list=ignore_list,
                        is_add_value=is_add_value,
                    )
                )
        if (other.components is None and self.components is not None) or (
            other.components is not None and self.components is None
        ):
            diff_list.append(name + ".components None mismatch")
        elif self.components is None:
            pass
        elif len(other.components) != len(self.components):
            diff_list.append("len(" + name + ".components)")
        else:
            for ii in range(len(other.components)):
                diff_list.extend(
                    self.components[ii].compare(
                        other.components[ii],
                        name=name + ".components[" + str(ii) + "]",
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

        # Get size of the properties inherited from Quantity
        S += super(QuantityVectorField, self).__sizeof__()
        if self.axes_name is not None:
            for value in self.axes_name:
                S += getsizeof(value)
        if self.components is not None:
            for value in self.components:
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

        # Get the properties inherited from Quantity
        QuantityVectorField_dict = super(QuantityVectorField, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.axes_name is None:
            QuantityVectorField_dict["axes_name"] = None
        else:
            QuantityVectorField_dict["axes_name"] = list()
            for obj in self.axes_name:
                if obj is not None:
                    QuantityVectorField_dict["axes_name"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    QuantityVectorField_dict["axes_name"].append(None)
        if self.components is None:
            QuantityVectorField_dict["components"] = None
        else:
            QuantityVectorField_dict["components"] = list()
            for obj in self.components:
                if obj is not None:
                    QuantityVectorField_dict["components"].append(
                        obj.as_dict(
                            type_handle_ndarray=type_handle_ndarray,
                            keep_function=keep_function,
                            **kwargs
                        )
                    )
                else:
                    QuantityVectorField_dict["components"].append(None)
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        QuantityVectorField_dict["__class__"] = "QuantityVectorField"
        return QuantityVectorField_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.axes_name is None:
            axes_name_val = None
        else:
            axes_name_val = list()
            for obj in self.axes_name:
                axes_name_val.append(obj.copy())
        if self.components is None:
            components_val = None
        else:
            components_val = list()
            for obj in self.components:
                components_val.append(obj.copy())
        symbol_val = self.symbol
        name_val = self.name
        physic_val = self.physic
        unit_val = self.unit
        unit_plot_val = self.unit_plot
        getter_val = self.getter
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            axes_name=axes_name_val,
            components=components_val,
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

        self.axes_name = None
        self.components = None
        # Set to None the properties inherited from Quantity
        super(QuantityVectorField, self)._set_None()

    def _get_axes_name(self):
        """getter of axes_name"""
        if self._axes_name is not None:
            for obj in self._axes_name:
                if obj is not None:
                    obj.parent = self
        return self._axes_name

    def _set_axes_name(self, value):
        """setter of axes_name"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "axes_name"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("axes_name", value, "[str]")
        self._axes_name = value

    axes_name = property(
        fget=_get_axes_name,
        fset=_set_axes_name,
        doc=u"""Name of the possible axes

        :Type: [str]
        """,
    )

    def _get_components(self):
        """getter of components"""
        if self._components is not None:
            for obj in self._components:
                if obj is not None:
                    obj.parent = self
        return self._components

    def _set_components(self, value):
        """setter of components"""
        if type(value) is list:
            for ii, obj in enumerate(value):
                if isinstance(obj, str):  # Load from file
                    try:
                        obj = load_init_dict(obj)[1]
                    except Exception as e:
                        self.get_logger().error(
                            "Error while loading " + obj + ", setting None instead"
                        )
                        obj = None
                        value[ii] = None
                if type(obj) is dict:
                    class_obj = import_class(
                        "pyleecan.Classes", obj.get("__class__"), "components"
                    )
                    value[ii] = class_obj(init_dict=obj)
                if value[ii] is not None:
                    value[ii].parent = self
        if value == -1:
            value = list()
        check_var("components", value, "[str]")
        self._components = value

    components = property(
        fget=_get_components,
        fset=_set_components,
        doc=u"""Name of the component

        :Type: [str]
        """,
    )
