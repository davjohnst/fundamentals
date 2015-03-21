#!/usr/bin/env python

from math import floor

class BinarySearch(object):


    def binary_search(self, nums, query):

        lo = 0
        hi = len(nums)

        while True:
            mid = int(floor((lo + hi) / 2))

            if mid == lo or mid == hi:
                return nums[mid] == query

            if nums[mid] == query:
                return True
            elif nums[mid] > query:
                hi = mid
            else:
                lo = mid
