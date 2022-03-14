from numpy import sum as np_sum, abs as np_abs, matmul


def comp_core_losses(self, group, freqs, Ce=None, Ch=None):
    """Calculate losses in iron core given by group "stator core" or "rotor core"
    assuming power density is given by (cf. https://www.femm.info/wiki/SPMLoss):

        Pcore = Ph + Pe = Ch*f*B^2 + Ce*f^2*B^2

    Parameters
    ----------
    self: LossFEMM
        a LossFEMM object
    group: str
        Name of part in which to calculate core losses
    freqs: ndarray
        frequency vector [Hz]
    Ch: float
        hysteresis loss coefficients [W/(m^3*T^2*Hz)]
    Ce: float
        eddy current loss coefficients [W/(m^3*T^2*Hz^2)]

    Returns
    -------
    Pcore : float
        Overall core losses [W]
    Pcore_density : ndarray
        Core loss density function of frequency and elements [W/m3]
    """

    if self.parent.parent is None:
        raise Exception("Cannot calculate core losses if simu is not in an Output")
    else:
        output = self.parent.parent

    if output.mag is None:
        raise Exception("Cannot calculate core losses if OutMag.mesholution is None")

    machine = output.simu.machine

    p = machine.get_pole_pair_number()

    if "stator" in group:
        Lst = machine.stator.L1
    else:
        Lst = machine.rotor.L1

    # Get magnetic flux density complex amplitude over frequency and for each element center in current group
    Bval_fft, Se = output.mag.get_fft_from_meshsol(group, label="B")

    # Squared flux density
    Bfft_square = np_abs(Bval_fft) ** 2

    # Eddy-current loss density (or proximity loss density) for each frequency and element
    Pcore_density = Ce * freqs[:, None] ** 2 * Bfft_square

    if Ch != 0:
        # Hysteretic loss density for each frequency and element
        Pcore_density += Ch * freqs[:, None] * Bfft_square

    # Integrate loss density over elements' volume and sum over frequency to get overall loss
    Pcore = Lst * 2 * p * np_sum(matmul(Pcore_density, Se))

    # Check if lambda function exists in coeff_dict
    coeff_dict = output.loss.coeff_dict
    if group not in coeff_dict:
        # Create lambda function to recalculate overall losses function of frequency
        coeff = matmul(Bfft_square, Se)
        if Ch == 0:
            A = 0
        else:
            A = Lst * 2 * p * Ch * coeff
        B = Lst * 2 * p * Ce * coeff
        coeff_dict[group] = {"A": A, "B": B}

        # lambda x: np_sum(A * x + B * x ** 2)

    return Pcore, Pcore_density