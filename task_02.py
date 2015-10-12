#!user/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci series"""

import authentication
import getpass


def login(username, maxattempts=3):
    authenticated = False
    failattempt = 'Incorrect username or password.You have {} attempts left.'
    
    attempt_num = 0
    while not authenticated and attempt_num < maxattempts:
        strinput = getpass.getpass('Please enter your password:')
        authenticated = authentication.authenticate(username, password)
        if authenticated:
            print True
        else:
            attempt_num += 1
            print failattempt.format(attempt_num[0])
        
            

    return authenticated


    
