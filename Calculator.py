class Calculator:
    last = None
#11
    def __init__(self):
        self.result = []

    def sum(self, a, b):
        s = f'sum({a}, {b}) == {round(a + b,1)}'
        self.result.insert(0,s)
        Calculator.last = s
        return (a + b)

    def sub(self, a, b):
        s = f'sub({a}, {b}) == {round(a - b,1)}'
        self.result.insert(0,s)
        Calculator.last = s
        return (a - b)

    def mul(self, a, b):
        s = f'mul({a}, {b}) == {round(a * b,1)}'
        self.result.insert(0,s)
        Calculator.last = s
        return (a * b)

    def div(self, a, b, mod=False):
        if mod == True:
            s = f'div({a}, {b}) == {round(a % b,1)}'
            self.result.insert(0,s)
            Calculator.last = s
            return (a % b)
        else:
            s = f'div({a}, {b}) == {round(a / b,1)}'
            self.result.insert(0,s)
            Calculator.last = s
            return (a / b)

    def history(self, n):
        if len(self.result) != 0:
            return (self.result[n - 1])
        else:
            return None

    @classmethod
    def clear(cls):
        cls.last = None