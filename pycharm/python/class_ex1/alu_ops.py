class Aluops:
    num1 = 0
    num2 = 0
    ans = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self, ops):
        if ops == "add":
            self.ans = self.num1 + self.num2
        if ops == "sub":
            self.ans = self.num1 - self.num2
        if ops == "mul":
            self.ans = self.num1 * self.num2
        if ops == "div":
            self.ans = self.num1 / self.num2

        print("{} of two numbers = " .format(ops) + str(self.ans))


obj = Aluops(10, 20)
obj.calculate("add")

obj = Aluops(1000, 20000)
obj.calculate("sub")

obj = Aluops(50, 20)
obj.calculate("mul")

obj = Aluops(50, 20)
obj.calculate("div")
