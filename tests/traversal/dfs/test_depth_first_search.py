#!/usr/bin/env python

from unittest import TestCase
from fundamentals.traversal.dfs.depth_first_search import DepthFirstSearch

class TestDepthFirstSearch(TestCase):

    def test_dfs(self):

        adjlist = [
            [1],
            [0, 4, 5],
            [3, 4, 5],
            [2, 6],
            [1, 2],
            [1, 2, 6],
            [3, 5],
            []
        ]

        dfs = DepthFirstSearch(adjlist)

        vo = dfs.dfs(1)
        self.assertEqual([1, 5, 6, 3, 2, 4, 0], vo)

