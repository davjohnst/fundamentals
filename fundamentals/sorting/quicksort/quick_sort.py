#!/usr/bin/env python

import sys
from sorting.base_sort import BaseSort

"""
Quicksort:
invented 1960 by Tony Hoare
Unix default sorting library
divide and conquer algorithm
 - divides a larger array into two smaller arrays:
   - low array
   - high array
 - recursively sort the sub-arrays

Steps:
 - pick an element called a "pivot" from the array
 - reorder the array so that elements less than the pivot
   come before the pivot, elements greater after the pivot
   (after: the pivot is in it's final position)
 - recursively apply the above steps to the sub-array of elements
   lower than and higher than the pivot

Base case:
 sub array length is 0 or 1

Average case performance:
  O(n log n)

Best case performance:
  O(n log n)

Worst case performance:
  O(n^2)

"""
class QuickSort(BaseSort):

    def sort(self, nums):
        self.quicksort(nums, 0, len(nums) - 1)

    def quicksort(self, nums, lo, hi):
        if lo < hi:
            pivot = self.partition(nums, lo, hi)
            self.quicksort(nums, lo, pivot - 1)
            self.quicksort(nums, pivot + 1, hi)

    def partition(self, nums, lo, hi):
        pivot_index, pivot_val = self.choose_pivot(nums, lo, hi)

        # if DEBUG: print "  debug: lo={0}, hi={1}, pivot_index={2}, pivot_val={3}".format(lo, hi, pivot_index, pivot_val)
        self.swap(nums, pivot_index, hi)

        store_index = lo
        for i in range(lo, hi):
            # if DEBUG: print "  debug: i={0}, store_index={1}, array={2}".format(i, store_index, nums)
            if nums[i] <= pivot_val:
                self.swap(nums, i, store_index)
                store_index += 1

        self.swap(nums, store_index, hi)
        return store_index

    @staticmethod
    def swap(nums, ind1, ind2):
        tmp = nums[ind1]
        nums[ind1] = nums[ind2]
        nums[ind2] = tmp
        # if DEBUG: print "  debug swap: {0}".format(nums)

    """ returns [<pivot index>, <pivot value>]"""

    def choose_pivot(self, nums, lo, hi):
        med = (lo + hi) / 2
        lo_val = nums[lo]
        high_val = nums[hi]
        median_val = nums[med]
        pivot_val = self.median_of_three(lo_val, median_val, high_val)

        if pivot_val == lo_val:
            return lo, pivot_val
        elif pivot_val == high_val:
            return hi, pivot_val
        else:
            return med, pivot_val

    @staticmethod
    def median_of_three(uno, dos, tres):
        low = sys.maxint
        high = -sys.maxint - 1
        for val in [uno, dos, tres]:
            if val < low: low = val
            if val > high: high = val

        has_seen_lo = False
        has_seen_hi = False
        for val in [uno, dos, tres]:
            if val == low and not has_seen_lo:
                has_seen_lo = True
                continue
            if val == high and not has_seen_hi:
                has_seen_hi = True
                continue
            return val
