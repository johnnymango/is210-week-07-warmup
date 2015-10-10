#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Truthy If Statements."""


def bool_to_str(bval):
    """This function checks a truthiness using If Else statment.

    Args:
        bval (mixed): a boolean or boolean-like value that can be evaluated
        for truthiness or falsiness.

    Returns:
        String: Yes to Truthy values and No to Falsy Values.

    Examples:

    >>> bool_to_str(3 < 4)
    'Yes'

    >>> bool_to_str(3 > 4)
    'No'

    >>> bool_to_str(True)
    'Yes'

    >>> bool_to_str(False)
    'No'
    """
    if bval:
        response = 'Yes'
    else:
        response = 'No'
    return response
