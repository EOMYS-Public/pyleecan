def __eq__(self, other):
    return (
        self.symbol == other.symbol
        and self.name == other.name
        and self.physic == other.physic
        and self.unit == other.unit
        and self.unit_plot == other.unit_plot
        and self.getter == other.getter
    )
