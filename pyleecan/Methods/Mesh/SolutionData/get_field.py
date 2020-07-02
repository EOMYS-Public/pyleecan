# -*- coding: utf-8 -*-
import numpy as np


def get_field(self, field_symbol="", index=None, indice=None, direction=None):
    """Get the value of variables stored in Solution.

     Parameters
     ----------
     self : Solution
         an Solution object
     field_name : str
         name of the field to return

     Returns
     -------
     field: array
         an array of field values

     """
#    if field_symbol == self.field.symbol:
    if index is None and indice is None and direction is None:
        if "direction" in [axis.name for axis in self.field.axes]:  # Vector
            field = self.field.get_along("time", "indice", "direction")[
                self.field.symbol
            ]
        else:  # scalar
            field = self.field.get_along("time", "indice")[self.field.symbol]

    elif indice is None and direction is None:
        if "direction" in [axis.name for axis in self.field.axes]:  # Vector
            field = self.field.get_along(
                "time[" + str(index) + "]", "indice", "direction"
            )[self.field.symbol]
        else:  # scalar
            field = self.field.get_along("time[" + str(index) + "]", "indice")[
                self.field.symbol
            ]

    return field