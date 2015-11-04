#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates a function for players' versus matchups"""


LISTED_PLAYERS = ['James', 'Jesse', 'Jennifer']


def get_matches(players):
    """This function will use enumerate to loop through a list of strings.

    Args:
        It takes one argument, players.

    Returns:
        A list of tuples

    Examples:
        >>>[('Jesse', 'James'), ('Jennifer', 'James'), ('Jennifer', 'Jesse')]
    """
    new_list = []
    for (offset_outer, list_outer) in enumerate(players):
        for (offset_inner, list_inner) in enumerate(players):
            if offset_outer > offset_inner:
                new_list.append((list_outer, list_inner))
    return new_list

get_matches(LISTED_PLAYERS)
