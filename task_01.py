#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Uses Half Cartesian for multiplie matchup scenarios."""


def get_matches(players):
    """This function processes the list of names to make unique matchups.

    Args:
    players (list): a list of player names

    Returns:
    list of unique matchups between players (stored as list of tuples)

    Examples:
        >>> get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
        >>> get_matches(['James', 'Jesse', 'Jennifer'])
        [('James', 'Jesse'), ('James', 'Jennifer'), ('Jesse', 'Jennifer')]

    """
    matches = []
    enum = list(enumerate(players))
    for play1 in enum:
        for play2 in enum:
            if play1[0] < play2[0]:
                matches.append((play1[1], play2[1]))
    return matches
