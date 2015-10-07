#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Demonstrates an Half-Cartesian application."""


def get_matches(players):
    """Creates a list of unique matches between players
        FOR ITEM 0 IN LIST A, TUPLE WITH ITEMS 1 THRU P-1 IN LIST B
        FOR ITEM 1 IN LIST A, TUPLE WITH ITEMS 2 THRU P-1 IN LIST B
        FOR ITEM 2 IN LIST A, TUPLE WITH ITEMS 3 THRU P-1 IN LIST B
            .
            .
            .
        FOR ITEM P-3 IN LIST A, TUPLE WITH ITEMS THRU P-2 IN LIST B
        FOR ITEM P-2 IN LIST A, TUPLE WITH ITEM P-1 IN LIST B

    Args:
        players: a list of player names

    Returns:
        A tuple containing a list of unique matchups between players

    Raises:

    Examples:

    """
    matches = []
    # l o o p  s t a r t
    for i, plyr1 in enumerate(players):
        if i < (len(players)-1):
            for j, plyr2 in enumerate(players):
                if i < j:
                    matches.append((plyr1, plyr2))
    matches = list(set(matches))
    print matches
    return matches
