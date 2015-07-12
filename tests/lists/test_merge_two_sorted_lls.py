#!/usr/bin/env python

from unittest import TestCase
from fundamentals.lists.linked_list import LL
from fundamentals.lists.merge_two_sorted_lls import MergeTwoSortedLLs

class TestMergeTwoSortedLLs(TestCase):

    def test_merge(self):
        ll1 = LL()
        ll1.add(1).add(2).add(3)
        ll2 = LL()
        ll2.add(2).add(2).add(4)

        result = MergeTwoSortedLLs.merge_two_sorted_lls(ll1.head, ll2.head)
        self.assertEquals("1, 2, 2, 2, 3, 4", result.pretty_walk())