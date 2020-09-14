# -*- coding: utf-8 -*-

from numpy import array_equal, roll, squeeze, sum as np_sum
from numpy.linalg import norm


def comp_wind_sym(wind_mat):
    """Computes the winding pattern periodicity and symmetries

    Parameters
    ----------
    wind_mat : numpy.ndarray
        Matrix of the Winding

    Returns
    -------
    Nperw: int
        Number of electrical period of the winding

    """
    assert len(wind_mat.shape) == 4, "dim 4 expected for wind_mat"

    # Summing on all the layers (Nlay_r and Nlay_theta)
    wind_mat2 = squeeze(np_sum(np_sum(wind_mat, axis=1), axis=0))

    qs = wind_mat.shape[3]  # Number of phase
    Zs = wind_mat.shape[2]  # Number of Slot

    Nperw = 1  # Number of electrical period of the winding
    Nperslot = 1  # Periodicity of the winding in number of slots

    for q in range(0, qs):
        k = 0
        stri = ""
        while k < Zs:
            stri = stri + str(int(wind_mat2[k, q]))
            k += 1
        Nperslot = lcm(Nperslot, principal_period(stri))

    if Nperslot == 1 or Nperslot == Zs:
        Nperw == 1
    else:
        Nperw = int(Zs / Nperslot)

    # Check for anti symmetries in the elementary winding pattern
    if (
        Nperw % 2 == 0
        and norm(
            wind_mat2[0 : Nperw // 2, :] + wind_mat2[Nperw // 2 : Nperw, :]
        )
        == 0
    ):
        is_asym_wind = True
        Nperw = Nperw * 2
    else:
        is_asym_wind = False

    return Nperw, is_asym_wind

def principal_period(s):
    i = (s+s).find(s, 1, -1)
    return 1 if i == -1 else s.count(s[:i])

def gcd(a, b):
    """Return the greatest common divisor of a and b

    Parameters
    ----------
    a : int
        first number
    b : int
        second number

    Returns
    -------
    gcd : int
        greatest common divisor of a and b
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return the least common multiple of a and b

    Parameters
    ----------
    a : int
        first number
    b : int
        second number

    Returns
    -------
    lcm : int
        least common multiple of a and b
    """
    return a * b // gcd(a, b)
