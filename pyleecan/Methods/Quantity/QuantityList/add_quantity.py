from ....Classes.QuantityMaker import QuantityMaker


def add_quantity(self, symbols, physic):
    """Add a quantity into the quantity list

    Parameters
    ----------
    symbol : str or list of str
        quantity(ies) to add. Need to have the same physic
    physic : str
        physic of the quantity(ies)
    """
    if isinstance(symbols, str):
        symbols = [symbols]

    for symbol in symbols:
        if not self.is_in(symbol, physic):
            qty = QuantityMaker().create_quantity(symbol, physic)
            if physic not in self.container:
                self.container[physic] = {}

            self.container[physic][qty.symbol] = qty
