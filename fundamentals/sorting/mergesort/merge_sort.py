#!/usr/bin/env python

from sorting.base_sort import BaseSort
from math import floor

"""
A divide and conquer algorithm
Full problem: sort the entire array
Sub-problem: sort the array from index p to r

Divide: find the number q midway between p and r
        floor((p+r)/2)
Conquer: recursively sort subarrays [p..q] and [q+1..r]
Combine: merge two sorted arrays back into the single sorted array

Base case: array containing < 2 elements

Average case performance:
 O(n log n)

Best case performance:
 O(n log n)

Worst case performance:
 O(n log n)

"""
class MergeSort(BaseSort):

    def sort(self, nums):
        self.merge_sort(nums, 0L, len(nums) - 1L)


    """ conquer (combine step)"""
    def merge(self, nums, p, q, r):

        p, q, r = int(p), int(q), int(r)

        lows = []
        for i in range(p, q+1L):
            lows.append(nums[i])

        highs = []
        for i in range(q+1L, r+1L):
            highs.append(nums[i])

        i = 0L
        j = 0L
        for k in range(p, r+1L):

            # if lows are used up, take next high
            if i == len(lows):
                nums[k] = highs[j]
                j += 1L
                continue

            # if highs are used up, take next low
            if j == len(highs):
                nums[k] = lows[i]
                i += 1L
                continue

            # if neither lows or highs are used up, compare
            if lows[i] <= highs[j]:
                nums[k] = lows[i]
                i += 1L
            else:
                nums[k] = highs[j]
                j += 1L


    """ divide step : break up big array into two smaller sorted arrays """
    def merge_sort(self, nums, p, r):

        if p < r:
            q = floor((p + r) / 2)
            self.merge_sort(nums, p, q)
            self.merge_sort(nums, q + 1L, r)
            self.merge(nums, p, q, r)
