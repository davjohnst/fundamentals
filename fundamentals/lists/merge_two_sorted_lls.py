#!/usr/bin/env python

from fundamentals.lists.linked_list import LL

class MergeTwoSortedLLs(object):

    @staticmethod
    def merge_two_sorted_lls(ll1, ll2):
        """
        Merge two sorted link lists into a new, combined, sorted linked list

        Example:
        1 --> 2 --> 3
        2 --> 2 --> 4

        returns:
        1 --> 2 --> 2 --> 2 --> 3 --> 4


        :param ll1: a sorted linked list
        :param ll2: a sorted linked list
        :return: a new, combined, sorted linked list
        """

        result = LL()

        while ll1 and ll2:
            if ll1.value <= ll2.value:
                result.add(ll1.value)
                ll1 = ll1.next
            else:
                result.add(ll2.value)
                ll2 = ll2.next

        # at least one list is now exhausted, let's speed through the rest
        if ll1:
            while ll1:
                result.add(ll1.value)
                ll1 = ll1.next

        if ll2:
            while ll2:
                result.add(ll2.value)
                ll2 = ll2.next

        return result.head



