import unittest
from src.rowavg import averages


class TestAvg(unittest.TestCase):
    def test_avg(self):
        self.assertEqual(averages(["1 3", "2 4"]), [2.0, 3.0])


if __name__ == "__main__":
    unittest.main()
