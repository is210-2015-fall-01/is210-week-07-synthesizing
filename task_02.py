#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""

import authentication
import getpass


def login(username, maxattempts=3):
    """the structure of a login

    Args:
         A string representing the username of the user attempting to log in.
         An integer represent the maximum number of prompted attempts.

    Returns:
        Return True if the user has successfully authenticated
        False if they exceed that maximum number of failed attempts.
    """

    authenticated = False
    numattempts = 0
    incorrect = 'Incorrect username or password. You have {} attempts left.'

    while not authenticated and numattempts < maxattempts:
        password = getpass.getpass('Please enter your password:')
        user = authentication.authenticate(username, password)

        if user is not False:
            authenticated = True

        else:
            numattempts += 1
            print incorrect.format(maxattempts - numattempts)

        return authenticated
