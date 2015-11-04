#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""There can only be one."""


def get_matches(players):
    """Creating a list of versus matchups for players.
    Args:
        list = List of players who will fight to the end.
    Returns:
        tuple = A tuple of created matches.
    Examples:
    >>> get_matches(['Harry', 'Howard', 'Hugh'])
    [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
    """

    dual = []
    dual_list = list(enumerate(players))
    for first in dual_list:
        for second in dual_list:
            if first[0] < second[0]:
                dual.append((first[1], second[1]))
    return sorted(dual)
