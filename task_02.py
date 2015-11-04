# /usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""

import authentication
import getpass


def login(username, maxattempts=3):
    """ Explaining the login function.
    Args:
        username (str):A string representing the user.
        maxattempts (int, optional): An integer represent the maximum
        number of prompted attempts before the function returns False. Defaults
        to 3
    Returns:
       Return True if the user has successfully authenticated before
       hitting the maximum number of attempts or False if they exceed
       that maximum number of failed attempts.
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
        """
    authenticated = False
    attempt = 0
    alert = 'Incorrect username or password. You have {} attempts left'
    while attempt < maxattempts and not authenticated:
        password = getpass.getpass('Please enter your password?')
        authorize = authentication.authenticate(username, password)
        if authorize is not False:
            authenticated = True
        else:
            attempt += 1
            print alert.format(maxattempts - attempt)
    return authenticated
