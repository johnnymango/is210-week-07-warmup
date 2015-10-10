#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The module perform lexicographical analysis. """

import decimal
decimal.getcontext().prec = 3

def lexicographics(to_analyze):
    """This function calculates the max, min and average values of strings.

    Args:
        to_analyze (string): a sequence of strings separated by new lines.

    Returns:
        Tuple: the length of the longest string, the the length of the shortest
        string, the average number of words per string.

    Examples:
        >>> lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal(4.0))

        >>> lexicographics('''You better run,
        you better do what you can,
        Don't wanna see no blood,
        don't be a macho man
        You wanna be tough,
        better do what you can,
        So beat it,
        but you wanna be bad''')
        (6, 3,  Decimal(4.5))
    """
    myvalues = []
    lines = to_analyze.split('\n')
    for items in lines:
        values = len(items.split())
        myvalues.append(values)
    return max(myvalues), min(myvalues), sum(myvalues) / decimal.Decimal(len(
        lines))

