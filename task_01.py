#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""w7 synthesizing task 01."""


def get_matches(players):
    """Function that takes one argument that
       list player names.

    Arg:
        Players(list): a list of players

    Returns:
        A newly created list of tuples.

    Examples:
        >>> import task_01
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]

    """

    matchups = []
    playlist = list(enumerate(players))
    for first in playlist:
        for second in playlist:
            if first[0] < second[0]:
                matchups.append((first[1], second[1]))
    return sorted(matchups)
