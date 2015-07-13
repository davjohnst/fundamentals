#!/usr/bin/env python

class TrieNode(object):

    def __init__(self, letter, is_terminal=True, children={}, value=None):
        self.letter = letter
        self.is_terminal = is_terminal
        self.children = children
        self.value = value

class Trie(object):

    def __init__(self):
        self.head = TrieNode("", is_terminal=False)

    def contains(self, word):
        current = self.head
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.is_terminal

    def get(self, word):
        current = self.head
        for letter in word:
            if letter not in current.children:
                return None
            current = current.children[letter]
        return current.value

    def put(self, word, value=None):
        current = self.head
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode(letter, is_terminal=False, children={})
                current = current.children[letter]

            else: # letter already has a node
                current = current.children[letter]
        current.is_terminal = True
        current.value = value

    def num_nodes(self):
        return self._num_nodes_under(self.head)

    def _num_nodes_under(self, node):
        # counting the number of nodes under, and including, the `node` argument

        # base case
        if len(node.children) == 0:
            return 1

        # recursive case
        num_under_each_child = [self._num_nodes_under(c) for c in node.children.values()]
        return 1 + sum(num_under_each_child)





def main():
    t = Trie()
    totalnchar = 0
    with open("/usr/share/dict/words", "r") as w:
        for line in w:
            line = line.lower().strip()
            t.put(line)
            totalnchar += len(line)

    print totalnchar
    print t.num_nodes()
    print totalnchar / float(t.num_nodes())


if __name__ == "__main__":
    main()