#!/usr/bin/env python

from fundamentals.adv_python.context_management.cm_examples import time_print

"""
Problem:

A child is running up a staircase with n steps, and can hop either 1 step, 2 steps or 3 steps
at a time.  Implement a method to count mow many possible ways the child can run up the stairs.
"""

class NWaysUpStairs(object):

    """
    Phase 1: Build as a recursive problem

      Base case: n < 0: 0
                 n = 0: 1

      Recursive: n = 1: nways(0) then 1 step
                 n = 2: nways(0) then 2 steps, OR nways(1) then 1 step
                        nways(0) + nways(1)
                 n = 3: nways(0) then 3 steps, OR nways(1) then 2 steps, OR nways(2) then 1 step

    Phase 2: Notice repeated subproblems, incorporate memoization for a dynamic programming solution
    """

    @staticmethod
    def nways_rec(n):

        if n < 0:
            return 0

        if n == 0:
            return 1

        else:
            return NWaysUpStairs.nways_rec(n-3) + NWaysUpStairs.nways_rec(n-2) + NWaysUpStairs.nways_rec(n-1)

    @staticmethod
    def _nways_dp(n, memoized):

        if n < 0:
            return 0

        if len(memoized) >= (n+1):
            return memoized[n]

        nwaysn = NWaysUpStairs._nways_dp(n-3, memoized) + NWaysUpStairs._nways_dp(n-2, memoized) + \
                 NWaysUpStairs._nways_dp(n-1, memoized)
        memoized.append(nwaysn)
        return nwaysn

    @staticmethod
    def nways_dp(n):
        return NWaysUpStairs._nways_dp(n, [1])


def main():
    with time_print("recursive nways"):
        print NWaysUpStairs.nways_rec(20)

    with time_print("dynamic programming nways"):
        print NWaysUpStairs.nways_dp(20)


if __name__ == "__main__":
    main()