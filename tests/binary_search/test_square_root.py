#!/usr/bin/env python

from unittest import TestCase
from fundamentals.binary_search.square_root import SquareRoot

class TestSquareRoot(TestCase):

    def test_sqrt_gt_one(self):
        self.assertAlmostEqual(10, SquareRoot.sqrt(100))

    def test_sqrt_lt_one(self):
        self.assertAlmostEqual(0.1, SquareRoot.sqrt(0.01))

    def test_sqrt_one(self):
        self.assertAlmostEqual(1, SquareRoot.sqrt(1))

    def test_throws_on_negatives(self):
        with self.assertRaises(ValueError):
            SquareRoot.sqrt(-1)


def main():
    pass


if __name__ == "__main__":
    main()