#!/usr/bin/env python

from unittest import TestCase

from fundamentals.sorting.base_sort import BaseSort

class TestBaseSort(TestCase):
    def test_base_sort(self):
        
        to_sort = [3, 1, 2, 4, 5]
        base_sort = BaseSort()
        base_sort.sort(to_sort)
        
        self.assertEquals([1, 2, 3, 4, 5], to_sort)
        
