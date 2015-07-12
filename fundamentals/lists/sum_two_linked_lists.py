#!/usr/bin/env python

from fundamentals.lists.linked_list import LL

class SumLinkedList(object):

    @staticmethod
    def sum_two_linked_lists(ll1, ll2):
        """
        Perform integer addition, where the digits in each integer are represented in a reversed linked list

        For example, 123 + 456
        3 --> 2 --> 1
        6 --> 5 --> 4
        +
        --------------
        9 --> 7 --> 5

        98 + 876
        8 --> 9
        6 --> 7 --> 8
        +
        ---------------
        4 --> 7 --> 9

        :param ll1: head of reversed linked list 1
        :param ll2: head of reversed linked list 2
        :return: head of reversed linked list, representing the integer sum
        """

        result = LL()
        carry = 0

        while ll1 or ll2:

            v1 = ll1.value if ll1 else 0
            v2 = ll2.value if ll2 else 0

            sum = v1 + v2 + carry
            if sum > 9:
                carry = 1
                sum = sum - 10
            else:
                carry = 0

            result.add(sum)

            if ll1:
                ll1 = ll1.next

            if ll2:
                ll2 = ll2.next

        if carry:
            result.add(carry)

        return result.head