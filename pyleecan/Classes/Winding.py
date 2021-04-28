# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Machine/Winding.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Machine/Winding
"""

from os import linesep
from sys import getsizeof
from logging import getLogger
from ._check import set_array, check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from ._frozen import FrozenClass

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Machine.Winding.comp_Ncspc import comp_Ncspc
except ImportError as error:
    comp_Ncspc = error

try:
    from ..Methods.Machine.Winding.comp_Ntsp import comp_Ntsp
except ImportError as error:
    comp_Ntsp = error

try:
    from ..Methods.Machine.Winding.comp_phasor_angle import comp_phasor_angle
except ImportError as error:
    comp_phasor_angle = error

try:
    from ..Methods.Machine.Winding.comp_winding_factor import comp_winding_factor
except ImportError as error:
    comp_winding_factor = error

try:
    from ..Methods.Machine.Winding.comp_length_endwinding import comp_length_endwinding
except ImportError as error:
    comp_length_endwinding = error

try:
    from ..Methods.Machine.Winding.comp_connection_mat import comp_connection_mat
except ImportError as error:
    comp_connection_mat = error

try:
    from ..Methods.Machine.Winding.get_dim_wind import get_dim_wind
except ImportError as error:
    get_dim_wind = error


from numpy import array, array_equal
from ._check import InitUnKnowClassError
from .Conductor import Conductor


class Winding(FrozenClass):
    """Winding class generating connection matrix using Star of slots method (coupling with SWAT-EM)"""

    VERSION = 1
    NAME = "Star of slots"

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Machine.Winding.comp_Ncspc
    if isinstance(comp_Ncspc, ImportError):
        comp_Ncspc = property(
            fget=lambda x: raise_(
                ImportError("Can't use Winding method comp_Ncspc: " + str(comp_Ncspc))
            )
        )
    else:
        comp_Ncspc = comp_Ncspc
    # cf Methods.Machine.Winding.comp_Ntsp
    if isinstance(comp_Ntsp, ImportError):
        comp_Ntsp = property(
            fget=lambda x: raise_(
                ImportError("Can't use Winding method comp_Ntsp: " + str(comp_Ntsp))
            )
        )
    else:
        comp_Ntsp = comp_Ntsp
    # cf Methods.Machine.Winding.comp_phasor_angle
    if isinstance(comp_phasor_angle, ImportError):
        comp_phasor_angle = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method comp_phasor_angle: "
                    + str(comp_phasor_angle)
                )
            )
        )
    else:
        comp_phasor_angle = comp_phasor_angle
    # cf Methods.Machine.Winding.comp_winding_factor
    if isinstance(comp_winding_factor, ImportError):
        comp_winding_factor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method comp_winding_factor: "
                    + str(comp_winding_factor)
                )
            )
        )
    else:
        comp_winding_factor = comp_winding_factor
    # cf Methods.Machine.Winding.comp_length_endwinding
    if isinstance(comp_length_endwinding, ImportError):
        comp_length_endwinding = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method comp_length_endwinding: "
                    + str(comp_length_endwinding)
                )
            )
        )
    else:
        comp_length_endwinding = comp_length_endwinding
    # cf Methods.Machine.Winding.comp_connection_mat
    if isinstance(comp_connection_mat, ImportError):
        comp_connection_mat = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method comp_connection_mat: "
                    + str(comp_connection_mat)
                )
            )
        )
    else:
        comp_connection_mat = comp_connection_mat
    # cf Methods.Machine.Winding.get_dim_wind
    if isinstance(get_dim_wind, ImportError):
        get_dim_wind = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use Winding method get_dim_wind: " + str(get_dim_wind)
                )
            )
        )
    else:
        get_dim_wind = get_dim_wind
    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        is_reverse_wind=False,
        Nslot_shift_wind=0,
        qs=3,
        Ntcoil=7,
        Npcp=2,
        type_connection=0,
        p=3,
        Lewout=0.015,
        conductor=-1,
        coil_pitch=0,
        wind_mat=None,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "is_reverse_wind" in list(init_dict.keys()):
                is_reverse_wind = init_dict["is_reverse_wind"]
            if "Nslot_shift_wind" in list(init_dict.keys()):
                Nslot_shift_wind = init_dict["Nslot_shift_wind"]
            if "qs" in list(init_dict.keys()):
                qs = init_dict["qs"]
            if "Ntcoil" in list(init_dict.keys()):
                Ntcoil = init_dict["Ntcoil"]
            if "Npcp" in list(init_dict.keys()):
                Npcp = init_dict["Npcp"]
            if "type_connection" in list(init_dict.keys()):
                type_connection = init_dict["type_connection"]
            if "p" in list(init_dict.keys()):
                p = init_dict["p"]
            if "Lewout" in list(init_dict.keys()):
                Lewout = init_dict["Lewout"]
            if "conductor" in list(init_dict.keys()):
                conductor = init_dict["conductor"]
            if "coil_pitch" in list(init_dict.keys()):
                coil_pitch = init_dict["coil_pitch"]
            if "wind_mat" in list(init_dict.keys()):
                wind_mat = init_dict["wind_mat"]
        # Set the properties (value check and convertion are done in setter)
        self.parent = None
        self.is_reverse_wind = is_reverse_wind
        self.Nslot_shift_wind = Nslot_shift_wind
        self.qs = qs
        self.Ntcoil = Ntcoil
        self.Npcp = Npcp
        self.type_connection = type_connection
        self.p = p
        self.Lewout = Lewout
        self.conductor = conductor
        self.coil_pitch = coil_pitch
        self.wind_mat = wind_mat

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        Winding_str = ""
        if self.parent is None:
            Winding_str += "parent = None " + linesep
        else:
            Winding_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Winding_str += "is_reverse_wind = " + str(self.is_reverse_wind) + linesep
        Winding_str += "Nslot_shift_wind = " + str(self.Nslot_shift_wind) + linesep
        Winding_str += "qs = " + str(self.qs) + linesep
        Winding_str += "Ntcoil = " + str(self.Ntcoil) + linesep
        Winding_str += "Npcp = " + str(self.Npcp) + linesep
        Winding_str += "type_connection = " + str(self.type_connection) + linesep
        Winding_str += "p = " + str(self.p) + linesep
        Winding_str += "Lewout = " + str(self.Lewout) + linesep
        if self.conductor is not None:
            tmp = self.conductor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            Winding_str += "conductor = " + tmp
        else:
            Winding_str += "conductor = None" + linesep + linesep
        Winding_str += "coil_pitch = " + str(self.coil_pitch) + linesep
        Winding_str += (
            "wind_mat = "
            + linesep
            + str(self.wind_mat).replace(linesep, linesep + "\t")
            + linesep
            + linesep
        )
        return Winding_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.is_reverse_wind != self.is_reverse_wind:
            return False
        if other.Nslot_shift_wind != self.Nslot_shift_wind:
            return False
        if other.qs != self.qs:
            return False
        if other.Ntcoil != self.Ntcoil:
            return False
        if other.Npcp != self.Npcp:
            return False
        if other.type_connection != self.type_connection:
            return False
        if other.p != self.p:
            return False
        if other.Lewout != self.Lewout:
            return False
        if other.conductor != self.conductor:
            return False
        if other.coil_pitch != self.coil_pitch:
            return False
        if not array_equal(other.wind_mat, self.wind_mat):
            return False
        return True

    def compare(self, other, name="self"):
        """Compare two objects and return list of differences"""

        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()
        if other._is_reverse_wind != self._is_reverse_wind:
            diff_list.append(name + ".is_reverse_wind")
        if other._Nslot_shift_wind != self._Nslot_shift_wind:
            diff_list.append(name + ".Nslot_shift_wind")
        if other._qs != self._qs:
            diff_list.append(name + ".qs")
        if other._Ntcoil != self._Ntcoil:
            diff_list.append(name + ".Ntcoil")
        if other._Npcp != self._Npcp:
            diff_list.append(name + ".Npcp")
        if other._type_connection != self._type_connection:
            diff_list.append(name + ".type_connection")
        if other._p != self._p:
            diff_list.append(name + ".p")
        if other._Lewout != self._Lewout:
            diff_list.append(name + ".Lewout")
        if (other.conductor is None and self.conductor is not None) or (
            other.conductor is not None and self.conductor is None
        ):
            diff_list.append(name + ".conductor None mismatch")
        elif self.conductor is not None:
            diff_list.extend(
                self.conductor.compare(other.conductor, name=name + ".conductor")
            )
        if other._coil_pitch != self._coil_pitch:
            diff_list.append(name + ".coil_pitch")
        if not array_equal(other.wind_mat, self.wind_mat):
            diff_list.append(name + ".wind_mat")
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object
        S += getsizeof(self.is_reverse_wind)
        S += getsizeof(self.Nslot_shift_wind)
        S += getsizeof(self.qs)
        S += getsizeof(self.Ntcoil)
        S += getsizeof(self.Npcp)
        S += getsizeof(self.type_connection)
        S += getsizeof(self.p)
        S += getsizeof(self.Lewout)
        S += getsizeof(self.conductor)
        S += getsizeof(self.coil_pitch)
        S += getsizeof(self.wind_mat)
        return S

    def as_dict(self, **kwargs):
        """
        Convert this object in a json serializable dict (can be use in __init__).
        Optional keyword input parameter is for internal use only
        and may prevent json serializability.
        """

        Winding_dict = dict()
        Winding_dict["is_reverse_wind"] = self.is_reverse_wind
        Winding_dict["Nslot_shift_wind"] = self.Nslot_shift_wind
        Winding_dict["qs"] = self.qs
        Winding_dict["Ntcoil"] = self.Ntcoil
        Winding_dict["Npcp"] = self.Npcp
        Winding_dict["type_connection"] = self.type_connection
        Winding_dict["p"] = self.p
        Winding_dict["Lewout"] = self.Lewout
        if self.conductor is None:
            Winding_dict["conductor"] = None
        else:
            Winding_dict["conductor"] = self.conductor.as_dict(**kwargs)
        Winding_dict["coil_pitch"] = self.coil_pitch
        if self.wind_mat is None:
            Winding_dict["wind_mat"] = None
        else:
            Winding_dict["wind_mat"] = self.wind_mat.tolist()
        # The class name is added to the dict for deserialisation purpose
        Winding_dict["__class__"] = "Winding"
        return Winding_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.is_reverse_wind = None
        self.Nslot_shift_wind = None
        self.qs = None
        self.Ntcoil = None
        self.Npcp = None
        self.type_connection = None
        self.p = None
        self.Lewout = None
        if self.conductor is not None:
            self.conductor._set_None()
        self.coil_pitch = None
        self.wind_mat = None

    def _get_is_reverse_wind(self):
        """getter of is_reverse_wind"""
        return self._is_reverse_wind

    def _set_is_reverse_wind(self, value):
        """setter of is_reverse_wind"""
        check_var("is_reverse_wind", value, "bool")
        self._is_reverse_wind = value

    is_reverse_wind = property(
        fget=_get_is_reverse_wind,
        fset=_set_is_reverse_wind,
        doc=u"""1 to reverse the default winding algorithm along the airgap (c, b, a instead of a, b, c along the trigonometric direction)

        :Type: bool
        """,
    )

    def _get_Nslot_shift_wind(self):
        """getter of Nslot_shift_wind"""
        return self._Nslot_shift_wind

    def _set_Nslot_shift_wind(self, value):
        """setter of Nslot_shift_wind"""
        check_var("Nslot_shift_wind", value, "int")
        self._Nslot_shift_wind = value

    Nslot_shift_wind = property(
        fget=_get_Nslot_shift_wind,
        fset=_set_Nslot_shift_wind,
        doc=u"""0 not to change the stator winding connection matrix built by pyleecan number of slots to shift the coils obtained with pyleecan winding algorithm (a, b, c becomes b, c, a with Nslot_shift_wind1=1)

        :Type: int
        """,
    )

    def _get_qs(self):
        """getter of qs"""
        return self._qs

    def _set_qs(self, value):
        """setter of qs"""
        check_var("qs", value, "int", Vmin=0, Vmax=100)
        self._qs = value

    qs = property(
        fget=_get_qs,
        fset=_set_qs,
        doc=u"""number of phases 

        :Type: int
        :min: 0
        :max: 100
        """,
    )

    def _get_Ntcoil(self):
        """getter of Ntcoil"""
        return self._Ntcoil

    def _set_Ntcoil(self, value):
        """setter of Ntcoil"""
        check_var("Ntcoil", value, "int", Vmin=1, Vmax=1000)
        self._Ntcoil = value

    Ntcoil = property(
        fget=_get_Ntcoil,
        fset=_set_Ntcoil,
        doc=u"""number of turns per coil

        :Type: int
        :min: 1
        :max: 1000
        """,
    )

    def _get_Npcp(self):
        """getter of Npcp"""
        return self._Npcp

    def _set_Npcp(self, value):
        """setter of Npcp"""
        check_var("Npcp", value, "int", Vmin=1, Vmax=1000)
        self._Npcp = value

    Npcp = property(
        fget=_get_Npcp,
        fset=_set_Npcp,
        doc=u"""number of parallel circuits per phase (maximum 2p)

        :Type: int
        :min: 1
        :max: 1000
        """,
    )

    def _get_type_connection(self):
        """getter of type_connection"""
        return self._type_connection

    def _set_type_connection(self, value):
        """setter of type_connection"""
        check_var("type_connection", value, "int", Vmin=0, Vmax=1)
        self._type_connection = value

    type_connection = property(
        fget=_get_type_connection,
        fset=_set_type_connection,
        doc=u"""Winding connection : 0 star (Y), 1 triangle (delta)

        :Type: int
        :min: 0
        :max: 1
        """,
    )

    def _get_p(self):
        """getter of p"""
        return self._p

    def _set_p(self, value):
        """setter of p"""
        check_var("p", value, "int", Vmin=1, Vmax=100)
        self._p = value

    p = property(
        fget=_get_p,
        fset=_set_p,
        doc=u"""pole pairs number

        :Type: int
        :min: 1
        :max: 100
        """,
    )

    def _get_Lewout(self):
        """getter of Lewout"""
        return self._Lewout

    def _set_Lewout(self, value):
        """setter of Lewout"""
        check_var("Lewout", value, "float", Vmin=0, Vmax=100)
        self._Lewout = value

    Lewout = property(
        fget=_get_Lewout,
        fset=_set_Lewout,
        doc=u"""straight length of the conductors outside the lamination before the curved part of winding overhang [m] - can be negative to tune the average turn length 

        :Type: float
        :min: 0
        :max: 100
        """,
    )

    def _get_conductor(self):
        """getter of conductor"""
        return self._conductor

    def _set_conductor(self, value):
        """setter of conductor"""
        if isinstance(value, str):  # Load from file
            value = load_init_dict(value)[1]
        if isinstance(value, dict) and "__class__" in value:
            class_obj = import_class(
                "pyleecan.Classes", value.get("__class__"), "conductor"
            )
            value = class_obj(init_dict=value)
        elif type(value) is int and value == -1:  # Default constructor
            value = Conductor()
        check_var("conductor", value, "Conductor")
        self._conductor = value

        if self._conductor is not None:
            self._conductor.parent = self

    conductor = property(
        fget=_get_conductor,
        fset=_set_conductor,
        doc=u"""Winding's conductor

        :Type: Conductor
        """,
    )

    def _get_coil_pitch(self):
        """getter of coil_pitch"""
        return self._coil_pitch

    def _set_coil_pitch(self, value):
        """setter of coil_pitch"""
        check_var("coil_pitch", value, "int")
        self._coil_pitch = value

    coil_pitch = property(
        fget=_get_coil_pitch,
        fset=_set_coil_pitch,
        doc=u"""Coil pitch (or coil span)

        :Type: int
        """,
    )

    def _get_wind_mat(self):
        """getter of wind_mat"""
        return self._wind_mat

    def _set_wind_mat(self, value):
        """setter of wind_mat"""
        if type(value) is int and value == -1:
            value = array([])
        elif type(value) is list:
            try:
                value = array(value)
            except:
                pass
        check_var("wind_mat", value, "ndarray")
        self._wind_mat = value

    wind_mat = property(
        fget=_get_wind_mat,
        fset=_set_wind_mat,
        doc=u"""Winding matrix calculated with Star of slots (from SWAT_EM package)

        :Type: ndarray
        """,
    )
