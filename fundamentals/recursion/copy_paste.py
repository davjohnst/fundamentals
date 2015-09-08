#!/usr/bin/env python

from fundamentals.adv_python.context_management.cm_examples import time_print

"""
You have four keys at your disposal.
You can type keys 'n' times.
You want to maximize the number of characters in your 'text editor'

Keys:
 - type an 'a'
 - select all
 - copy
 - append paste buffer
"""

# recursive...
class CopyPaste(object):
    def __init__(self, n):
        self.n = n

    def max_len(self):

        if self.n < 1:
            raise ValueError("must be positive")

        return self._max_len(self.n, 0, 0, 0)

    def _max_len(self, moves_left, len_copy, len_sel, len_text):
        if moves_left == 0:
            return len_text

        # type an 'a'
        nchar_a = self._max_len(moves_left - 1, len_copy, len_sel, len_text + 1)

        # type 'select-all'
        nchar_s = self._max_len(moves_left - 1, len_copy, len_text, len_text)

        # type 'copy'
        nchar_c = self._max_len(moves_left - 1, len_sel, len_sel, len_text)

        # type 'paste'
        nchar_p = self._max_len(moves_left - 1, len_copy, len_sel, len_text + len_copy)

        return max(nchar_a, nchar_s, nchar_c, nchar_p)


class CopyPasteDP(object):
    def __init__(self, n):
        self.n = n
        self.memo_table = {}

    def max_len(self):

        if self.n < 1: 
            raise ValueError("must be positive")

        return self._max_len(self.n, 0, 0, 0)

    def _max_len(self, moves_left, len_copy, len_sel, len_text):
        if moves_left == 0:
            return len_text

        subproblem_tuple = (moves_left, len_copy, len_sel, len_text)
        if subproblem_tuple in self.memo_table:
            return self.memo_table[subproblem_tuple]

        # type an 'a'
        nchar_a = self._max_len(moves_left - 1, len_copy, len_sel, len_text + 1)

        # type 'select-all'
        nchar_s = self._max_len(moves_left - 1, len_copy, len_text, len_text)

        # type 'copy'
        nchar_c = self._max_len(moves_left - 1, len_sel, len_sel, len_text)

        # type 'paste'
        nchar_p = self._max_len(moves_left - 1, len_copy, len_sel, len_text + len_copy)

        max_chars = max(nchar_a, nchar_s, nchar_c, nchar_p)

        self.memo_table[subproblem_tuple] = max_chars
        return max_chars



def main():
    print CopyPaste(1).max_len()
    print CopyPaste(6).max_len()
    print CopyPaste(7).max_len()
    print CopyPaste(8).max_len()

    with time_print("recursive 11"):
        print CopyPaste(11).max_len()

    with time_print("dynamic programming 11"):
        print CopyPasteDP(11).max_len()


if __name__ == "__main__":
    main()