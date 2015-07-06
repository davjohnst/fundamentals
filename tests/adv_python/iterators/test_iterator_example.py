#!/usr/bin/env python

from unittest import TestCase
from fundamentals.adv_python.iterators.iterator_example import IteratorExample

class TestIteratorExample(TestCase):

    def test_default_iter(self):

        ie = IteratorExample([1, 2, 3, 4, 5])
        default_it = ie.get_default_iterator()
        val = default_it.next()
        self.assertEqual(1, val)

        sum = 0
        for x in default_it:
            sum += x

        self.assertEqual(14, sum)

    def test_backwards_iter(self):

        ie = IteratorExample([2, 4, 6, 8])

        backwards_it = ie.get_backwards_iterator()
        self.assertEqual(8, backwards_it.next())
        self.assertEqual(6, backwards_it.next())
        self.assertEqual(4, backwards_it.next())
        self.assertEqual(2, backwards_it.next())
        with self.assertRaises(StopIteration):
            backwards_it.next()


