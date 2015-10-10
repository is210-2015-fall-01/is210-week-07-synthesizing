#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""w7 synthesizing task 02."""

import authentication
import getpass


def login(username, maxattempts=3):
    """This function creates a login.

    Args:
        Username(str): A string that represents the username
        of the username of the user attempting to log in.

gi        maxattempts(int, optional): An integer represent the maximum
        number of prompted attempts before the function returns false.

    Returns:
        Return True if the user has successfully authenticated.
        Return False if they exceed that max number of failed attempts.

    Examples:




    """

    userpw = False
    numattempts = 0
    incorrect = 'Incorrect username or password. You have {} attempts left.'

    while not userpw and numattempts < maxattempts:
        password = getpass.getpass('Please enter your password:')
        usrauth = authentication.authenticate(username, password)

        if usrauth is not False:
            userpw = True

        else:
            numattempts += 1
            print incorrect.format(maxattempts - numattempts)

    return userpw
