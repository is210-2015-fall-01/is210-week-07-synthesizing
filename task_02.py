#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is task_02 docstring."""


import getpass
import authentication


def login(username, maxattempts=3):
    """This function simulates user login authentication.

    This function makes use of the getpass and authenticate modules to
    simulate user login authentication.

    Args:
        username (str): A username as defined in the assignment.
        maxattempts (int): Maximum number of allowed login attempts.

    Returns:
        True or False

    Example:
        >>> login('mike', 5)
        Enter Password:
        Incorrect username or password. You have 4 attempts left.
        Enter Password:
        Incorrect username or password. You have 3 attempts left.
        Enter Password:
        Incorrect username or password. You have 2 attempts left.
        Enter Password:
        True
    """
    authenticated = False
    warning = 'Incorrect username or password. You have {} attempts left.'
    while not authenticated and (maxattempts > 0):
        mypass = getpass.getpass('Enter Password: ')
        if authentication.authenticate(username, mypass) is True:
            authenticated = True
        else:
            maxattempts -= 1
            if maxattempts != 0:
                print warning.format(maxattempts)
    return authenticated
