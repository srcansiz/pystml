from pystml.stats.LOF import LOF
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
        pass



