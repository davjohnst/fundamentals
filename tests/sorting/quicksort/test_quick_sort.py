#!/usr/bin/env python

from unittest import TestCase

from fundamentals.sorting.quicksort.quick_sort import QuickSort

class TestQuickSort(TestCase):
    def test_quick_sort(self):

        to_sort = [3, 1, 2, 4, 5]
        quick_sort = QuickSort()
        quick_sort.sort(to_sort)

        self.assertEquals([1, 2, 3, 4, 5], to_sort)

