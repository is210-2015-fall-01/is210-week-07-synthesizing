#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is task_01 docstring."""


def get_matches(players):
    """"This is a game matching function.

    This function gets a list of players and creates a half-Cartesian list
    of players playing against each other.

    Args:
        players (list): A list of player names.

    Returns:
        Half-Cartesian list of player matches. A list containing tuples of
        matched pairs.

    Example:
        >>> get_matches(['Larry', 'Curly', 'Moe'])
        [('Larry', 'Curly'), ('Larry', 'Moe'), ('Curly', 'Moe')]

    """
    match = []
    for row in enumerate(players):
        for col in enumerate(players):
            if row < col:
                match.append((row[1], col[1]))
    return match
