# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Slot/VentilationNotchW60.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Slot/VentilationNotchW60
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
from .Hole import Hole

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Slot.VentilationNotchW60.build_geometry import build_geometry
except ImportError as error:
    build_geometry = error

try:
    from ..Methods.Slot.VentilationNotchW60.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Slot.VentilationNotchW60.comp_radius import comp_radius
except ImportError as error:
    comp_radius = error

try:
    from ..Methods.Slot.VentilationNotchW60.comp_surface import comp_surface
except ImportError as error:
    comp_surface = error

try:
    from ..Methods.Slot.VentilationNotchW60.get_center import get_center
except ImportError as error:
    get_center = error


from numpy import isnan
from ._check import InitUnKnowClassError


class VentilationNotchW60(Hole):
    """Circular axial ventilation duct"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Slot.VentilationNotchW60.build_geometry
    if isinstance(build_geometry, ImportError):
        build_geometry = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationNotchW60 method build_geometry: "
                    + str(build_geometry)
                )
            )
        )
    else:
        build_geometry = build_geometry
    # cf Methods.Slot.VentilationNotchW60.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use VentilationNotchW60 method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Slot.VentilationNotchW60.comp_radius
    if isinstance(comp_radius, ImportError):
        comp_radius = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationNotchW60 method comp_radius: "
                    + str(comp_radius)
                )
            )
        )
    else:
        comp_radius = comp_radius
    # cf Methods.Slot.VentilationNotchW60.comp_surface
    if isinstance(comp_surface, ImportError):
        comp_surface = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationNotchW60 method comp_surface: "
                    + str(comp_surface)
                )
            )
        )
    else:
        comp_surface = comp_surface
    # cf Methods.Slot.VentilationNotchW60.get_center
    if isinstance(get_center, ImportError):
        get_center = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use VentilationNotchW60 method get_center: "
                    + str(get_center)
                )
            )
        )
    else:
        get_center = get_center
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        notch_shape=None,
        position=0.5,
        Zh=36,
        mat_void=-1,
        magnetization_dict_offset=None,
        Alpha0=0,
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
            if "notch_shape" in list(init_dict.keys()):
                notch_shape = init_dict["notch_shape"]
            if "position" in list(init_dict.keys()):
                position = init_dict["position"]
            if "Zh" in list(init_dict.keys()):
                Zh = init_dict["Zh"]
            if "mat_void" in list(init_dict.keys()):
                mat_void = init_dict["mat_void"]
            if "magnetization_dict_offset" in list(init_dict.keys()):
                magnetization_dict_offset = init_dict["magnetization_dict_offset"]
            if "Alpha0" in list(init_dict.keys()):
                Alpha0 = init_dict["Alpha0"]
        # Set the properties (value check and convertion are done in setter)
        self.notch_shape = notch_shape
        self.position = position
        # Call Hole init
        super(VentilationNotchW60, self).__init__(
            Zh=Zh,
            mat_void=mat_void,
            magnetization_dict_offset=magnetization_dict_offset,
            Alpha0=Alpha0,
        )
        # The class is frozen (in Hole init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        VentilationNotchW60_str = ""
        # Get the properties inherited from Hole
        VentilationNotchW60_str += super(VentilationNotchW60, self).__str__()
        if self.notch_shape is not None:
            tmp = (
                self.notch_shape.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            VentilationNotchW60_str += "notch_shape = " + tmp
        else:
            VentilationNotchW60_str += "notch_shape = None" + linesep + linesep
        VentilationNotchW60_str += "position = " + str(self.position) + linesep
        return VentilationNotchW60_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Hole
        if not super(VentilationNotchW60, self).__eq__(other):
            return False
        if other.notch_shape != self.notch_shape:
            return False
        if other.position != self.position:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Hole
        diff_list.extend(
            super(VentilationNotchW60, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if (other.notch_shape is None and self.notch_shape is not None) or (
            other.notch_shape is not None and self.notch_shape is None
        ):
            diff_list.append(name + ".notch_shape None mismatch")
        elif self.notch_shape is not None:
            diff_list.extend(
                self.notch_shape.compare(
                    other.notch_shape,
                    name=name + ".notch_shape",
                    ignore_list=ignore_list,
                    is_add_value=is_add_value,
                )
            )
        if (
            other._position is not None
            and self._position is not None
            and isnan(other._position)
            and isnan(self._position)
        ):
            pass
        elif other._position != self._position:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._position)
                    + ", other="
                    + str(other._position)
                    + ")"
                )
                diff_list.append(name + ".position" + val_str)
            else:
                diff_list.append(name + ".position")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Hole
        S += super(VentilationNotchW60, self).__sizeof__()
        S += getsizeof(self.notch_shape)
        S += getsizeof(self.position)
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

        # Get the properties inherited from Hole
        VentilationNotchW60_dict = super(VentilationNotchW60, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        if self.notch_shape is None:
            VentilationNotchW60_dict["notch_shape"] = None
        else:
            VentilationNotchW60_dict["notch_shape"] = self.notch_shape.as_dict(
                type_handle_ndarray=type_handle_ndarray,
                keep_function=keep_function,
                **kwargs
            )
        VentilationNotchW60_dict["position"] = self.position
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        VentilationNotchW60_dict["__class__"] = "VentilationNotchW60"
        return VentilationNotchW60_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        if self.notch_shape is None:
            notch_shape_val = None
        else:
            notch_shape_val = self.notch_shape.copy()
        position_val = self.position
        Zh_val = self.Zh
        if self.mat_void is None:
            mat_void_val = None
        else:
            mat_void_val = self.mat_void.copy()
        if self.magnetization_dict_offset is None:
            magnetization_dict_offset_val = None
        else:
            magnetization_dict_offset_val = self.magnetization_dict_offset.copy()
        Alpha0_val = self.Alpha0
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            notch_shape=notch_shape_val,
            position=position_val,
            Zh=Zh_val,
            mat_void=mat_void_val,
            magnetization_dict_offset=magnetization_dict_offset_val,
            Alpha0=Alpha0_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.notch_shape is not None:
            self.notch_shape._set_None()
        self.position = None
        # Set to None the properties inherited from Hole
        super(VentilationNotchW60, self)._set_None()

    def _get_notch_shape(self):
        """getter of notch_shape"""
        return self._notch_shape

    def _set_notch_shape(self, value):
        """setter of notch_shape"""
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
                "pyleecan.Classes", value.get("__class__"), "notch_shape"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            Slot = import_class("pyleecan.Classes", "Slot", "notch_shape")
            value = Slot()
        check_var("notch_shape", value, "Slot")
        self._notch_shape = value

        if self._notch_shape is not None:
            self._notch_shape.parent = self

    notch_shape = property(
        fget=_get_notch_shape,
        fset=_set_notch_shape,
        doc=u"""Shape of the notch to add on the tooth

        :Type: Slot
        """,
    )

    def _get_position(self):
        """getter of position"""
        return self._position

    def _set_position(self, value):
        """setter of position"""
        check_var("position", value, "float", Vmin=0, Vmax=1)
        self._position = value

    position = property(
        fget=_get_position,
        fset=_set_position,
        doc=u"""Position of the slot [0=Begin of arc, 1=end of arc]

        :Type: float
        :min: 0
        :max: 1
        """,
    )
