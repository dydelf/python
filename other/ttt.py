"""
Tic tac toe with curses
"""

import time
import curses

def draw_board():
    v = '|    |    |    |'
    h = ' ____ ____ ____ '
    for i in range(0, 10):
        if i%3 == 0:
            window.addstr(2, 2, h)
        else:
            window.addstr(2, 2, v)
        window.refresh()
        time.sleep(2)

curses.wrapper(draw_board)
