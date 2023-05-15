from ...Classes.QuantityScalar import QuantityScalar
from ...Classes.QuantityData import QuantityData
from ...Classes.QuantityVectorField import QuantityVectorField


def Is__quantity_maker(**kwarg):
    return QuantityData(
        symbol="Is",
        name="Stator phase current",
        physic="elec",
        unit="Arms",
        unit_plot="Arms",
        getter="elec.get_Is()",
        axes_name=["time", "phase"],
    )


def Id__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Id",
        name="Stator phase current along d-axis",
        physic="elec",
        unit="Arms",
        unit_plot="Arms",
        getter="elec.OP.get_Id_Iq()['Id']",
    )


def Iq__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Iq",
        name="Stator phase current along q-axis",
        physic="elec",
        unit="Arms",
        unit_plot="Arms",
        getter="elec.OP.get_Id_Iq()['Iq']",
    )


def If__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="If",
        name="Rotor current",
        physic="elec",
        unit="Arms",
        unit_plot="Arms",
        getter="elec.OP.If_ref()",
    )


def Tem_av_ref__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Tem_av_ref",
        name="Reference average electromagnetic torque",
        physic="elec",
        unit="N.m",
        unit_plot="N.m",
        getter="elec.OP.Tem_av_ref",
    )


def Tem_av_elec__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Tem_av_elec",
        name="Average Torque from EEC",
        physic="elec",
        unit="N.m",
        unit_plot="N.m",
        getter="elec.Tem_av",
    )


def slip__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="slip",
        name="Rotor mechanical slip",
        physic="elec",
        unit="",
        unit_plot="",
        getter="elec.OP.get_slip()",
    )


def s_times_f_e__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="s.f_e",
        name="Slip frequency",
        physic="elec",
        unit="Hz",
        unit_plot="Hz",
        getter="",
    )


def U0_per_f_e__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="U0/f_e",
        name="Voltage frequency",
        physic="elec",
        unit="V/Hz",
        unit_plot="V/Hz",
        getter="",
    )


def Rfe__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Rfe",
        name="Iron loss resistance",
        physic="elec",
        unit="Ohm",
        unit_plot="Ohm",
        getter="elec.eec.Rfe",
    )


def L1__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="L1",
        name="Stator phase inductance",
        physic="elec",
        unit="H",
        unit_plot="H",
        getter="elec.eec.L1",
    )


def R1__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="R1",
        name="Stator phase resistance",
        physic="elec",
        unit="Ohm",
        unit_plot="Ohm",
        getter="elec.eec.R1",
    )


def R2__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="R2",
        name="Rotor phase resistance",
        physic="elec",
        unit="Ohm",
        unit_plot="Ohm",
        getter="elec.eec.R2",
    )


def L2__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="L2",
        name="Rotor phase inductance",
        physic="elec",
        unit="H",
        unit_plot="H",
        getter="elec.eec.L2",
    )


def K21Z__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="K21Z",
        name="transformation ratio from secondary (2, rotor) to primary (1, stator) for impedance",
        physic="elec",
        unit="",
        unit_plot="",
        getter="elec.eec.K21Z",
    )


def K21I__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="K21I",
        name="transformation ratio from secondary (2, rotor) to primary (1, stator) for current",
        physic="elec",
        unit="",
        unit_plot="",
        getter="elec.eec.K21I",
    )


def Im_table__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Im_table",
        name="Array of magnetizing current",
        physic="elec",
        unit="Arms",
        unit_plot="Arms",
        getter="elec.eec.Im_table",
    )


def Lm_table__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Lm_table",
        name="Array of magnetizing inductance function of Im_table",
        physic="elec",
        unit="H",
        unit_plot="H",
        getter="elec.eec.Lm_table",
    )


def I1__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="I1",
        name="Stator phase current (after solve)",
        physic="elec",
        unit="Arms",
        unit_plot="Arms",
        getter="elec.eec.I1",
    )


def I2__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="I2",
        name="Rotor phase current (after solve)",
        physic="elec",
        unit="Arms",
        unit_plot="Arms",
        getter="elec.eec.I2",
    )


def U1__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="U1",
        name="Stator phase voltage (after solve)",
        physic="elec",
        unit="Vrms",
        unit_plot="Vrms",
        getter="elec.eec.U1",
    )


def U2__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="U2",
        name="Rotor phase voltage (after solve)",
        physic="elec",
        unit="Vrms",
        unit_plot="Vrms",
        getter="elec.eec.U2",
    )


def Ife__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Ife",
        name="Iron loss current (after solve)",
        physic="elec",
        unit="Arms",
        unit_plot="Arms",
        getter="elec.eec.If",
    )


def Lm__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Lm",
        name="Magnetizing inductance (after solve)",
        physic="elec",
        unit="H",
        unit_plot="H",
        getter="elec.eec.Lm",
    )


def Im__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Im",
        name="Magnetizing current (after solve)",
        physic="elec",
        unit="Arms",
        unit_plot="Arms",
        getter="elec.eec.Im",
    )


def Trot__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Trot",
        name="Average rotor temperature for operational EEC calculation",
        physic="elec",
        unit="degC",
        unit_plot="degC",
        getter="elec.eec.Trot",
    )


def Tsta__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Tsta",
        name="Average stator temperature for operational EEC calculation",
        physic="elec",
        unit="degC",
        unit_plot="degC",
        getter="elec.eec.Tsta",
    )


def Xke_skinS__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Xke_skinS",
        name="Skin effect coefficient for inductances at stator side",
        physic="elec",
        unit="",
        unit_plot="",
        getter="elec.eec.Xke_skinS",
    )


def Xke_skinR__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Xke_skinR",
        name="Skin effect coefficient for inductances at rotor side",
        physic="elec",
        unit="",
        unit_plot="",
        getter="elec.eec.Kke_skinR",
    )


def Xkr_skinS__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Xkr_skinS",
        name="Skin effect coefficient for resistances at stator side",
        physic="elec",
        unit="",
        unit_plot="",
        getter="elec.eec.Xkr_skinS",
    )


def Xkr_skinR__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Xkr_skinR",
        name="Skin effect coefficient for resistances at rotor side",
        physic="elec",
        unit="",
        unit_plot="",
        getter="elec.eec.Xkr_skinR",
    )


def Ud__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Ud",
        name="Stator voltage along d-axis",
        physic="elec",
        unit="Vrms",
        unit_plot="Vrms",
        getter="elec.OP.get_Ud_Uq()['Ud']",
    )


def Uq__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Uq",
        name="Stator voltage along q-axis",
        physic="elec",
        unit="Vrms",
        unit_plot="Vrms",
        getter="elec.OP.get_Ud_Uq()['Uq']",
    )


def I0__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="I0",
        name="Stator current rms amplitude",
        physic="elec",
        unit="Arms",
        unit_plot="Arms",
        getter="elec.OP.get_I0_Phi0()['I0']",
    )


def U0__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="U0",
        name="Stator voltage rms amplitude",
        physic="elec",
        unit="Vrms",
        unit_plot="Vrms",
        getter="elec.OP.get_U0_UPhi0()['U0']",
    )


def phi0__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="phi0",
        name="Stator current phase",
        physic="elec",
        unit="rad",
        unit_plot="rad",
        getter="elec.OP.get_I0_Phi0()['Phi0']",
    )


def Uphi0__quantity_maker(**kwarg):
    return QuantityScalar(
        symbol="Uphi0",
        name="Stator voltage phase",
        physic="elec",
        unit="rad",
        unit_plot="Vrms",
        getter="elec.OP.get_U0_UPhi0()['UPhi0']",
    )
