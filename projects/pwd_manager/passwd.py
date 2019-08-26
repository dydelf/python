#! /usr/bin/env python3
"""
This is a password manager for storing and restoring passwords.
NOT SECURE
"""

import sys
import pyperclip
import click


PASSWORDS = {
    'email': 'to jest skopiowane haslo',
    'blog': 'test',
    'luggage': '',
}

"""
Usage of click library is pointless,
we could use normal functions and the code would be clearer and simpler
the amount of text written into the command line would be smaller also
"""

@click.group()
def cli():
    pass

@cli.command()
@click.argument('account')
#@click.option('--get', '-g', help='Get the password of a given account name')
#@click.argument('--account')

def get(account):
    """Get the password of a given account name."""
    
    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        click.echo("Password for " + account + " copied.")
    else:
        click.echo('There is no such account')
        
         
@cli.command()
@click.argument('account')
@click.argument('password')
#@click.option('--update', help='Update the password for a given account')
#@click.option('--password', prompt='What is the new password? ', help='Input the new password')

def update(account, password):
    """Update the password of a given account."""
    if account in PASSWORDS:
        password = PASSWORDS[account]
        pyperclip.copy(PASSWORDS[account])
        click.echo("Password for " + account + " updated and copied.")
    else:
        click.echo('There is no such account')
     
 

cli.add_command(get)
cli.add_command(update)
        
if __name__ == '__main__':
    """
    try:
        account = sys.argv[2]
    except IndexError:
        account = sys.argv[1]
    """
    account = sys.argv[1]
    cli()