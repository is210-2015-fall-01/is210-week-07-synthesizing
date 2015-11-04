#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is week 7 synthesizing task_02."""


import authentication
import getpass


def login(username, maxattempts=3):
    """This function authenticate user to login.

    This function use getpass module and prompt users to provide their passwords
    which will then be used to authenticate successfull login.

    Args:
        username(str): The username of the user attempting to log in.
        maxattempts(int, optional): The maximum number of prompted attempts.

    Returns:
        If true return true otherwise return false.

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
        Please enter your password:
        True
    """

    authenticated = False
    attempt = 0
    warning = 'Incorrect username or password. You have {} attempts left.'

    while not authenticated and attempt < maxattempts:
        mypassd = getpass.getpass('Please enter your password:')

        if authentication.authenticate(username, mypassd) is True:
            authenticated = True

        else:
            attempt += 1
            print warning.format(maxattempts - attempt)
    return authenticated
