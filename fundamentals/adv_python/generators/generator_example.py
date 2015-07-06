#!/usr/bin/env python

class GeneratorExample(object):

    @classmethod
    def integer_generator(self, max):
        i = 0
        while i < max:
            yield i
            i += 1

