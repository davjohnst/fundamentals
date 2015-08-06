#!/usr/bin/env python

class StackSort(object):

    """
    Write a program to sort a stack in ascending order with the biggest items on top.
     You may use additional stacks to hold items, but can't use other data structures.
     Your api: push, pop, peek, isEmpty

     ex:      bottom of stack ---->   top of stack

     [3, 4, 1, 5, 2]
     sorts to
     [1, 2, 3, 4, 5]

    """

    @staticmethod
    def sortStack(input_stack):

        output_stack = []
        tmp = []
        while input_stack:
            next = input_stack.pop()
            if len(output_stack) == 0 or output_stack[-1] <= next:
                output_stack.append(next)
            else:
                while len(output_stack) > 0:
                    if output_stack[-1] > next:
                        t = output_stack.pop()
                        tmp.append(t)
                    else:
                        break
                output_stack.append(next)
                while len(tmp) > 0:
                    output_stack.append(tmp.pop())

        return output_stack


def main():
    stack = [3, 4, 1, 5, 2]
    print StackSort.sortStack(stack)


if __name__ == "__main__":
    main()