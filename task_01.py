#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is week7 synthesizing task 01."""


def get_matches(players):
    """This function will create a matching player list.

    This function going to use a nested for loop and loop over the same object
    twice to produce matching list od players.

    Arg:
       players(str): list of names.

    Returns:
        returns names as tuple.

    Examples:
        >>> import task_01
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]

    """

    player = []
    lists = list(enumerate(players))
    for index1 in lists:
        for index2 in lists:
            if index1[0] < index2[0]:
                player.append((index1[1], index2[1]))
    return player
