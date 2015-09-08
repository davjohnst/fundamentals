#!/usr/bin/env python

"""
Generates all 2^n subsets of an array using backtracking.
TODO: backtrack using bit arrays instead of input array
"""
class AllSubsets(object):

    def __init__(self, arr):
        self.arr = arr

    def all_subsets(self):
        results = []
        self._all_subsets(self.arr, [], results)
        return results

    def _all_subsets(self, unprocessed, processed, results):

        if len(unprocessed) == 0:
            results.append(processed)
            return

        # include next element
        self._all_subsets(unprocessed[1:], processed + [unprocessed[0]], results)
        # exclude next element
        self._all_subsets(unprocessed[1:], processed, results)


def main():
    arr = [1, 2, 3, 4, 5]
    all_subs = AllSubsets(arr)
    all_subsets = all_subs.all_subsets()
    for x in all_subsets:
        print x
    print len(all_subsets)



if __name__ == "__main__":
    main()