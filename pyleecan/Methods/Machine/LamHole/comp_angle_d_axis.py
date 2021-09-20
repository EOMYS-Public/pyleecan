from numpy import pi


def comp_angle_d_axis(self):
    """Compute the angle between the X axis and the first d+ axis
    By convention a "Tooth" is centered on the X axis
    By convention the first magnet is +

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    d_angle : float
        angle between the X axis and the first d+ axis
    """

    p = self.get_pole_pair_number()
    if self.has_magnet() and self.hole[0].magnet_0.type_magnetization!=3: #Normale rotor with magnets
        return pi / p / 2
    else: #Without magnet or spoke rotor with magnets
        return 0
