#!/usr/bin/env python

from unittest import TestCase
from fundamentals.backtracking.path_through_grid import PathThroughGrid


class TestPathThroughGrid(TestCase):

    def test_no_path(self):
        grid = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 0, 1]
        ]

        ptg = PathThroughGrid(grid)
        self.assertIsNone(ptg.get_path())

    def test_path(self):
        grid = [
            [1, 1, 0],
            [1, 1, 1],
            [0, 0, 1]
        ]

        ptg = PathThroughGrid(grid)
        self.assertEquals([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)],ptg.get_path())