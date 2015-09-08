#!/usr/bin/env python


class AllPermutations(object):

    def __init__(self, arr):
        self.arr = arr

    def all_permutations(self):
        results = []
        used = []
        self._all_permutations(self.arr, used, results)
        return results

    def _all_permutations(self, to_use, used, results):
        if len(to_use) == 0:
            results.append(used)

        for i, x in enumerate(to_use):
            new_used = used + [x]
            new_to_use = to_use[:i] + to_use[i+1:]
            self._all_permutations(new_to_use, new_used, results)


def main():
    arr = [1, 2, 3, 4]
    ap = AllPermutations(arr)
    results = ap.all_permutations()
    for x in results:
        print x
    print len(results)


if __name__ == "__main__":
    main()