#!/usr/bin/env python

"""
Iterators have a next() method, and when there's nothing left to return, raises `StopIteration` exception
  - Allows looping just once
  - Holds the state of a single iteration
"""

class IteratorExample(object):

    def __init__(self, nums):
        self.nums = nums

    def get_default_iterator(self):
        return self.nums.__iter__()

    def get_backwards_iterator(self):
        return self.BackwardsIterator(self.nums)

    class BackwardsIterator(object):
        def __init__(self, nums):
            self.nums = nums
            self.index = len(nums) - 1

        def next(self):
            if self.index < 0:
                raise StopIteration
            else:
                self.index -= 1
                return self.nums[self.index + 1]
