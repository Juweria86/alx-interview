#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """calculates the fewest number of operations needed to
    result in exactly n H characters in the file."""

    if n <= 1:
        return 0
    op = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            op += factor
            n //= factor
        factor += 1

    return op
