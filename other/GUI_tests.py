"""
Trying the GUI from PyQt5
"""

#from PyQt5.QtWidgets import QApplication, QLabel

#app = QApplication([])
#label = QLabel('Hello World')
#label.show()
#app.exec_()

from PyQt5.QtWidgets import *

app = QApplication([])
#app.setStyle('Fusion')
window = QWidget()
numbers = QLineEdit()
layout = QVBoxLayout()
layout.addWidget(numbers)
#layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec_()