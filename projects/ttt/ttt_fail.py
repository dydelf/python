"""
Simple tic tac toe game.
Failed attempt to create everything from memory and by myself.
"""

import numpy as np
from colorama import init, Fore, Back, Style


class TicTacToe():
    
    def __init__(self):
        
        init(autoreset=True)
        
        self.back = Back.GREEN
        self.vis = Fore.BLACK
        self.invis = Fore.GREEN

        self.theBoard = {
            'up-L': '_', 'up-M': '_', 'up-R': '_',
            'mid-L': '_', 'mid-M': '_', 'mid-R': '_',
            'dwn-L': '_', 'dwn-M': '_', 'dwn-R': '_',
        }

    def printBoard(self):
        print(self.theBoard['up-L'], ' | ', self.theBoard['up-M'], ' | ', self.theBoard['up-R'])
        print("---+-----+----")
        print(self.theBoard['mid-L'], ' | ', self.theBoard['mid-M'], ' | ', self.theBoard['mid-R'])
        print("---+-----+----")
        print(self.theBoard['dwn-L'], ' | ', self.theBoard['dwn-M'], ' | ', self.theBoard['dwn-R'])
        
        
    def print_X(self):
        x = input()
        if x == '1':
            self.theBoard['up-L'] = 'X'
        elif x =='2':
            self.theBoard['up-M'] = 'X'
        elif x =='3':
            self.theBoard['up-R'] = 'X'
        elif x =='4':
            self.theBoard['mid-L'] = 'X'
        elif x =='5':
            self.theBoard['mid-M'] = 'X'
        elif x =='6':
            self.theBoard['mid-R'] = 'X'
        elif x =='7':
            self.theBoard['dwn-L'] = 'X'
        elif x =='8':
            self.theBoard['dwn-M'] = 'X'
        elif x =='9':
            self.theBoard['dwn-R'] = 'X'
        
        
    def print_O(self):
        x = input()
        if x == '1':
            self.theBoard['up-L'] = 'O'
        elif x =='2':
            self.theBoard['up-M'] = 'O'
        elif x =='3':
            self.theBoard['up-R'] = 'O'
        elif x =='4':
            self.theBoard['mid-L'] = 'O'
        elif x =='5':
            self.theBoard['mid-M'] = 'O'
        elif x =='6':
            self.theBoard['mid-R'] = 'O'
        elif x =='7':
            self.theBoard['dwn-L'] = 'O'
        elif x =='8':
            self.theBoard['dwn-M'] = 'O'
        elif x =='9':
            self.theBoard['dwn-R'] = 'O'
            
    def checkWin_X(self):
        if self.theBoard['up-L'] and self.theBoard['up-M'] and self.theBoard['up-R'] == 'X':
            print("You win X-player!")
        elif self.theBoard['mid-L'] and self.theBoard['mid-M'] and self.theBoard['mid-R'] == 'X':
            print("You win X-player!")
        elif self.theBoard['dwn-L'] and self.theBoard['dwn-M'] and self.theBoard['dwn-R'] == 'X':
            print("You win X-player!")
        elif self.theBoard['up-L'] and self.theBoard['mid-L'] and self.theBoard['dwn-L'] == 'X':
            print("You win X-player!")
        elif self.theBoard['up-M'] and self.theBoard['mid-M'] and self.theBoard['dwn-M'] == 'X':
            print("You win X-player!")
        elif self.theBoard['up-R'] and self.theBoard['mid-R'] and self.theBoard['dwn-R'] == 'X':
            print("You win X-player!")
        elif self.theBoard['up-L'] and self.theBoard['mid-M'] and self.theBoard['dwn-R'] == 'X':
            print("You win X-player!")
        elif self.theBoard['up-R'] and self.theBoard['mid-M'] and self.theBoard['dwn-L'] == 'X':
            print("You win X-player!")
            
    def checkWin_O(self):
        if self.theBoard['up-L'] and self.theBoard['up-M'] and self.theBoard['up-R'] == 'O':
            print("You win O-player!")
        elif self.theBoard['mid-L'] and self.theBoard['mid-M'] and self.theBoard['mid-R'] == 'O':
            print("You win O-player!")
        elif self.theBoard['dwn-L'] and self.theBoard['dwn-M'] and self.theBoard['dwn-R'] == 'O':
            print("You win O-player!")
        elif self.theBoard['up-L'] and self.theBoard['mid-L'] and self.theBoard['dwn-L'] == 'O':
            print("You win O-player!")
        elif self.theBoard['up-M'] and self.theBoard['mid-M'] and self.theBoard['dwn-M'] == 'O':
            print("You win O-player!")
        elif self.theBoard['up-R'] and self.theBoard['mid-R'] and self.theBoard['dwn-R'] == 'O':
            print("You win O-player!")
        elif self.theBoard['up-L'] and self.theBoard['mid-M'] and self.theBoard['dwn-R'] == 'O':
            print("You win O-player!")
        elif self.theBoard['up-R'] and self.theBoard['mid-M'] and self.theBoard['dwn-L'] == 'O':
            print("You win O-player!")
            
if __name__ == '__main__':
    tic = TicTacToe()
    for i in np.arange(0, 5):
        tic.printBoard()
        tic.print_X()
        tic.checkWin_X()
        tic.checkWin_O()
        tic.printBoard()
        tic.print_O()
        tic.checkWin_X()
        tic.checkWin_O()
        