#!/usr/bin/env python

from tower import Tower


"""
The classic Towers of Hanoi problem,
implements a solution using recursion.
runtime: O(2^n)
space: O(n)
"""
class Hanoi(object):

    def __init__(self, n):

        # stack starts on tower A
        self.towerA = Tower(n, "A")
        self.towerB = Tower(0, "B")
        self.towerC = Tower(0, "C")


    def _move(self, ndiscs, towerFrom, towerAux, towerTo):

        if ndiscs == 0:
            return

        else:
            # move n-1 discs to the auxiliary tower
            self._move(ndiscs - 1, towerFrom, towerTo, towerAux)

            # move nth disc from the source tower to the destination tower
            val = towerFrom.pop()
            towerTo.add(val)

            # move n-1 discs from the auxiliary tower to the destination tower
            self._move(ndiscs - 1, towerAux, towerFrom, towerTo)


    def run(self):
        self._move(self.towerA.size(), self.towerA, self.towerB, self.towerC)


if __name__ == "__main__":
    h = Hanoi(4)
    h.run()


