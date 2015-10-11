#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates a program for login and authentication"""


import authentication
import getpass


def login(username, max_attempts=3):
    """This function loops through user input to authenticate password

    Args:
        It takes 2 arguments, username and max_attempts, with 3 as default max.

    Returns:
        A boolean
    """

    authenticated = False
    attempt = 0
    while (attempt < max_attempts) or (authenticated == False):
        myval = getpass.getpass(prompt='Enter password:  ')
        attempt += 1
        authenticated = authentication.authenticate(username, myval)

    return authenticated
