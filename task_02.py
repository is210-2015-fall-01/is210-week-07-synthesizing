#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Password task2"""


import authentication
import getpass


def login(username, maxattempts=3):
    """Login to see top secret files

    Args:
        username (str): Enter username
        maxattempts (int): Number of attempts, default 3.

    Returns:
        (bool):True if password is right, False if password is wrong.

    Examples:
        >>> task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False
    """

    auth = False
    nope = 'Incorrect username or password. You have {} attempts left.'

    while auth is False and maxattempts > 0:
        password = getpass.getpass('Please enter your password:')
        auth = authentication.authenticate(username, password)

        if auth is not False:
            auth = True

        else:
            maxattempts -= 1
            print nope.format(maxattempts)

    return auth
