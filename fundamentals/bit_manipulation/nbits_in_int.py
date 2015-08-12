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
    def integer_rep(n):
        """
        :param n: a non-negative integer
        :return: string representation of it's binary value,
           e.g., 2 --> "10"
                 255 --> "11111111"
        """
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

    @staticmethod
    def decimal_rep(dec):
        """
        :param dec: a decimal value between 0 and 1
        :return: a string representation of it's binary value
           e.g., 0.5 --> ".1"
                 0.25 -> ".01"
                 0.75 -> ".11"
        """
        if dec <= 0 or dec >= 1:
            raise ValueError("input must be a decimal between 0 and 1")

        results = ["."]

        while dec > 0 and len(results) <= 32:
            dec *= 2
            if dec >= 1.0:
                results.append("1")
                dec -= 1.0
            else:
                results.append("0")

        return "".join(results)

    @staticmethod
    def number_rep(num):
        """
        :param num: a non-negative real number
        :return: a string representation of it's binary value
           e.g., 11.25 --> "1011.01"
        """

        wholenum = int(num)
        dec = num - float(wholenum)

        return "{0}{1}".format(BinaryRepresentation.integer_rep(wholenum), BinaryRepresentation.decimal_rep(dec))


def main():
    print NBitsInInt.nbits(7)
    print NBitsInInt.nbits(255)
    print "-" * 20
    print BinaryRepresentation.integer_rep(7)
    print BinaryRepresentation.integer_rep(11)
    print "-" * 20
    print BinaryRepresentation.decimal_rep(0.5)
    print BinaryRepresentation.decimal_rep(0.25)
    print BinaryRepresentation.decimal_rep(0.75)
    print "-" * 20
    print BinaryRepresentation.number_rep(11.25)



if __name__ == "__main__":
    main()