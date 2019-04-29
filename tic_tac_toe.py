"""
Very basic `tic tac toe game.
"""

def draw_board():
    v = '|    |    |    |'
    h = ' ____ ____ ____ '
    for i in range(0,10):
        if i%3==0:
            print(h)
        else:
            print(v)
draw_board()
