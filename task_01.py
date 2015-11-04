#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


def get_matches(players):
    """A list of versus matchups for players in a street fighter tournament

    Args:
        players (list): A list of player names.

    Returns:
        Return the newly created list of tuples.
    """

    player = []
    player_list = list(enumerate(players))
    for first in player_list:
        for second in player_list:
            if first[0] < second[0]:
                player.append((first[1], second[1]))
    return sorted(player)
