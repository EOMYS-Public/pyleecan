from os.path import join, isfile
from numpy import pi


def convert_other_to_dict(self, file_path):
    """convert file .mot into dict and creation other_unit_dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    file_path : str
        Path to the file to convert

    Returns
    ----------
    other_dict: dict
        dict with param present in file .mot without unit
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)
    """

    list_path = file_path.split(".")
    if not list_path[-1] == "mot":
        raise NameError("the file is not a .mot, please select a .mot to convert")
    if not isfile(file_path):
        raise Exception("Error: This file doesn't exist: " + file_path)
    else:
        file = open(join(file_path, file_path))

    ####
    # .mot files are organized as follow:
    # the file is compose different part, with a title into [], and after a list of value, after restart an other part, we have a space
    # to example
    # [Dimensions]
    # Stator_Lam_Dia=130
    # Stator_Bore=80
    # Airgap=1

    # [Design_Options]
    # BPM_Rotor=Surface_Radial
    # Top_Bar=Round
    # Bottom_Bar=Rectangular
    ####

    ####
    # other_dict = {
    #   [Dimensions] = {
    #        Stator_Lam_Dia : 130
    #        Stator_Bore : 80
    #        Airgap : 1
    #       }
    #
    #   [Design_Options] = {
    #       BPM_Rotor : Surface_Radial
    #       Top_Bar : Round
    #       Bottom_Bar : Rectangular
    #       }
    # }
    ####

    other_dict = {}
    for line in file:
        # if the float is writte with "," ex :1,26   ti do conversion we need to have float writte with point ex 1.26
        line = line.replace(",", ".")
        # deleted \n in line
        line = line.strip("\n")
        # separation different part like .mot
        if line[:1] == "[":
            temp_dict = {}
            other_dict[line] = temp_dict
        elif line == "":
            pass

        else:
            # lb = line before =
            lb = line.split("=")
            value = lb[1]

            # changement type after equal (value)
            if isint(value):
                value = int(value)
            elif value == ("True"):
                value = True
            elif value == ("False"):
                value = False
            elif isfloat(value):
                value = float(value)

            if value == (""):
                pass
            else:
                temp_dict[lb[0]] = value

    # Extract unit dict
    other_unit_dict_temp = other_dict["[Units]"]
    other_unit_dict = {}

    # set length
    unit = other_unit_dict_temp["Units_Length"]
    if unit == "mm":
        other_unit_dict["m"] = 0.001
        # we want to have m so we need to multiply by 0.001
    elif unit == "m":
        other_unit_dict["m"] = 1

    other_unit_dict["rad"] = 1
    other_unit_dict["deg"] = pi / 180

    pole_number = other_dict["[Dimensions]"]["Pole_Number"]

    other_unit_dict["ED"] = (2 / pole_number) * (pi / 180)
    # we want to have rad so we need to multiply by 2/pole_number
    other_unit_dict[None] = 1  # No unit => No scale
    other_unit_dict[""] = 1  # No unit => No scale
    other_unit_dict["-"] = 1  # No unit => No scale
    other_unit_dict["[]"] = 1  # No unit => No scale

    self.other_dict = other_dict
    self.other_unit_dict = other_unit_dict
    file.close()


# conversion str in float
def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


# conversion str in int
def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
