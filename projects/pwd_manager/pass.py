#! /usr/bin/env python3
"""
Not secure version of simple password manager
"""

import sys
import pyperclip

PASSWORDS = {
    'email': 'to jest skopiowane haslo',
    'blog': 'test',
    'luggage': '',
}

if len(sys.argv) < 2:
    print('Usage: ./pass.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)