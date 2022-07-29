def get_hole_list(self):
    """Return the list of all the holes

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    hole_list : [Hole]
        List of all the holes
    """
    if self.hole is None:
        self.hole = list()
    return self.hole
