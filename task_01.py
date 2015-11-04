# /usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


def get_matches(players):
    """ Explaining the get_matches function.
    Args:
        players (A list): A list of player names.
    Returns:
        A tuple with unique matchups of the players.
    Examples:
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
    """
    matchups = []
    for num in enumerate(players):
        for play in enumerate(players):
            if num < play:
                matchups.append((num[1], play[1]))
    return matchups
