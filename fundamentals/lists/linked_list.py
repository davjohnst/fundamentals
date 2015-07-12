#!/usr/bin/env python

class LL_node(object):

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def walk(self):
        current = self
        while current:
            yield current.value
            current = current.next

    def pretty_walk(self):
        return ", ".join([str(x) for x in self.walk()])

class LL(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        node = LL_node(value, None)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        return self

    def iterative_reverse_ll(self):
        current = self.head
        new = None
        while current:
            new = LL_node(current.value, new)
            current = current.next

        return new

    def recursive_reverse_ll(self):
        head, tail = self._visit(self.head)
        return head

    def _visit(self, node):

        # base case
        if not node.next:
            head = LL_node(node.value, None)
            return head, head

        # recursive case
        else:
            (head, current) = self._visit(node.next)
            new = LL_node(node.value, None)
            current.next = new
            return head, new

    def delkey(self, keyval):
        """ Removes the first instance of keyval in the linked list, if it exists """

        if self.head.value == keyval:
            self.head = self.head.next
            return self

        current = self.head
        while current.next:
            if current.next.value == keyval:
                nextnext = current.next.next
                current.next.next = None
                current.next = nextnext

                # if nextnext is a termination
                if not nextnext:
                    tail = current

                return self

            current = current.next



def main():

    ll = LL()
    ll.add(3).add(4).add(5).add(6)

    print ll.head.pretty_walk()
    print ll.iterative_reverse_ll().pretty_walk()
    print ll.recursive_reverse_ll().pretty_walk()



if __name__ == "__main__":
    main()