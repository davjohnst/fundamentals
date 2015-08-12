#!/usr/bin/env python

from unittest import TestCase
from fundamentals.bit_manipulation.nbits_in_int import NBitsInInt
from fundamentals.bit_manipulation.nbits_in_int import BinaryRepresentation

class TestBinary(TestCase):

    def test_nbits(self):
        self.assertEquals(3, NBitsInInt.nbits(7))
        self.assertEquals(8, NBitsInInt.nbits(255))

    def test_binary_rep(self):
        self.assertEquals("1011", BinaryRepresentation.binary_rep(11))
        self.assertEquals("", BinaryRepresentation.binary_rep(0))
        self.assertEquals("11111111", BinaryRepresentation.binary_rep(255))