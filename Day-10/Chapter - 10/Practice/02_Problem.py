# Write a class "calculato" capable of finding square, cube and square root of a number.
import math

class Calculator:
    def __init__(self,number):
        self.number = number

    def square(self):
        print(f"The Square of {self.number} is {self.number * self.number}")
    def cube(self):
        print(f"The Cube of {self.number} is {self.number ** 3}")
    def square_root(self):
        print(f"The Square Root of {self.number} is {math.sqrt(self.number)}")

calculate = Calculator(25)   

calculate.square()
calculate.square_root()
calculate.cube()
