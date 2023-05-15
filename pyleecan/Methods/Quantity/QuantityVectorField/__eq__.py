from ....Functions.Load.import_class import import_class


def __eq__(self, other):
    qty_vectFiedl_class = import_class("pyleecan.Classes", "QuantityVectorField")
    return (
        super(qty_vectFiedl_class).__eq__(other) and self.components == other.components
    )
