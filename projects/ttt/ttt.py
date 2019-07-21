"""
Simple terminal tic tac toe game for two players.
Repeats itself at the end.
"""

class TicTacToe():
    
    def __init__(self):
        
        self.win = False
        
        self.theBoard = {
            'q': '_', 'w': '_', 'e': '_',
            'a': '_', 's': '_', 'd': '_',
            'z': '_', 'x': '_', 'c': '_',
        }
        
        self.instructionBoard = {
            'q': 'q', 'w': 'w', 'e': 'e',
            'a': 'a', 's': 's', 'd': 'd',
            'z': 'z', 'x': 'x', 'c': 'c',
        }
        
    def printBoard(self, board):
        print(board['q'], ' | ', board['w'], ' | ', board['e'])
        print("---+-----+----")
        print(board['a'], ' | ', board['s'], ' | ', board['d'])
        print("---+-----+----")
        print(board['z'], ' | ', board['x'], ' | ', board['c'])
        
    def instructions(self):
        print("\nWelcome!")
        print("This is a Tic Tac Toe game :)")
        print("Please use the following keys to enter X or O")
        self.printBoard(self.instructionBoard)
        print("May the best win!\n")
    
    def print_XO(self):
        self.reset()
        turn = 'X'
        for i in range(9):
            self.printBoard(self.theBoard)
            self.checkWin(self.theBoard)
            if self.win == True:
                print("\nYou win!\n")
                break
            else:
                print('\nTurn for ' + turn + '. Move on which space?')
                move = input()
                print("\n")
                self.theBoard[move] = turn
                if turn == 'X':
                    turn = 'O'
                elif turn == 'O':
                    turn = 'X'
        #self.printBoard(self.theBoard)

        
    def checkWin(self, board):
        check = ['X', 'O']
        # checking horizontal
        if (board['q'] in check) and board['q'] == board['w'] == board['e']:
            self.win = True
        elif (board['a'] in check) and board['a'] == board['s'] == board['d']:
            self.win = True
        elif (board['z'] in check) and board['z'] == board['x'] == board['c']:
            self.win = True
        # checking vertical
        elif (board['q'] in check) and board['q'] == board['a'] == board['z']:
            self.win = True
        elif (board['w'] in check) and board['w'] == board['s'] == board['x']:
            self.win = True
        elif (board['e'] in check) and board['e'] == board['d'] == board['c']:
            self.win = True
        # checking diagonal
        elif (board['q'] in check) and board['q'] == board['s'] == board['c']:
            self.win = True
        elif (board['e'] in check) and board['e'] == board['s'] == board['z']:
            self.win = True
            
    def reset(self):
        self.win = False
        self.theBoard = {
            'q': '_', 'w': '_', 'e': '_',
            'a': '_', 's': '_', 'd': '_',
            'z': '_', 'x': '_', 'c': '_',
        }
        
        
if __name__ == '__main__':
    tic = TicTacToe()
    tic.instructions()
    flag = True
    while True:
        tic.print_XO()
        x = input('Game Over! \nWould you like to play again?  y|n\n')
        if x == 'n':
            break