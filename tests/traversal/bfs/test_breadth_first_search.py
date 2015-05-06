#!/usr/bin/env python

from unittest import TestCase
from fundamentals.traversal.bfs.breadth_first_search import BreadthFirstSearch

class TestBreadthFirstSearch(TestCase):

    def test_bfs(self):

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

        bfs = BreadthFirstSearch(adjlist)

        vo = bfs.bfs(1)
        self.assertEqual([1, 0, 4, 5, 2, 6, 3], vo)

