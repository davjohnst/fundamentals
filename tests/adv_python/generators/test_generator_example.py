#!/usr/bin/env python

from unittest import TestCase
from fundamentals.adv_python.generators.generator_example import GeneratorExample

class TestGeneratorExample(TestCase):

        def test_generator_example(self):

            f = GeneratorExample.integer_generator(3)
            self.assertEquals(0, f.next())
            self.assertEquals(1, f.next())
            self.assertEquals(2, f.next())
            with self.assertRaises(StopIteration):
                f.next()