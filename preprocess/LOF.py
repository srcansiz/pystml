import math
import pystml.utils as ut


def plot():
    return None


class LOF:

    def __init__(self, data, k=10):
        data, type = ut.checkDataFormat(data)
        self.data = data
        self.type = type
        self.k = k





