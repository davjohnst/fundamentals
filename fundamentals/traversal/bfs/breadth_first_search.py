#!/usr/bin/env python

from collections import deque

class BreadthFirstSearch(object):

    def __init__(self, adjlist):
        self.adjlist = adjlist

    def bfs(self, root_index):

        queue = deque([root_index])
        visited = [] # keep ordered list to verify visitation order

        while len(queue) != 0:
            current = queue.popleft()
            if not current in visited:
                print "visiting node {0}".format(current)
                visited.append(current)
                for x in self.adjlist[current]:
                    if not x in visited:
                        print "adding {0} to queue".format(x)
                        queue.append(x)

        return visited


if __name__ == "__main__":
    adjlist = [
        [1],
        [0, 4, 5],
        [3, 4, 5],
        [2, 6],
        [1, 2],
        [1, 2, 6],
        [3, 5],
        []
    ]

    bfs = BreadthFirstSearch(adjlist)
    vo = bfs.bfs(1)
    print vo


