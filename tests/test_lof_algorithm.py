from pystml.stats.LOF import LOF
from pystml._neighbour import euclidean
from utils.generate_data import generate_lof_data
import unittest

LOF_data = generate_lof_data(save=False)


class TestLOF(unittest.TestCase):

    def setUp(self) -> None:
        self.lof = LOF(data=LOF_data)
        pass

    def tearDown(self) -> None:
        pass

    def test_k_distance(self):
        print("HERE")
        dist = euclidean(((1, 2), (1, 2)))
        print(dist)
        raise TypeError
