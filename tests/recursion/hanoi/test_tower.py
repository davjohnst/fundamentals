#!/usr/bin/env python

from unittest import TestCase

from fundamentals.recursion.hanoi.tower import Tower

class TestTower(TestCase):

    def test_adding(self):
        t = Tower(0, "a")
        t.add(3)
        t.add(2)
        self.assertEqual(2, t.size())

        t.pop()
        t.add(1)
        self.assertEqual(2, t.size())

        try:
            self.add(5)
        except:
            pass

        self.assertEqual(2, t.size())


