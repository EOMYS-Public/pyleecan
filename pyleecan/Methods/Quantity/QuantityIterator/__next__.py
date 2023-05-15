def __next__(self):
    if self.physic_iter is None:
        self.init_iterator()

    if self.remaining_qty is None or len(self.remaining_qty) == 0:
        self.phy_dict = self.physic_iter.__next__()  # raise StopIteration
        self.remaining_qty = list(self.phy_dict.keys())

    qty = self.remaining_qty.pop(0)
    return self.phy_dict[qty]
