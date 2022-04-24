import math
import pandas as pd
import numpy as np

class LOF:

    def __init__(self, data):
        self.data = data

    @staticmethod
    def _k_distance(data: np.ndarray, max_n: int = 3):
        """ Static method to get k_distance

        data: Pandas Dataframe or Numpy array
        max_n: Number of maximum neighbours
        """

        data.mean(axis=1)





