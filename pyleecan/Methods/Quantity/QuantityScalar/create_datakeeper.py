from ....Classes.DataKeeper import DataKeeper


def create_datakeeper(self):
    """Create a Datakeeper for a scalar quantity

    Returns
    -------
    DataKeeper
        The datakeeper created
    """
    return DataKeeper(
        name=self.name,
        symbol=self.symbol,
        unit=self.unit,
        physic=self.physic,
        keeper=f"lambda output : output.{self.getter}",
        error_keeper="lambda simu: np.nan",
    )
