#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


import authentication
import getpass


def login(username, maxattempts=3):
    """A login page.

    Agrs:
         The username of the user attempting to log in.
         The maximum number of prompted attempts.

    Returns:
        Return True if the user has successfully authenticated
        False if they exceed that maximum number of failed attempts.


    """

    authenticated = False
    counter = 0
    warning = 'Incorrect username or password. You have {} attempts left.'

    while not authenticated and counter < maxattempts:
        password = getpass.getpass('Please enter your password:')

        if authentication.authenticate(username, password) is True:
            authenticated = True

        else:
            counter += 1
            print warning.format(maxattempts - password)
    return authenticated
