class Calculator:

    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
    
    def plus(self):
        return self.number1 + self.number2



calculator = Calculator(10,5)
print(calculator.plus())


calculator.number1 = -2
calculator.number2 = 2
print(calculator.plus())









#     def plus(self,number1,number2):
#         self.number1 = number1
#         self.number2 = number2
#         return number1 + number2

# calculator = Calculator(10,5)
# print(calculator.plus())

# calculator.number1 = -2
# calculator.number2 = 2
# print(calculator.plus())
