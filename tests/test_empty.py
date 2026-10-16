import unittest
from src.rowavg import averages


class TestEmpty(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(averages([""]), [None])


if __name__ == "__main__":
    unittest.main()
