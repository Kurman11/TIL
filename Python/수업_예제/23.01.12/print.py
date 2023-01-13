
class Calculator:

    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2

    def print(self):
        return print(f'합 : {self.number1 + self.number2}')
        


calculator = Calculator(10,5)
print(calculator.print())


calculator.number1 = -2
calculator.number2 = 2
print(calculator.print())
