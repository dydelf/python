"""
Calculator app
Functionalities cover simple math functions
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit, QGridLayout, 
                             QMainWindow, QPushButton, QLCDNumber)
import sys


class Window(QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(0, 0, 0, 0)
        self.setWindowTitle("Calculator")
        
        self.initUI()
        
    def initUI(self):
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        self.display = QLCDNumber(self)
        layout.addWidget(self.display, 0, 0, 1, 4)
        
        #numbers = QLineEdit()
        #layout.addWidget(numbers, 0, 0, 1, 4)
        self.number_1 = QPushButton('1')
        layout.addWidget(self.number_1, 1, 0)
        self.num_1 = str(1)
        self.v = 1
        
        #for n in range(1, 1):
        #    getattr(self, 'number_n%s' % n).pressed.connect(lambda v=n: self.input_number(v))
        
        self.number_1.pressed.connect(self.input_number)
        
        layout.addWidget(QPushButton('2'), 1, 1)
        layout.addWidget(QPushButton('3'), 1, 2)
        layout.addWidget(QPushButton('4'), 2, 0)
        layout.addWidget(QPushButton('5'), 2, 1)
        layout.addWidget(QPushButton('6'), 2, 2)
        layout.addWidget(QPushButton('7'), 3, 0)
        layout.addWidget(QPushButton('8'), 3, 1)
        layout.addWidget(QPushButton('9'), 3, 2)
        layout.addWidget(QPushButton('0'), 3, 3)
        layout.addWidget(QPushButton('='), 3, 4)
        layout.addWidget(QPushButton('+'), 1, 3)
        layout.addWidget(QPushButton('-'), 1, 4)
        layout.addWidget(QPushButton('*'), 2, 3)
        layout.addWidget(QPushButton('/'), 2, 4)
        layout.addWidget(QPushButton('CE'), 0, 4)
        
        self.show()
                
    def update(self):
        self.label.adjustSize()
        
    def input_number(self, v):
        self.v = 2
        self.dis()
        
    def dis(self):
        self.display.display(self.v)
        
        
def window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
    
window()