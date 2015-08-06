#!/usr/bin/env python

class BSTNode(object):

    def __init__(self, parent, left, right, value):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value

class BST(object):

    def __init__(self):
        self.root = None

    def put(self, val):
        if self.root is None:
            self.root = BSTNode(None, None, None, val)
        else:
            self._put(val, self.root)

    def _put(self, val, current_node):
        if val < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(current_node, None, None, val)
            else:
                self._put(val, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = BSTNode(current_node, None, None, val)
            else:
                self._put(val, current_node.right)

    def contains(self, val):
        current_node = self.root
        while current_node is not None:
            if current_node.value == val:
                return True
            elif val < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return False

    def pre_order_traversal(self, func):
        self._pre_order_traversal(self.root, func)

    def _pre_order_traversal(self, node, func):
        if node is not None:
            func(node)

            if node.left is not None:
                self._pre_order_traversal(node.left, func)

            if node.right is not None:
                self._pre_order_traversal(node.right, func)


def main():
    b = BST()
    b.put(10)
    b.put(4)
    b.put(14)
    b.put(2)
    b.put(1)

    def print_val(node):
        print node.value

    b.pre_order_traversal(print_val)

    print b.contains(1)
    print b.contains(3)


if __name__ == "__main__":
    main()