#!/usr/bin/env python

from unittest import TestCase
from fundamentals.stacks.sort_using_stack import StackSort

class TestStackSort(TestCase):

    def test_stack_sort(self):

        a = [3, 6, 8, 2, 78, 1, 23, 45, 9]
        b = a[:]
        std = StackSort.sortStack(a)
        true_std = sorted(b)

        self.assertEquals(true_std, std)




def main():
    pass


if __name__ == "__main__":
    main()