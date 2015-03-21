#!/usr/bin/env python

from unittest import TestCase

from fundamentals.sorting.mergesort.merge_sort import MergeSort

class TestMergeSort(TestCase):

    def test_merging(self):
        merge_sort = MergeSort()

        nums = [3, 1, 4, 2, 0]
        merge_sort.merge(nums, 1, 2, 3)
        self.assertEquals([3, 1, 2, 4, 0], nums)

        nums = [9, 8, 5, 6, 7, 3, 4, 2, 1, 0]
        merge_sort.merge(nums, 2, 4, 6)
        self.assertEquals([9, 8, 3, 4, 5, 6, 7, 2, 1, 0], nums)


    def test_merge_sort(self):

        to_sort = [3, 1, 2, 4, 5]
        merge_sort = MergeSort()
        merge_sort.sort(to_sort)

        self.assertEquals([1, 2, 3, 4, 5], to_sort)


