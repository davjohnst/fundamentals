#!/usr/bin/env python

class GrabScrab(object):

    @staticmethod
    def is_steal(original, steal):

        if len(original) == len(steal):
            return False

        steal_map = {}
        for letter in steal:
            steal_map[letter] = steal_map.get(letter, 0) + 1

        for letter in original:
            steal_map[letter] = steal_map.get(letter, 0) - 1
            if steal_map[letter] < 0:
                return False

        return True


def main():
    print GrabScrab.is_steal("abc", "abcd")
    print GrabScrab.is_steal("loon", "moonlight")
    print GrabScrab.is_steal("dog", "god")
    print GrabScrab.is_steal("sally", "sally")
    print GrabScrab.is_steal("lop", "loop")
    print GrabScrab.is_steal("camp", "pam")


if __name__ == "__main__":
    main()