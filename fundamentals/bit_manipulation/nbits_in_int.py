#!/usr/bin/env python

class NBitsInInt(object):

    @staticmethod
    def nbits(n):
        if n < 0:
            raise ValueError("n should be positive")

        nbits = 0
        while n > 0:
            nbits += 1
            n = n >> 1

        return nbits

class BinaryRepresentation(object):

    @staticmethod
    def binary_rep(n):
        if n < 0:
            raise ValueError("let's not think about negative numbers yet")

        results = []
        nbits = NBitsInInt.nbits(n)

        # from (nbits - 1) to 0...
        for i in xrange(nbits - 1, -1, -1):

            # leftmost digit is a 1 if n is greater than 2^i
            results.append("1" if n >= (1 << i) else "0")

            # mask the most significant digit to 0
            n &= ((1 << i) - 1)

        return "".join(results)




def main():
    print NBitsInInt.nbits(7)
    print NBitsInInt.nbits(255)

    print BinaryRepresentation.binary_rep(7)
    print BinaryRepresentation.binary_rep(11)


if __name__ == "__main__":
    main()