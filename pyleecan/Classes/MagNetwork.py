# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Simulation/MagNetwork.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Simulation/MagNetwork
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
from .Magnetics import Magnetics

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.MagNetwork.geometry_motor import geometry_motor
except ImportError as error:
    geometry_motor = error

try:
    from ..Methods.Simulation.MagNetwork.pre_processing.init_cell import init_cell
except ImportError as error:
    init_cell = error

try:
    from ..Methods.Simulation.MagNetwork.pre_processing.init_mesh_BC import init_mesh_BC
except ImportError as error:
    init_mesh_BC = error

try:
    from ..Methods.Simulation.MagNetwork.pre_processing.init_point import init_point
except ImportError as error:
    init_point = error

try:
    from ..Methods.Simulation.MagNetwork.pre_processing.init_reluc import init_reluc
except ImportError as error:
    init_reluc = error

try:
    from ..Methods.Simulation.MagNetwork.pre_processing.numeroting_unknows import (
        numeroting_unknows,
    )
except ImportError as error:
    numeroting_unknows = error

try:
    from ..Methods.Simulation.MagNetwork.pre_processing.save_mesh import save_mesh
except ImportError as error:
    save_mesh = error

try:
    from ..Methods.Simulation.MagNetwork.pre_processing.init_mesh import init_mesh
except ImportError as error:
    init_mesh = error

try:
    from ..Methods.Simulation.MagNetwork.assembler.assembly import assembly
except ImportError as error:
    assembly = error

try:
    from ..Methods.Simulation.MagNetwork.assembler.assembly_one_area import (
        assembly_one_area,
    )
except ImportError as error:
    assembly_one_area = error

try:
    from ..Methods.Simulation.MagNetwork.assembler.right_member_assembly import (
        right_member_assembly,
    )
except ImportError as error:
    right_member_assembly = error

try:
    from ..Methods.Simulation.MagNetwork.post_processing.add_BC_to_Phi import (
        add_BC_to_Phi,
    )
except ImportError as error:
    add_BC_to_Phi = error

try:
    from ..Methods.Simulation.MagNetwork.post_processing.compute_B import compute_B
except ImportError as error:
    compute_B = error

try:
    from ..Methods.Simulation.MagNetwork.solver_linear_model import solver_linear_model
except ImportError as error:
    solver_linear_model = error

try:
    from ..Methods.Simulation.MagNetwork.run_radial import run_radial
except ImportError as error:
    run_radial = error

try:
    from ..Methods.Simulation.MagNetwork.plot.Plot_B import Plot_B
except ImportError as error:
    Plot_B = error

try:
    from ..Methods.Simulation.MagNetwork.plot.view_contour_flux import view_contour_flux
except ImportError as error:
    view_contour_flux = error

try:
    from ..Methods.Simulation.MagNetwork.plot.view_contour_flux2 import (
        view_contour_flux2,
    )
except ImportError as error:
    view_contour_flux2 = error

try:
    from ..Methods.Simulation.MagNetwork.comp_flux_airgap_local import (
        comp_flux_airgap_local,
    )
except ImportError as error:
    comp_flux_airgap_local = error

try:
    from ..Methods.Simulation.MagNetwork.comp_flux_airgap import comp_flux_airgap
except ImportError as error:
    comp_flux_airgap = error

try:
    from ..Methods.Simulation.MagNetwork.comp_axes import comp_axes
except ImportError as error:
    comp_axes = error

try:
    from ..Methods.Simulation.MagNetwork.run_cartesian import run_cartesian
except ImportError as error:
    run_cartesian = error

try:
    from ..Methods.Simulation.MagNetwork.run_non_linear import run_non_linear
except ImportError as error:
    run_non_linear = error

try:
    from ..Methods.Simulation.MagNetwork.solver_non_linear_model import (
        solver_non_linear_model,
    )
except ImportError as error:
    solver_non_linear_model = error

try:
    from ..Methods.Simulation.MagNetwork.cartesianmeshclass_pyleecan import (
        cartesianmeshclass_pyleecan,
    )
except ImportError as error:
    cartesianmeshclass_pyleecan = error

try:
    from ..Methods.Simulation.MagNetwork.geometry_linear_motor_separetion import (
        geometry_linear_motor_separetion,
    )
except ImportError as error:
    geometry_linear_motor_separetion = error


from numpy import isnan
from ._check import InitUnKnowClassError


class MagNetwork(Magnetics):
    """Abstract class to solve the electric machines using the reluctance network"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Simulation.MagNetwork.geometry_motor
    if isinstance(geometry_motor, ImportError):
        geometry_motor = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method geometry_motor: " + str(geometry_motor)
                )
            )
        )
    else:
        geometry_motor = geometry_motor
    # cf Methods.Simulation.MagNetwork.pre_processing.init_cell
    if isinstance(init_cell, ImportError):
        init_cell = property(
            fget=lambda x: raise_(
                ImportError("Can't use MagNetwork method init_cell: " + str(init_cell))
            )
        )
    else:
        init_cell = init_cell
    # cf Methods.Simulation.MagNetwork.pre_processing.init_mesh_BC
    if isinstance(init_mesh_BC, ImportError):
        init_mesh_BC = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method init_mesh_BC: " + str(init_mesh_BC)
                )
            )
        )
    else:
        init_mesh_BC = init_mesh_BC
    # cf Methods.Simulation.MagNetwork.pre_processing.init_point
    if isinstance(init_point, ImportError):
        init_point = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method init_point: " + str(init_point)
                )
            )
        )
    else:
        init_point = init_point
    # cf Methods.Simulation.MagNetwork.pre_processing.init_reluc
    if isinstance(init_reluc, ImportError):
        init_reluc = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method init_reluc: " + str(init_reluc)
                )
            )
        )
    else:
        init_reluc = init_reluc
    # cf Methods.Simulation.MagNetwork.pre_processing.numeroting_unknows
    if isinstance(numeroting_unknows, ImportError):
        numeroting_unknows = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method numeroting_unknows: "
                    + str(numeroting_unknows)
                )
            )
        )
    else:
        numeroting_unknows = numeroting_unknows
    # cf Methods.Simulation.MagNetwork.pre_processing.save_mesh
    if isinstance(save_mesh, ImportError):
        save_mesh = property(
            fget=lambda x: raise_(
                ImportError("Can't use MagNetwork method save_mesh: " + str(save_mesh))
            )
        )
    else:
        save_mesh = save_mesh
    # cf Methods.Simulation.MagNetwork.pre_processing.init_mesh
    if isinstance(init_mesh, ImportError):
        init_mesh = property(
            fget=lambda x: raise_(
                ImportError("Can't use MagNetwork method init_mesh: " + str(init_mesh))
            )
        )
    else:
        init_mesh = init_mesh
    # cf Methods.Simulation.MagNetwork.assembler.assembly
    if isinstance(assembly, ImportError):
        assembly = property(
            fget=lambda x: raise_(
                ImportError("Can't use MagNetwork method assembly: " + str(assembly))
            )
        )
    else:
        assembly = assembly
    # cf Methods.Simulation.MagNetwork.assembler.assembly_one_area
    if isinstance(assembly_one_area, ImportError):
        assembly_one_area = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method assembly_one_area: "
                    + str(assembly_one_area)
                )
            )
        )
    else:
        assembly_one_area = assembly_one_area
    # cf Methods.Simulation.MagNetwork.assembler.right_member_assembly
    if isinstance(right_member_assembly, ImportError):
        right_member_assembly = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method right_member_assembly: "
                    + str(right_member_assembly)
                )
            )
        )
    else:
        right_member_assembly = right_member_assembly
    # cf Methods.Simulation.MagNetwork.post_processing.add_BC_to_Phi
    if isinstance(add_BC_to_Phi, ImportError):
        add_BC_to_Phi = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method add_BC_to_Phi: " + str(add_BC_to_Phi)
                )
            )
        )
    else:
        add_BC_to_Phi = add_BC_to_Phi
    # cf Methods.Simulation.MagNetwork.post_processing.compute_B
    if isinstance(compute_B, ImportError):
        compute_B = property(
            fget=lambda x: raise_(
                ImportError("Can't use MagNetwork method compute_B: " + str(compute_B))
            )
        )
    else:
        compute_B = compute_B
    # cf Methods.Simulation.MagNetwork.solver_linear_model
    if isinstance(solver_linear_model, ImportError):
        solver_linear_model = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method solver_linear_model: "
                    + str(solver_linear_model)
                )
            )
        )
    else:
        solver_linear_model = solver_linear_model
    # cf Methods.Simulation.MagNetwork.run_radial
    if isinstance(run_radial, ImportError):
        run_radial = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method run_radial: " + str(run_radial)
                )
            )
        )
    else:
        run_radial = run_radial
    # cf Methods.Simulation.MagNetwork.plot.Plot_B
    if isinstance(Plot_B, ImportError):
        Plot_B = property(
            fget=lambda x: raise_(
                ImportError("Can't use MagNetwork method Plot_B: " + str(Plot_B))
            )
        )
    else:
        Plot_B = Plot_B
    # cf Methods.Simulation.MagNetwork.plot.view_contour_flux
    if isinstance(view_contour_flux, ImportError):
        view_contour_flux = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method view_contour_flux: "
                    + str(view_contour_flux)
                )
            )
        )
    else:
        view_contour_flux = view_contour_flux
    # cf Methods.Simulation.MagNetwork.plot.view_contour_flux2
    if isinstance(view_contour_flux2, ImportError):
        view_contour_flux2 = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method view_contour_flux2: "
                    + str(view_contour_flux2)
                )
            )
        )
    else:
        view_contour_flux2 = view_contour_flux2
    # cf Methods.Simulation.MagNetwork.comp_flux_airgap_local
    if isinstance(comp_flux_airgap_local, ImportError):
        comp_flux_airgap_local = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method comp_flux_airgap_local: "
                    + str(comp_flux_airgap_local)
                )
            )
        )
    else:
        comp_flux_airgap_local = comp_flux_airgap_local
    # cf Methods.Simulation.MagNetwork.comp_flux_airgap
    if isinstance(comp_flux_airgap, ImportError):
        comp_flux_airgap = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method comp_flux_airgap: "
                    + str(comp_flux_airgap)
                )
            )
        )
    else:
        comp_flux_airgap = comp_flux_airgap
    # cf Methods.Simulation.MagNetwork.comp_axes
    if isinstance(comp_axes, ImportError):
        comp_axes = property(
            fget=lambda x: raise_(
                ImportError("Can't use MagNetwork method comp_axes: " + str(comp_axes))
            )
        )
    else:
        comp_axes = comp_axes
    # cf Methods.Simulation.MagNetwork.run_cartesian
    if isinstance(run_cartesian, ImportError):
        run_cartesian = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method run_cartesian: " + str(run_cartesian)
                )
            )
        )
    else:
        run_cartesian = run_cartesian
    # cf Methods.Simulation.MagNetwork.run_non_linear
    if isinstance(run_non_linear, ImportError):
        run_non_linear = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method run_non_linear: " + str(run_non_linear)
                )
            )
        )
    else:
        run_non_linear = run_non_linear
    # cf Methods.Simulation.MagNetwork.solver_non_linear_model
    if isinstance(solver_non_linear_model, ImportError):
        solver_non_linear_model = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method solver_non_linear_model: "
                    + str(solver_non_linear_model)
                )
            )
        )
    else:
        solver_non_linear_model = solver_non_linear_model
    # cf Methods.Simulation.MagNetwork.cartesianmeshclass_pyleecan
    if isinstance(cartesianmeshclass_pyleecan, ImportError):
        cartesianmeshclass_pyleecan = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method cartesianmeshclass_pyleecan: "
                    + str(cartesianmeshclass_pyleecan)
                )
            )
        )
    else:
        cartesianmeshclass_pyleecan = cartesianmeshclass_pyleecan
    # cf Methods.Simulation.MagNetwork.geometry_linear_motor_separetion
    if isinstance(geometry_linear_motor_separetion, ImportError):
        geometry_linear_motor_separetion = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use MagNetwork method geometry_linear_motor_separetion: "
                    + str(geometry_linear_motor_separetion)
                )
            )
        )
    else:
        geometry_linear_motor_separetion = geometry_linear_motor_separetion
    # generic save method is available in all object
    save = save
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        type_model=1,
        type_coord_sys=2,
        Kmesh_fineness=1,
        rotor_shift=8,
        stator_yoke_elements_r=2,
        airgap_elements_r=2,
        rotor_yoke_elements_r=2,
        stator_isthmus_elements_r=2,
        stator_tooth_elements_r=2,
        magnet_elements_r=2,
        is_remove_slotS=False,
        is_remove_slotR=False,
        is_remove_ventS=False,
        is_remove_ventR=False,
        is_mmfs=True,
        is_mmfr=True,
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_t=False,
        is_periodicity_a=False,
        angle_stator_shift=0,
        angle_rotor_shift=0,
        logger_name="Pyleecan.Magnetics",
        Slice_enforced=None,
        Nslices_enforced=None,
        type_distribution_enforced=None,
        is_current_harm=True,
        T_mag=20,
        is_periodicity_rotor=False,
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
            if "type_model" in list(init_dict.keys()):
                type_model = init_dict["type_model"]
            if "type_coord_sys" in list(init_dict.keys()):
                type_coord_sys = init_dict["type_coord_sys"]
            if "Kmesh_fineness" in list(init_dict.keys()):
                Kmesh_fineness = init_dict["Kmesh_fineness"]
            if "rotor_shift" in list(init_dict.keys()):
                rotor_shift = init_dict["rotor_shift"]
            if "stator_yoke_elements_r" in list(init_dict.keys()):
                stator_yoke_elements_r = init_dict["stator_yoke_elements_r"]
            if "airgap_elements_r" in list(init_dict.keys()):
                airgap_elements_r = init_dict["airgap_elements_r"]
            if "rotor_yoke_elements_r" in list(init_dict.keys()):
                rotor_yoke_elements_r = init_dict["rotor_yoke_elements_r"]
            if "stator_isthmus_elements_r" in list(init_dict.keys()):
                stator_isthmus_elements_r = init_dict["stator_isthmus_elements_r"]
            if "stator_tooth_elements_r" in list(init_dict.keys()):
                stator_tooth_elements_r = init_dict["stator_tooth_elements_r"]
            if "magnet_elements_r" in list(init_dict.keys()):
                magnet_elements_r = init_dict["magnet_elements_r"]
            if "is_remove_slotS" in list(init_dict.keys()):
                is_remove_slotS = init_dict["is_remove_slotS"]
            if "is_remove_slotR" in list(init_dict.keys()):
                is_remove_slotR = init_dict["is_remove_slotR"]
            if "is_remove_ventS" in list(init_dict.keys()):
                is_remove_ventS = init_dict["is_remove_ventS"]
            if "is_remove_ventR" in list(init_dict.keys()):
                is_remove_ventR = init_dict["is_remove_ventR"]
            if "is_mmfs" in list(init_dict.keys()):
                is_mmfs = init_dict["is_mmfs"]
            if "is_mmfr" in list(init_dict.keys()):
                is_mmfr = init_dict["is_mmfr"]
            if "type_BH_stator" in list(init_dict.keys()):
                type_BH_stator = init_dict["type_BH_stator"]
            if "type_BH_rotor" in list(init_dict.keys()):
                type_BH_rotor = init_dict["type_BH_rotor"]
            if "is_periodicity_t" in list(init_dict.keys()):
                is_periodicity_t = init_dict["is_periodicity_t"]
            if "is_periodicity_a" in list(init_dict.keys()):
                is_periodicity_a = init_dict["is_periodicity_a"]
            if "angle_stator_shift" in list(init_dict.keys()):
                angle_stator_shift = init_dict["angle_stator_shift"]
            if "angle_rotor_shift" in list(init_dict.keys()):
                angle_rotor_shift = init_dict["angle_rotor_shift"]
            if "logger_name" in list(init_dict.keys()):
                logger_name = init_dict["logger_name"]
            if "Slice_enforced" in list(init_dict.keys()):
                Slice_enforced = init_dict["Slice_enforced"]
            if "Nslices_enforced" in list(init_dict.keys()):
                Nslices_enforced = init_dict["Nslices_enforced"]
            if "type_distribution_enforced" in list(init_dict.keys()):
                type_distribution_enforced = init_dict["type_distribution_enforced"]
            if "is_current_harm" in list(init_dict.keys()):
                is_current_harm = init_dict["is_current_harm"]
            if "T_mag" in list(init_dict.keys()):
                T_mag = init_dict["T_mag"]
            if "is_periodicity_rotor" in list(init_dict.keys()):
                is_periodicity_rotor = init_dict["is_periodicity_rotor"]
        # Set the properties (value check and convertion are done in setter)
        self.type_model = type_model
        self.type_coord_sys = type_coord_sys
        self.Kmesh_fineness = Kmesh_fineness
        self.rotor_shift = rotor_shift
        self.stator_yoke_elements_r = stator_yoke_elements_r
        self.airgap_elements_r = airgap_elements_r
        self.rotor_yoke_elements_r = rotor_yoke_elements_r
        self.stator_isthmus_elements_r = stator_isthmus_elements_r
        self.stator_tooth_elements_r = stator_tooth_elements_r
        self.magnet_elements_r = magnet_elements_r
        # Call Magnetics init
        super(MagNetwork, self).__init__(
            is_remove_slotS=is_remove_slotS,
            is_remove_slotR=is_remove_slotR,
            is_remove_ventS=is_remove_ventS,
            is_remove_ventR=is_remove_ventR,
            is_mmfs=is_mmfs,
            is_mmfr=is_mmfr,
            type_BH_stator=type_BH_stator,
            type_BH_rotor=type_BH_rotor,
            is_periodicity_t=is_periodicity_t,
            is_periodicity_a=is_periodicity_a,
            angle_stator_shift=angle_stator_shift,
            angle_rotor_shift=angle_rotor_shift,
            logger_name=logger_name,
            Slice_enforced=Slice_enforced,
            Nslices_enforced=Nslices_enforced,
            type_distribution_enforced=type_distribution_enforced,
            is_current_harm=is_current_harm,
            T_mag=T_mag,
            is_periodicity_rotor=is_periodicity_rotor,
        )
        # The class is frozen (in Magnetics init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        MagNetwork_str = ""
        # Get the properties inherited from Magnetics
        MagNetwork_str += super(MagNetwork, self).__str__()
        MagNetwork_str += "type_model = " + str(self.type_model) + linesep
        MagNetwork_str += "type_coord_sys = " + str(self.type_coord_sys) + linesep
        MagNetwork_str += "Kmesh_fineness = " + str(self.Kmesh_fineness) + linesep
        MagNetwork_str += "rotor_shift = " + str(self.rotor_shift) + linesep
        MagNetwork_str += (
            "stator_yoke_elements_r = " + str(self.stator_yoke_elements_r) + linesep
        )
        MagNetwork_str += "airgap_elements_r = " + str(self.airgap_elements_r) + linesep
        MagNetwork_str += (
            "rotor_yoke_elements_r = " + str(self.rotor_yoke_elements_r) + linesep
        )
        MagNetwork_str += (
            "stator_isthmus_elements_r = "
            + str(self.stator_isthmus_elements_r)
            + linesep
        )
        MagNetwork_str += (
            "stator_tooth_elements_r = " + str(self.stator_tooth_elements_r) + linesep
        )
        MagNetwork_str += "magnet_elements_r = " + str(self.magnet_elements_r) + linesep
        return MagNetwork_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Magnetics
        if not super(MagNetwork, self).__eq__(other):
            return False
        if other.type_model != self.type_model:
            return False
        if other.type_coord_sys != self.type_coord_sys:
            return False
        if other.Kmesh_fineness != self.Kmesh_fineness:
            return False
        if other.rotor_shift != self.rotor_shift:
            return False
        if other.stator_yoke_elements_r != self.stator_yoke_elements_r:
            return False
        if other.airgap_elements_r != self.airgap_elements_r:
            return False
        if other.rotor_yoke_elements_r != self.rotor_yoke_elements_r:
            return False
        if other.stator_isthmus_elements_r != self.stator_isthmus_elements_r:
            return False
        if other.stator_tooth_elements_r != self.stator_tooth_elements_r:
            return False
        if other.magnet_elements_r != self.magnet_elements_r:
            return False
        return True

    def compare(self, other, name="self", ignore_list=None, is_add_value=False):
        """Compare two objects and return list of differences"""

        if ignore_list is None:
            ignore_list = list()
        if type(other) != type(self):
            return ["type(" + name + ")"]
        diff_list = list()

        # Check the properties inherited from Magnetics
        diff_list.extend(
            super(MagNetwork, self).compare(
                other, name=name, ignore_list=ignore_list, is_add_value=is_add_value
            )
        )
        if other._type_model != self._type_model:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_model)
                    + ", other="
                    + str(other._type_model)
                    + ")"
                )
                diff_list.append(name + ".type_model" + val_str)
            else:
                diff_list.append(name + ".type_model")
        if other._type_coord_sys != self._type_coord_sys:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._type_coord_sys)
                    + ", other="
                    + str(other._type_coord_sys)
                    + ")"
                )
                diff_list.append(name + ".type_coord_sys" + val_str)
            else:
                diff_list.append(name + ".type_coord_sys")
        if other._Kmesh_fineness != self._Kmesh_fineness:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._Kmesh_fineness)
                    + ", other="
                    + str(other._Kmesh_fineness)
                    + ")"
                )
                diff_list.append(name + ".Kmesh_fineness" + val_str)
            else:
                diff_list.append(name + ".Kmesh_fineness")
        if other._rotor_shift != self._rotor_shift:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._rotor_shift)
                    + ", other="
                    + str(other._rotor_shift)
                    + ")"
                )
                diff_list.append(name + ".rotor_shift" + val_str)
            else:
                diff_list.append(name + ".rotor_shift")
        if other._stator_yoke_elements_r != self._stator_yoke_elements_r:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._stator_yoke_elements_r)
                    + ", other="
                    + str(other._stator_yoke_elements_r)
                    + ")"
                )
                diff_list.append(name + ".stator_yoke_elements_r" + val_str)
            else:
                diff_list.append(name + ".stator_yoke_elements_r")
        if other._airgap_elements_r != self._airgap_elements_r:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._airgap_elements_r)
                    + ", other="
                    + str(other._airgap_elements_r)
                    + ")"
                )
                diff_list.append(name + ".airgap_elements_r" + val_str)
            else:
                diff_list.append(name + ".airgap_elements_r")
        if other._rotor_yoke_elements_r != self._rotor_yoke_elements_r:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._rotor_yoke_elements_r)
                    + ", other="
                    + str(other._rotor_yoke_elements_r)
                    + ")"
                )
                diff_list.append(name + ".rotor_yoke_elements_r" + val_str)
            else:
                diff_list.append(name + ".rotor_yoke_elements_r")
        if other._stator_isthmus_elements_r != self._stator_isthmus_elements_r:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._stator_isthmus_elements_r)
                    + ", other="
                    + str(other._stator_isthmus_elements_r)
                    + ")"
                )
                diff_list.append(name + ".stator_isthmus_elements_r" + val_str)
            else:
                diff_list.append(name + ".stator_isthmus_elements_r")
        if other._stator_tooth_elements_r != self._stator_tooth_elements_r:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._stator_tooth_elements_r)
                    + ", other="
                    + str(other._stator_tooth_elements_r)
                    + ")"
                )
                diff_list.append(name + ".stator_tooth_elements_r" + val_str)
            else:
                diff_list.append(name + ".stator_tooth_elements_r")
        if other._magnet_elements_r != self._magnet_elements_r:
            if is_add_value:
                val_str = (
                    " (self="
                    + str(self._magnet_elements_r)
                    + ", other="
                    + str(other._magnet_elements_r)
                    + ")"
                )
                diff_list.append(name + ".magnet_elements_r" + val_str)
            else:
                diff_list.append(name + ".magnet_elements_r")
        # Filter ignore differences
        diff_list = list(filter(lambda x: x not in ignore_list, diff_list))
        return diff_list

    def __sizeof__(self):
        """Return the size in memory of the object (including all subobject)"""

        S = 0  # Full size of the object

        # Get size of the properties inherited from Magnetics
        S += super(MagNetwork, self).__sizeof__()
        S += getsizeof(self.type_model)
        S += getsizeof(self.type_coord_sys)
        S += getsizeof(self.Kmesh_fineness)
        S += getsizeof(self.rotor_shift)
        S += getsizeof(self.stator_yoke_elements_r)
        S += getsizeof(self.airgap_elements_r)
        S += getsizeof(self.rotor_yoke_elements_r)
        S += getsizeof(self.stator_isthmus_elements_r)
        S += getsizeof(self.stator_tooth_elements_r)
        S += getsizeof(self.magnet_elements_r)
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

        # Get the properties inherited from Magnetics
        MagNetwork_dict = super(MagNetwork, self).as_dict(
            type_handle_ndarray=type_handle_ndarray,
            keep_function=keep_function,
            **kwargs
        )
        MagNetwork_dict["type_model"] = self.type_model
        MagNetwork_dict["type_coord_sys"] = self.type_coord_sys
        MagNetwork_dict["Kmesh_fineness"] = self.Kmesh_fineness
        MagNetwork_dict["rotor_shift"] = self.rotor_shift
        MagNetwork_dict["stator_yoke_elements_r"] = self.stator_yoke_elements_r
        MagNetwork_dict["airgap_elements_r"] = self.airgap_elements_r
        MagNetwork_dict["rotor_yoke_elements_r"] = self.rotor_yoke_elements_r
        MagNetwork_dict["stator_isthmus_elements_r"] = self.stator_isthmus_elements_r
        MagNetwork_dict["stator_tooth_elements_r"] = self.stator_tooth_elements_r
        MagNetwork_dict["magnet_elements_r"] = self.magnet_elements_r
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        MagNetwork_dict["__class__"] = "MagNetwork"
        return MagNetwork_dict

    def copy(self):
        """Creates a deepcopy of the object"""

        # Handle deepcopy of all the properties
        type_model_val = self.type_model
        type_coord_sys_val = self.type_coord_sys
        Kmesh_fineness_val = self.Kmesh_fineness
        rotor_shift_val = self.rotor_shift
        stator_yoke_elements_r_val = self.stator_yoke_elements_r
        airgap_elements_r_val = self.airgap_elements_r
        rotor_yoke_elements_r_val = self.rotor_yoke_elements_r
        stator_isthmus_elements_r_val = self.stator_isthmus_elements_r
        stator_tooth_elements_r_val = self.stator_tooth_elements_r
        magnet_elements_r_val = self.magnet_elements_r
        is_remove_slotS_val = self.is_remove_slotS
        is_remove_slotR_val = self.is_remove_slotR
        is_remove_ventS_val = self.is_remove_ventS
        is_remove_ventR_val = self.is_remove_ventR
        is_mmfs_val = self.is_mmfs
        is_mmfr_val = self.is_mmfr
        type_BH_stator_val = self.type_BH_stator
        type_BH_rotor_val = self.type_BH_rotor
        is_periodicity_t_val = self.is_periodicity_t
        is_periodicity_a_val = self.is_periodicity_a
        angle_stator_shift_val = self.angle_stator_shift
        angle_rotor_shift_val = self.angle_rotor_shift
        logger_name_val = self.logger_name
        if self.Slice_enforced is None:
            Slice_enforced_val = None
        else:
            Slice_enforced_val = self.Slice_enforced.copy()
        Nslices_enforced_val = self.Nslices_enforced
        type_distribution_enforced_val = self.type_distribution_enforced
        is_current_harm_val = self.is_current_harm
        T_mag_val = self.T_mag
        is_periodicity_rotor_val = self.is_periodicity_rotor
        # Creates new object of the same type with the copied properties
        obj_copy = type(self)(
            type_model=type_model_val,
            type_coord_sys=type_coord_sys_val,
            Kmesh_fineness=Kmesh_fineness_val,
            rotor_shift=rotor_shift_val,
            stator_yoke_elements_r=stator_yoke_elements_r_val,
            airgap_elements_r=airgap_elements_r_val,
            rotor_yoke_elements_r=rotor_yoke_elements_r_val,
            stator_isthmus_elements_r=stator_isthmus_elements_r_val,
            stator_tooth_elements_r=stator_tooth_elements_r_val,
            magnet_elements_r=magnet_elements_r_val,
            is_remove_slotS=is_remove_slotS_val,
            is_remove_slotR=is_remove_slotR_val,
            is_remove_ventS=is_remove_ventS_val,
            is_remove_ventR=is_remove_ventR_val,
            is_mmfs=is_mmfs_val,
            is_mmfr=is_mmfr_val,
            type_BH_stator=type_BH_stator_val,
            type_BH_rotor=type_BH_rotor_val,
            is_periodicity_t=is_periodicity_t_val,
            is_periodicity_a=is_periodicity_a_val,
            angle_stator_shift=angle_stator_shift_val,
            angle_rotor_shift=angle_rotor_shift_val,
            logger_name=logger_name_val,
            Slice_enforced=Slice_enforced_val,
            Nslices_enforced=Nslices_enforced_val,
            type_distribution_enforced=type_distribution_enforced_val,
            is_current_harm=is_current_harm_val,
            T_mag=T_mag_val,
            is_periodicity_rotor=is_periodicity_rotor_val,
        )
        return obj_copy

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type_model = None
        self.type_coord_sys = None
        self.Kmesh_fineness = None
        self.rotor_shift = None
        self.stator_yoke_elements_r = None
        self.airgap_elements_r = None
        self.rotor_yoke_elements_r = None
        self.stator_isthmus_elements_r = None
        self.stator_tooth_elements_r = None
        self.magnet_elements_r = None
        # Set to None the properties inherited from Magnetics
        super(MagNetwork, self)._set_None()

    def _get_type_model(self):
        """getter of type_model"""
        return self._type_model

    def _set_type_model(self, value):
        """setter of type_model"""
        check_var("type_model", value, "int", Vmin=1, Vmax=2)
        self._type_model = value

    type_model = property(
        fget=_get_type_model,
        fset=_set_type_model,
        doc=u"""Type of the model to be solved: linear (1) or non-linear (2)

        :Type: int
        :min: 1
        :max: 2
        """,
    )

    def _get_type_coord_sys(self):
        """getter of type_coord_sys"""
        return self._type_coord_sys

    def _set_type_coord_sys(self, value):
        """setter of type_coord_sys"""
        check_var("type_coord_sys", value, "int", Vmin=1, Vmax=2)
        self._type_coord_sys = value

    type_coord_sys = property(
        fget=_get_type_coord_sys,
        fset=_set_type_coord_sys,
        doc=u"""Type of the coordinate system: cartesian (1) or radial (2)

        :Type: int
        :min: 1
        :max: 2
        """,
    )

    def _get_Kmesh_fineness(self):
        """getter of Kmesh_fineness"""
        return self._Kmesh_fineness

    def _set_Kmesh_fineness(self, value):
        """setter of Kmesh_fineness"""
        check_var("Kmesh_fineness", value, "int")
        self._Kmesh_fineness = value

    Kmesh_fineness = property(
        fget=_get_Kmesh_fineness,
        fset=_set_Kmesh_fineness,
        doc=u"""Mesh density according to theta-direction

        :Type: int
        """,
    )

    def _get_rotor_shift(self):
        """getter of rotor_shift"""
        return self._rotor_shift

    def _set_rotor_shift(self, value):
        """setter of rotor_shift"""
        check_var("rotor_shift", value, "int")
        self._rotor_shift = value

    rotor_shift = property(
        fget=_get_rotor_shift,
        fset=_set_rotor_shift,
        doc=u"""number of cells to be shifted when changing the rotor position

        :Type: int
        """,
    )

    def _get_stator_yoke_elements_r(self):
        """getter of stator_yoke_elements_r"""
        return self._stator_yoke_elements_r

    def _set_stator_yoke_elements_r(self, value):
        """setter of stator_yoke_elements_r"""
        check_var("stator_yoke_elements_r", value, "int")
        self._stator_yoke_elements_r = value

    stator_yoke_elements_r = property(
        fget=_get_stator_yoke_elements_r,
        fset=_set_stator_yoke_elements_r,
        doc=u"""number of discretized elements of the stator yoke according to the r-axis

        :Type: int
        """,
    )

    def _get_airgap_elements_r(self):
        """getter of airgap_elements_r"""
        return self._airgap_elements_r

    def _set_airgap_elements_r(self, value):
        """setter of airgap_elements_r"""
        check_var("airgap_elements_r", value, "int")
        self._airgap_elements_r = value

    airgap_elements_r = property(
        fget=_get_airgap_elements_r,
        fset=_set_airgap_elements_r,
        doc=u"""number of discretized elements of the airgap according to the r-axis

        :Type: int
        """,
    )

    def _get_rotor_yoke_elements_r(self):
        """getter of rotor_yoke_elements_r"""
        return self._rotor_yoke_elements_r

    def _set_rotor_yoke_elements_r(self, value):
        """setter of rotor_yoke_elements_r"""
        check_var("rotor_yoke_elements_r", value, "int")
        self._rotor_yoke_elements_r = value

    rotor_yoke_elements_r = property(
        fget=_get_rotor_yoke_elements_r,
        fset=_set_rotor_yoke_elements_r,
        doc=u"""number of discretized elements of the rotor yoke according to the r-axis

        :Type: int
        """,
    )

    def _get_stator_isthmus_elements_r(self):
        """getter of stator_isthmus_elements_r"""
        return self._stator_isthmus_elements_r

    def _set_stator_isthmus_elements_r(self, value):
        """setter of stator_isthmus_elements_r"""
        check_var("stator_isthmus_elements_r", value, "int")
        self._stator_isthmus_elements_r = value

    stator_isthmus_elements_r = property(
        fget=_get_stator_isthmus_elements_r,
        fset=_set_stator_isthmus_elements_r,
        doc=u"""number of discretized elements of the geometry between the stator interior radius and the slot interior radius

        :Type: int
        """,
    )

    def _get_stator_tooth_elements_r(self):
        """getter of stator_tooth_elements_r"""
        return self._stator_tooth_elements_r

    def _set_stator_tooth_elements_r(self, value):
        """setter of stator_tooth_elements_r"""
        check_var("stator_tooth_elements_r", value, "int")
        self._stator_tooth_elements_r = value

    stator_tooth_elements_r = property(
        fget=_get_stator_tooth_elements_r,
        fset=_set_stator_tooth_elements_r,
        doc=u"""number of discretized elements of the stator tooth according to the r-axis

        :Type: int
        """,
    )

    def _get_magnet_elements_r(self):
        """getter of magnet_elements_r"""
        return self._magnet_elements_r

    def _set_magnet_elements_r(self, value):
        """setter of magnet_elements_r"""
        check_var("magnet_elements_r", value, "int")
        self._magnet_elements_r = value

    magnet_elements_r = property(
        fget=_get_magnet_elements_r,
        fset=_set_magnet_elements_r,
        doc=u"""number of discretized elements of the magnet according to the r-axis

        :Type: int
        """,
    )
