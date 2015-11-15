#!/usr/bin/env python

from fundamentals.adv_python.context_management.cm_examples import time_print

"""
Given an amount of money, a set of coin denominations, and an unlimited number of coins in those
denominations, how many different sets of coins could be used to pay the amount?

Define:
 m: the number of denominations
 N: the amount to make change for
 S_0, ..., S_m-1: the ordered set of denominations

 C(N, m) = the number of ways to make change for N using coin values S_0, ..., S_m-1

 E.g., $2.00 using denominations 1.00, 0.50, 0.25

 C(2.0, [1, 0.5, 0.25]) = C(1.0, [1, 0.5, 0.25) + C(2.0, [0.5, 0.25])

 We always spend coins in largest to smallest order to maintain set invariant.
 E.g., 7 = 1, 5, 1 or 1, 1, 5 or 5, 1, 1 (all one set of two pennies and a nickel paid)

"""

class CoinChange(object):

    def __init__(self, denominations):
        self.denominations = sorted(denominations, reverse=True)


    def nways_to_make_change(self, amount):
        return self._nways_to_make_change(amount, len(self.denominations))


    def _nways_to_make_change(self, amount, k):
        """
        :param amount: amount to make change for
        :param k: make change using no denominations smaller than denominations[k-1]
        :return: number of ways to make change of $(amount) using denominations[0, ..., k-1]
        """

        # base cases:

        # there's only one way to make change for 0
        if amount == 0:
            return 1

        # there's no way to make negative change
        if amount < 0:
            return 0

        # there's no way to make change for a positive amount of money using *no* coins
        if amount >= 1 and k <= 0:
            return 0

        # apply recursion:
        # C(N, k) = C(N-S[k], k) + C(N, k-1)
        return self._nways_to_make_change(amount - self.denominations[k - 1], k) + \
               self._nways_to_make_change(amount, k - 1)


    def nways_to_make_changeDP(self, amount):
        # DP_matrix: rows for partial amounts [0, amount]
        #            cols for max denomination [0, len(denomination)-1]
        partial_results = {}

        for k in xrange(len(self.denominations)):
            partial_results[(0, k)] = 1

        return self._nways_to_make_changeDP(amount, len(self.denominations), partial_results)


    def _nways_to_make_changeDP(self, amount, k, partial_results):
        for N in xrange(1, amount + 1):
            for pk in xrange(0, k):
                # count of solutions including D[pk]
                x = partial_results[(N - self.denominations[pk], pk)] if N - self.denominations[pk] >= 0 else 0
                # count of solutions excluding D[pk]
                y = partial_results[(N, pk-1)] if pk >= 1 else 0
                partial_results[(N, pk)] = x + y


        return partial_results[amount, k-1]


def main():
    c = CoinChange([1, 5, 10])

    for x in xrange(0, 11):
        print "{0}, nways: {1}".format(x, c.nways_to_make_change(x))

    for x in xrange(0, 11):
        print "{0}, nwaysDP: {1}".format(x, c.nways_to_make_changeDP(x))

    with time_print("recursive") as tpr:
        print c.nways_to_make_change(400)

    with time_print("dp") as tpd:
        print c.nways_to_make_changeDP(400)



if __name__ == "__main__":
    main()