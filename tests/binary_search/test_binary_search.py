#!/usr/bin/env python

from unittest import TestCase

from fundamentals.binary_search.binary_search import BinarySearch

class TestBaseSort(TestCase):
    def test_base_sort(self):
        
        to_search = range(0, 100)
        binary_search = BinarySearch()

        self.assertTrue(binary_search.binary_search(to_search, 23L))
        self.assertFalse(binary_search.binary_search(to_search, 101L))
