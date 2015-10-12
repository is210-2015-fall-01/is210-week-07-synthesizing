#!user/bin/env python
# -*- coding: utf-8 -*-
"""Login simulator"""

import authentication
import getpass


def login(username, maxattempts=3):
    """Input username and password practice.
    Arguments:
        username (str): username from list of approved users
        maxattampts (int): defaults to 3 unless otherwise input
    Returns:
        prompt to enter password, under variable stringput. If
        entered incorrectly returns failattempt variable and
        displays number of remaining tries.
    Examples:
        login('augustus')
        >>>Please enter your password:
        If correct:
            True
        If incorrect:
            Incorrect username or password.You have 2 attempts left.
    """
    authenticated = False
    failattempt = 'Incorrect username or password.You have {} attempts left.'
    
    attempt_num = 0
    while not authenticated and attempt_num < maxattempts:
        strinput = getpass.getpass('Please enter your password:')
        authenticated = authentication.authenticate('username', 'password')
        if authenticated is True:
            print True
        else:
            attempt_num += 1
            print failattempt.format(maxattempts - attempt_num)
        
            

    return authenticated


    
