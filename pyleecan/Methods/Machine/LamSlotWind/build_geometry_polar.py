import numpy as np
from numpy import exp
from ....Classes.Circle import Circle
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import LAM_LAB
from copy import deepcopy


def build_geometry_polar(self, sym=1):
    """compute the point coordinates needed to plot the stator

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    """

    # Dimensions in m
    Stat_in = self.Rint
    Stat_out = self.Rext
    Stat_yoke = Stat_out - self.comp_height_yoke()
    slot_int = Stat_yoke - self.slot.comp_height_active()

    # angles in rad
    angle_slot = self.slot.comp_angle_active_eq()
    angle_slot_opening_int = self.slot.comp_angle_opening()
    angle_half_teeth = (2 * np.pi - (self.get_Zs() * angle_slot)) / (2 * self.get_Zs())
    stator_angle = 2 * np.pi / self.get_Zs()

    # Definition of points
    Z1 = Stat_in * exp(0j)
    Z2 = Stat_yoke * exp(0j)
    Z3 = Stat_out * exp(0j)
    Z4 = Stat_in * exp(-1j * angle_half_teeth)
    Z5 = Stat_yoke * exp(-1j * angle_half_teeth)
    Z6 = Stat_in * exp(-1j * (angle_half_teeth + angle_slot))
    Z7 = Stat_yoke * exp(-1j * (angle_half_teeth + angle_slot))
    Z8 = Stat_in * exp(-1j * (2 * angle_half_teeth + angle_slot))
    Z9 = Stat_yoke * exp(-1j * (2 * angle_half_teeth + angle_slot))
    Z10 = Stat_out * exp(-1j * (2 * angle_half_teeth + angle_slot))
    # points in case (W0 != W2)
    Za = Stat_in * exp(
        -1j * (angle_half_teeth + 0.5 * (angle_slot - angle_slot_opening_int))
    )
    Zb = slot_int * exp(
        -1j * (angle_half_teeth + 0.5 * (angle_slot - angle_slot_opening_int))
    )
    Zc = slot_int * exp(
        -1j * (angle_half_teeth + 0.5 * (angle_slot + angle_slot_opening_int))
    )
    Zd = Stat_in * exp(
        -1j * (angle_half_teeth + 0.5 * (angle_slot + angle_slot_opening_int))
    )
    # points in case (stator_isthmus != 0)
    Z1_isthmus = slot_int * exp(-1j * angle_half_teeth)
    Z2_isthmus = slot_int * exp(-1j * (angle_half_teeth + angle_slot))
    Z3_isthmus = slot_int * exp(0j)
    Z4_isthmus = slot_int * exp(-1j * (2 * angle_half_teeth + angle_slot))

    # Defining lines and arcs
    stator_yoke_list = list()
    stator_tooth_list1 = list()
    stator_tooth_list2 = list()
    stator_isthmus_list1 = list()
    stator_isthmus_list2 = list()
    surf_stat_list = list()
    surf_list = list()
    # air_isthmus_list = list()

    # Definition of the stator yoke surface
    stator_yoke_list.append(Segment(Z2, Z3))
    stator_yoke_list.append(Arc1(Z3, Z10, -Stat_out, is_trigo_direction=False))
    stator_yoke_list.append(Segment(Z10, Z9))
    stator_yoke_list.append(Arc1(Z9, Z7, Stat_yoke))
    stator_yoke_list.append(Arc1(Z7, Z5, slot_int))
    stator_yoke_list.append(Arc1(Z5, Z2, Stat_yoke))

    # Definition of the other surfaces
    if slot_int != Stat_in:
        if angle_slot_opening_int == angle_slot:
            # surf isthmus 1
            stator_isthmus_list1.append(Segment(Z1, Z3_isthmus))
            stator_isthmus_list1.append(
                Arc1(Z3_isthmus, Z1_isthmus, -slot_int, is_trigo_direction=False)
            )
            stator_isthmus_list1.append(Segment(Z1_isthmus, Z4))
            stator_isthmus_list1.append(Arc1(Z4, Z1, Stat_in))

            # surf isthmus 2
            stator_isthmus_list2.append(Segment(Z6, Z2_isthmus))
            stator_isthmus_list2.append(
                Arc1(Z2_isthmus, Z4_isthmus, -slot_int, is_trigo_direction=False)
            )
            stator_isthmus_list2.append(Segment(Z4_isthmus, Z8))
            stator_isthmus_list2.append(Arc1(Z8, Z6, Stat_in))

            # surf tooth 1
            stator_tooth_list1.append(Segment(Z3_isthmus, Z2))
            stator_tooth_list1.append(
                Arc1(Z2, Z5, -Stat_yoke, is_trigo_direction=False)
            )
            stator_tooth_list1.append(Segment(Z5, Z1_isthmus))
            stator_tooth_list1.append(Arc1(Z1_isthmus, Z3_isthmus, slot_int))

            # surf tooth 2
            stator_tooth_list2.append(Segment(Z2_isthmus, Z7))
            stator_tooth_list2.append(
                Arc1(Z7, Z9, -Stat_yoke, is_trigo_direction=False)
            )
            stator_tooth_list2.append(Segment(Z9, Z4_isthmus))
            stator_tooth_list2.append(Arc1(Z4_isthmus, Z2_isthmus, slot_int))
        else:
            # surf isthmus 1
            stator_isthmus_list1.append(Segment(Z1, Z3_isthmus))
            stator_isthmus_list1.append(
                Arc1(Z3_isthmus, Z1_isthmus, -slot_int, is_trigo_direction=False)
            )
            stator_isthmus_list1.append(
                Arc1(Z1_isthmus, Zb, -slot_int, is_trigo_direction=False)
            )
            stator_isthmus_list1.append(Segment(Zb, Za))
            stator_isthmus_list1.append(Arc1(Za, Z1, Stat_in))

            # surf isthmus 2
            stator_isthmus_list2.append(Segment(Zd, Zc))
            stator_isthmus_list2.append(
                Arc1(Zc, Z2_isthmus, -slot_int, is_trigo_direction=False)
            )
            stator_isthmus_list2.append(
                Arc1(Z2_isthmus, Z4_isthmus, -slot_int, is_trigo_direction=False)
            )
            stator_isthmus_list2.append(Segment(Z4_isthmus, Z8))
            stator_isthmus_list2.append(Arc1(Z8, Zd, Stat_in))

            # surf tooth 1
            stator_tooth_list1.append(Segment(Z3_isthmus, Z2))
            stator_tooth_list1.append(
                Arc1(Z2, Z5, -Stat_yoke, is_trigo_direction=False)
            )
            stator_tooth_list1.append(Segment(Z5, Z1_isthmus))
            stator_tooth_list1.append(Arc1(Z1_isthmus, Z3_isthmus, slot_int))

            # surf tooth 2
            stator_tooth_list2.append(Segment(Z2_isthmus, Z7))
            stator_tooth_list2.append(
                Arc1(Z7, Z9, -Stat_yoke, is_trigo_direction=False)
            )
            stator_tooth_list2.append(Segment(Z9, Z4_isthmus))
            stator_tooth_list2.append(Arc1(Z4_isthmus, Z2_isthmus, slot_int))

        # surf air slot
        # air_isthmus_list.append(Segment(Z4, Z1_isthmus))
        # air_isthmus_list.append(Segment(Z6, Z2_isthmus))
        # air_isthmus_list.append(Arc1(Z4, Z6, Stat_in))
        # air_isthmus_list.append(Arc1(Z1_isthmus, Z2_isthmus, slot_int))

    else:
        # surf tooth 1
        stator_tooth_list1.append(Segment(Z1, Z2))
        stator_tooth_list1.append(Arc1(Z2, Z5, -Stat_yoke, is_trigo_direction=False))
        stator_tooth_list1.append(Segment(Z5, Z4))
        stator_tooth_list1.append(Arc1(Z4, Z1, Stat_in))

        # surf tooth 2
        stator_tooth_list2.append(Segment(Z6, Z7))
        stator_tooth_list2.append(Arc1(Z7, Z9, -Stat_yoke, is_trigo_direction=False))
        stator_tooth_list2.append(Segment(Z9, Z8))
        stator_tooth_list2.append(Arc1(Z8, Z6, Stat_in))

    # Defining surfaces
    surf_stator_yoke = SurfLine(
        line_list=stator_yoke_list,
        label="Yoke",
        point_ref=((Stat_out + Stat_yoke) / 2)
        * exp(-1j * (angle_half_teeth + (angle_slot / 2))),
    )
    surf_stat_list.append(surf_stator_yoke)
    if slot_int != Stat_in:
        surf1_stator_teeth = SurfLine(
            line_list=stator_tooth_list1,
            label="Tooth1",
            point_ref=((slot_int + Stat_yoke) / 2) * exp(-1j * (angle_half_teeth / 2)),
        )
        surf_stat_list.append(surf1_stator_teeth)
        surf2_stator_teeth = SurfLine(
            line_list=stator_tooth_list2,
            label="Tooth2",
            point_ref=((slot_int + Stat_yoke) / 2)
            * exp(-1j * (angle_slot + (3 / 2 * angle_half_teeth))),
        )
        surf_stat_list.append(surf2_stator_teeth)
        surf1_stator_isthmus = SurfLine(
            line_list=stator_isthmus_list1,
            label="stator_isthmus1",
            point_ref=((slot_int + Stat_in) / 2) * exp(-1j * (angle_half_teeth / 2)),
        )
        surf_stat_list.append(surf1_stator_isthmus)
        surf2_stator_isthmus = SurfLine(
            line_list=stator_isthmus_list2,
            label="stator_isthmus2",
            point_ref=((slot_int + Stat_in) / 2)
            * exp(-1j * (angle_slot + (3 / 2 * angle_half_teeth))),
        )
        surf_stat_list.append(surf2_stator_isthmus)
    else:
        surf1_stator_teeth = SurfLine(
            line_list=stator_tooth_list1,
            label="Tooth1",
            point_ref=((Stat_in + Stat_yoke) / 2) * exp(-1j * (angle_half_teeth / 2)),
        )
        surf_stat_list.append(surf1_stator_teeth)
        surf2_stator_teeth = SurfLine(
            line_list=stator_tooth_list2,
            label="Tooth2",
            point_ref=((Stat_in + Stat_yoke) / 2)
            * exp(-1j * (angle_slot + (3 / 2 * angle_half_teeth))),
        )
        surf_stat_list.append(surf2_stator_teeth)

    # Rotate the defined surfaces to define 2*pi angle
    # Definition of initial surfaces
    surf_list.append(deepcopy(surf_stator_yoke))
    surf_list.append(deepcopy(surf1_stator_teeth))
    surf_list.append(deepcopy(surf2_stator_teeth))
    if slot_int != Stat_in:
        surf_list.append(deepcopy(surf1_stator_isthmus))
        surf_list.append(deepcopy(surf2_stator_isthmus))

    # Definition of rotated surfaces
    for i in range(self.get_Zs() // sym - 1):
        # surf stator yoke
        surf_stator_yoke.rotate(stator_angle)
        surf_list.append(deepcopy(surf_stator_yoke))
        # surf 1 stator tooth
        surf1_stator_teeth.rotate(stator_angle)
        surf_list.append(deepcopy(surf1_stator_teeth))
        # surf 2 stator tooth
        surf2_stator_teeth.rotate(stator_angle)
        surf_list.append(deepcopy(surf2_stator_teeth))
        if slot_int != Stat_in:
            # surf 1 stator isthmus
            surf1_stator_isthmus.rotate(stator_angle)
            surf_list.append(deepcopy(surf1_stator_isthmus))
            # surf 2 stator isthmus
            surf2_stator_isthmus.rotate(stator_angle)
            surf_list.append(deepcopy(surf2_stator_isthmus))

    for surf in surf_list:
        surf.label = self.get_label() + "_" + LAM_LAB
    # return surf_stat_list
    return surf_list
