from ....Classes.QuantityIterator import QuantityIterator


def __iter__(self):
    return self.get_quantity_iter(self)
