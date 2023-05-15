def __next__(self):
    if self.remaining_phy is None:
        self.init_iterator()

    if len(self.remaining_phy) == 0:
        raise StopIteration
    else:
        phy = self.remaining_phy.pop(0)
        return self.container[phy]
