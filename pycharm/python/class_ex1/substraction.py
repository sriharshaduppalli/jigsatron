class Substraction:
    num1 = 0
    num2 = 0
    ans = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        self.ans = self.num1 - self.num2
        print("addition of two numbers = " + str(self.ans))


obj = Substraction(10, 20)
obj.calculate()

obj = Substraction(1000, 20000)
obj.calculate()
