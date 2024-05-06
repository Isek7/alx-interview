#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, isek = 0, 2
    while isek <= n:
        # if n evenly divides by isek
        if n % isek == 0:
            # total even-divisions by isek = total operations
            ops += isek
            # set n to the remainder
            n = n / isek
            # reduce isek to find remaining smaller vals that evenly-divide n
            isek -= 1
        # increment isek until it evenly-divides n
        isek += 1
    return ops
