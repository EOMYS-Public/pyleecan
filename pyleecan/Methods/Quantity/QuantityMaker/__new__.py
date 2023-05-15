from ....Classes import QuantityMaker as QM


def __new__(cls, *args, **kwargs):
    if QM.QuantityMaker.unique_instance is None:
        QM.QuantityMaker.unique_instance = super(QM.QuantityMaker, cls).__new__(
            cls, *args, **kwargs
        )
    return QM.QuantityMaker.unique_instance
    # return super(QM.QuantityMaker, cls).__new__(cls, *args, **kwargs)
