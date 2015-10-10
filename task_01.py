#!user/bin/env python
# -*- coding: utf-8 -*-
"""Half cartesian"""


def get_matches(players):
    """Matches each player in list with other players in lineup.
    Arguments:
        players(list): list of players' names
    Returns:
        list of players matched which each other as tuples
    Examples:
        LINEUP = ['Nick', 'James', 'Jessee', 'Alan']
        get_matches(LINEUP)
        >>>[('Nick', 'James'), ('Nick', 'Jessee'), ('Nick', 'Alan'),
        ('James', 'Jessee'), ('James', 'Alan'), ('Jessee', 'Alan')]
        """
    results = []
    for index, player in enumerate(players):

        for index2, player2 in enumerate(players):
            if index < index2:
                results.append((player, player2))

    return results


LINEUP = ['Nick', 'James', 'Jessee', 'Alan']
