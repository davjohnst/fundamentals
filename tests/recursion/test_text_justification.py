#!/usr/bin/env python

from unittest import TestCase
from fundamentals.recursion.text_justification import TextJustification

class TestTextJustification(TestCase):

    def testTextJustification(self):
        text = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
        expected = "\n".join(["the quick", "brown fox", "jumped", "over the", "lazy dog"])
        self.assertEquals(expected, TextJustification(10).justify(text))

    def testBadInput(self):
        with self.assertRaises(ValueError):
            TextJustification(10).justify(["here's a word", "larger", "than", "10"])



