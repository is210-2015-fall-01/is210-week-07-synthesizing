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
    >>> get_matches(['James', 'Jesse', 'Jennifer'])
    [('James', 'Jennifer'), ('James', 'Jesse')]

    """
    matches = []
    ENUM = enumerate(players)
    for a, PLAY1 in ENUM:
        if a < (len(players)-1):
            for b, PLAY2 in ENUM:
                if a < b:
                    matches.append((PLAY1, PLAY2))
                    matches = list(sorted(set(matches)))
    return matches
