#!/usr/bin/env python

from unittest import TestCase
from fundamentals.bit_manipulation.nbits_in_int import NBitsInInt
from fundamentals.bit_manipulation.nbits_in_int import BinaryRepresentation

class TestBinary(TestCase):

    def test_nbits(self):
        self.assertEquals(3, NBitsInInt.nbits(7))
        self.assertEquals(8, NBitsInInt.nbits(255))

    def test_binary_rep(self):
        self.assertEquals("1011", BinaryRepresentation.integer_rep(11))
        self.assertEquals("", BinaryRepresentation.integer_rep(0))
        self.assertEquals("11111111", BinaryRepresentation.integer_rep(255))

    def test_decimal_rep(self):
        self.assertEquals(".01", BinaryRepresentation.decimal_rep(0.25))
        self.assertEquals(".1", BinaryRepresentation.decimal_rep(0.5))
        self.assertEquals(".001", BinaryRepresentation.decimal_rep(0.125))

    def test_number_rep(self):
        self.assertEquals("1011.001", BinaryRepresentation.number_rep(11.125))