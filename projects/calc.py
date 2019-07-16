"""
Simplest Calculator Possible
"""

import numpy as np


class Calculator():
    
    def __init__(self):
        self.numbers = []
        self.flag = True

    def instructions(self):
        print("\nWelcome to the Simplest Calculator Possible")
        print("Please provide numbers and operation that you want to perform")
        print("You can use as many numbers as you want")
        print("Type 0 to stop inputting new numbers")

    def inp(self):
        flag = True
        while flag:
            try:
                num = float(input("Input number: "))
                self.numbers.append(num)
                if 0 in self.numbers:
                    self.numbers.pop(-1)
                    flag = False
            except ValueError:
                print("\nPlease use only integers!")
                return
                
        for i in self.numbers:
            print(i, end=' | ')
    
    def operation(self):
        try:
            op = input("\nWhat operation would you like to perform?  + | - | * | / \n")
        except ValueError:
            print("Please provide an integer!")
            return
        
        if op == "+":
            print(sum(self.numbers))
        elif op == "-":
            self.res = [self.numbers[i] - self.numbers[i+1] for i in range(len(self.numbers) -1)]
            print(self.res)
        elif op == "*":
            result = np.prod(self.numbers)
            print(result)
        elif op == "/":
            result = "cholero nie dzieli sie przez zero"
            print(result)
            

if __name__ == '__main__':
    
    calc = Calculator()
    flag = True
    while flag:
        calc.instructions()
        calc.inp()
        calc.operation()
        again = input("\nWould you like to go again?   Y | N")
        if again == "N":
            flag = False