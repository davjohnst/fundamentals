#!/usr/bin/env python

from unittest import TestCase
from fundamentals.dicts.grab_scrab import GrabScrab

class TestGrabScrab(TestCase):

    def test_grab_scrab(self):
        self.assertTrue(GrabScrab.is_steal("abc", "abcd"))
        self.assertTrue(GrabScrab.is_steal("loon", "moonlight"))
        self.assertFalse(GrabScrab.is_steal("dog", "god"))
        self.assertFalse(GrabScrab.is_steal("sally", "sally"))
        self.assertTrue(GrabScrab.is_steal("lop", "loop"))
        self.assertFalse(GrabScrab.is_steal("camp", "pam"))