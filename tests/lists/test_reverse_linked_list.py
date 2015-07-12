#!/usr/bin/env python

from unittest import TestCase
from fundamentals.lists.linked_list import LL

class TestLL(TestCase):

    def test_rev_ll(self):
        ll = LL()
        ll.add(3).add(4).add(5).add(6)
        self.assertEquals("3, 4, 5, 6", ll.head.pretty_walk())
        self.assertEquals("6, 5, 4, 3", ll.recursive_reverse_ll().pretty_walk())
        self.assertEquals("6, 5, 4, 3", ll.iterative_reverse_ll().pretty_walk())

    def test_del(self):
        ll = LL()
        ll.add(3).add(4).add(5).add(6)
        self.assertEquals("3, 4, 5, 6", ll.head.pretty_walk())
        ll.delkey(3)
        self.assertEquals("4, 5, 6", ll.head.pretty_walk())
        ll.delkey(10)
        self.assertEquals("4, 5, 6", ll.head.pretty_walk())
        ll.delkey(5)
        self.assertEquals("4, 6", ll.head.pretty_walk())
        ll.delkey(6)
        self.assertEquals("4", ll.head.pretty_walk())


