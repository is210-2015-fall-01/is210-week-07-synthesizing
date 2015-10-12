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
    prompt = 'Please enter your password'
    response = 'Incorrect username or password. You have {} attempts left.'
    counter = 0
    while not authenticated and counter < maxattempts:
        password = getpass.getpass(prompt)
        authenticated = authentication.authenticate(username, password)
        counter += 1
        if not authenticated:
            print response.format(maxattempts - counter, maxattempts)
        return authenticated
