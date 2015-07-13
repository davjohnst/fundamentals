#!/usr/bin/env python

from unittest import TestCase
from fundamentals.trie.trie import Trie


class TestTrie(TestCase):

    def test_trie(self):
        t = Trie()
        self.assertFalse(t.contains("abc"))
        t.put("abc", 3)
        self.assertTrue(t.contains("abc"))
        self.assertFalse(t.contains("ab"))
        self.assertFalse(t.contains("abcd"))
        self.assertEquals(3, t.get("abc"))
        self.assertEquals(None, t.get("ab"))
        self.assertEquals(None, t.get("abcd"))

    def test_trie_count(self):
        t = Trie()
        self.assertEquals(1, t.num_nodes())
        t.put("abc")
        self.assertEquals(4, t.num_nodes())