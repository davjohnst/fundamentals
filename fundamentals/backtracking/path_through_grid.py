#!/usr/bin/env python

"""
Imagine a robot sitting in the upper left hand corner of a grid.
It can move Right and Down.
The grid may have roadblocks (0's)
Find a path, if one exists, for the robot to traverse from its starting
point to the bottom right hand corner of the grid.
"""

class PathThroughGrid(object):

    def __init__(self, grid):
        self.grid = grid

    def get_path(self):
        visited = set()
        path = []
        x = len(self.grid) - 1
        y = len(self.grid[0]) - 1
        is_path = self._get_path(x, y, self.grid, visited, path)
        return path if len(path) > 0 else None

    def _get_path(self, x, y, grid, visited, path):
        """
        Get a path from grid[x, y] to the starting point (1, 1).
        Return True if there's a path, and append the path to the `path` arg
        Return False otherwise (and don't append anything)

        :param x: x
        :param y: y
        :param grid: static grid
        :param visited: don't traverse to the same node twice
        :param path: recursively build the path
        :return: True if there is a valid path
        """

        if x < 0 or y < 0:
            return False

        if grid[x][y] == 0:
            return False

        if x == 0 and y == 0:
            path.append((x, y))
            return True

        if (x-1, y) not in visited:
            visited.add((x-1, y))
            if self._get_path(x-1, y, grid, visited, path):
                path.append((x, y))
                return True

        if (x, y-1) not in visited:
            visited.add((x, y-1))
            if self._get_path(x, y-1, grid, visited, path):
                path.append((x, y))
                return True

        return False

def main():
    grid = [
        [1, 1, 0],
        [1, 0, 1],
        [0, 0, 1]
    ]

    ptg = PathThroughGrid(grid)
    print ptg.get_path()




if __name__ == "__main__":
    main()