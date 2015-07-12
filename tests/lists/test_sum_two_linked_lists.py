#!/usr/bin/env python

from unittest import TestCase
from fundamentals.lists.linked_list import LL
from fundamentals.lists.sum_two_linked_lists import SumLinkedList

class TestSumLinkedList(TestCase):

    def test_sum(self):
        ll1 = LL()
        ll1.add(9).add(8).add(7)

        ll2 = LL()
        ll2.add(8).add(9).add(9)

        result = SumLinkedList.sum_two_linked_lists(ll1.head, ll2.head)

        self.assertEquals("7, 8, 7, 1", result.pretty_walk())

    def test_ragged(self):
        ll1 = LL()
        ll1.add(1).add(1).add(1).add(1)

        ll2 = LL()
        ll2.add(2).add(2)

        result = SumLinkedList.sum_two_linked_lists(ll1.head, ll2.head)

        self.assertEquals("3, 3, 1, 1", result.pretty_walk())

        result = SumLinkedList.sum_two_linked_lists(ll2.head, ll1.head)

        self.assertEquals("3, 3, 1, 1", result.pretty_walk())

