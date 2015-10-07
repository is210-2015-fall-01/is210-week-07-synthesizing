#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Looped Authentication Process"""

import authentication
import getpass


def login(username, maxattempts=3):
    """This function authenticates a user in a login process.

    Args:
        username (str): A string representing the username of the user
        attempting to log in
        maxattempts (int, optional): An integer represent the maximum number
        of prompted attempts before the function returns False. Defaults to 3

    Returns:
        ok: True if the user has been authenticated; False otherwise

    Examples:
        Correct password entered on first attempt:
            >>> task_02.login('veruca', 2)
            Please enter your password:
            True
        Incorrect password entered maxattempts number of times:
            >>> task_02.login('veruca', 2)
            Please enter your password:
            True
    """
    aok = False
    i = 1
    getpw1 = 'Please enter your password: '
    getpw2 = 'Incorrect username or password. You have {} attempts left.'

    while (not aok) and (i <= maxattempts):
        if i == 1:
            aok = authentication.authenticate(username, getpass.getpass(getpw1))
        elif i > 1:
            print getpw2.format(maxattempts-i+1)
            aok = authentication.authenticate(username, getpass.getpass(getpw1))
        if aok:
            break
        i += 1
    return aok
