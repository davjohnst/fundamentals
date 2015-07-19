#!/usr/bin/env python

from fundamentals.adv_python.context_management.cm_examples import time_print

class SlowFibonacci(object):
    """
     Slow recursive implementation of calculating the Fibonacci sequence, for comparison's sake
    """

    @staticmethod
    def fib(n):

        if n < 0:
            raise ValueError("n can't be less than 0")

        if n == 0:
            return 0

        if n == 1:
            return 1

        return SlowFibonacci.fib(n-1) + SlowFibonacci.fib(n-2)

class DPFibonacci(object):
    """
    Fast dynamic programming implementation of calculating the Fibonacci sequence
    """

    @staticmethod
    def fib(n):
        return DPFibonacci._fib(n, [0, 1])

    @staticmethod
    def _fib(n, fib_solved):

        if n < 0:
            raise ValueError("n can't be less than 0")

        if len(fib_solved) >= (n+1):
            return fib_solved[n]

        else:
            fibn = DPFibonacci._fib(n - 2, fib_solved) + DPFibonacci._fib(n - 1, fib_solved)
            fib_solved.append(fibn)
            return fibn


def main():
    print SlowFibonacci.fib(6)

    with time_print("slow fib"):
        print SlowFibonacci.fib(32)

    print DPFibonacci.fib(6)

    with time_print("dp fib"):
        print DPFibonacci.fib(32)



if __name__ == "__main__":
    main()