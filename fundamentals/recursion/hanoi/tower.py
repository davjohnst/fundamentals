#!/usr/bin/env python

class Tower(object):

    def __init__(self, n, tower_name):

        if n < 0:
            raise ValueError("n must be 0 or greater")

        self.stack = [x + 1 for x in range(n)][::-1]
        self.tower_name = tower_name


    def size(self):
        return len(self.stack)


    def add(self, value):

        if self.size() == 0 or self.stack[-1] > value:
            prev = self.stack[-1] if self.size() > 0 else "[empty]"
            print "[Tower {0}] stacking a {1} on top of a {2}".format(self.tower_name, value, prev)
            self.stack.append(value)
            return

        raise ValueError("must stack smaller values over bigger values")


    def pop(self):

        if self.size() == 0:
            raise ValueError("can't pop when tower has 0 elements")

        popped = self.stack.pop()
        print "[Tower {0}] popping {1}".format(self.tower_name, popped)
        return popped


    def to_string(self):
        return str(self.stack)


if __name__ == "__main__":
    t = Tower(3, "a")
    t.pop()
    t.pop()
    t.add(1)
    print t.to_string()
