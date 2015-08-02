#!/usr/bin/env python

from unittest import TestCase
from fundamentals.binary_search_tree.binary_search_tree import BST

class TestBST(TestCase):

    def test_bst(self):
        b = BST()
        b.put(10)
        b.put(4)
        b.put(14)
        b.put(2)
        b.put(3)
        b.put(1)
        b.put(15)

        pre_order = []
        def add_to_pre_order(node):
            pre_order.append(node.value)
        b.pre_order_traversal(add_to_pre_order)
        self.assertEquals([10, 4, 2, 1, 3, 14, 15], pre_order)