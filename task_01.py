#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""My Fibonacci Sequence."""


def fibonacci(maxint):
    """This function creates a Fibonacci sequence.

    Args:
        maxint (int): The upper boundary of the Fibonacci sequence.

    Returns:
        List: The list of Fibonacci numbers up to but not including the upper
        boundary.

    Examples:

    >>> fibonacci(21)
    [0, 1, 1, 2, 3, 5, 8, 13]

    >>> fibonacci(22)
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    fiblist = [0, ]
    mya, myb = 0, 1
    while myb < maxint:
        fiblist.append(myb)
        mya, myb = myb, mya + myb
    return fiblist
