#!/usr/bin/env python

"""
The purpose of this file is simply to try out various bit manipulation techniques in Python
"""

import string

def main():
    print "1101_2 in base10:", int('1101', 2)
    print "13 in base 2: {:#b}".format(13)
    print "-10 in base 2: {:#b}".format(-10)
    print "13 in hex: {:#x}".format(13)
    print "255 in hex: 0x%x" % 255
    print "1110110 in base 10:", int('1110110', 2)
    print "118 in ascii:", chr(118)
    print "ascii 'v' as integer:", ord("v")
    print "0xff as integer:", int('0xff', 16)
    for i in xrange(3, 5):
        print "2^{0} = {1}".format(i, 1 << i)

if __name__ == "__main__":
    main()