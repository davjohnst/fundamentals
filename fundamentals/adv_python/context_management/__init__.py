#!/usr/bin/env python

import contextlib
import time

""" Manually create a context manager """
class ContextManagementExample(object):

    def __enter__(self):
        print "Entering..."

    def __exit__(self, *args):
        print "Exiting..."

""" Decorator pattern abstracts away context management in an easy wrapper """
@contextlib.contextmanager
def time_print(task_name):
    t = time.time()
    try:
        yield
    finally:
        print task_name, "took", time.time() - t, "seconds."


def main():
    with ContextManagementExample() as cme:
        print "doing some work..."

    with time_print("sleeping") as tp:
        time.sleep(0.5)


if __name__ == "__main__":
    main()