def is_in(self, qty, phy):
    return phy in self.container and qty in self.container[phy]
