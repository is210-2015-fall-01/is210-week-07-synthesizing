#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Login/authentication screen."""


import authentication
import getpass


def login(username, maxattempts=3):
    """This function will authenticate user(allows few attempts).

    Args:
        username (str): string that is username of user who is logging in
        maxattempts (int,optional): int rep maximum number of attempts

    Returns:
        boolean: T if successfully authen. F if exceed max number.

    Examples:
        >>> import task_02
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

        >>> import task_02
        >>> task_02.login('veruca', 2)
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:greed
        True
    """
    Incorrect = 'Incorrect username or password. You have {} attempts left.'
    AUTHEN = False
    NUMA = 0
    while not AUTHEN and NUMA < maxattempts:
        askpass = getpass.getpass('Please enter your password:')
        user = authentication.authenticate(username, askpass)
        if user is not False:
            AUTHEN = True
        else:
            NUMA += 1
            print Incorrect.format(maxattempts - NUMA)
    return AUTHEN
