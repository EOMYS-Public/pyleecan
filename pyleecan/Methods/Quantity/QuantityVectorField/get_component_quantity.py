from ....Classes.QuantityMaker import QuantityMaker


def get_component_quantity(self, component):
    symbol = f"{self.symbol}_{component}"
    return QuantityMaker().create_quantity(symbol, self.physic)
