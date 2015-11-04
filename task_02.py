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
    message = 'Incorrect username or password. You have {} attempts left'
    while counter < maxattempts and not authenticated:
        password = getpass.getpass('Please enter your password?')
        usrauth = authentication.authenticate(username, password)
        if usrauth is not False:
            authenticated = True
        else:
            counter += 1
            print message.format(maxattempts - counter)
    return authenticated
