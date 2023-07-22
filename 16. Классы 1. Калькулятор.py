# 16. Классы 1. Калькулятор
# Опишите класс Calculator, который будет реализовывать следующие методы и поля:
#
# sum(self, a, b) - сложение чисел a и b
# sub(self, a, b) - вычитание
# mul(self, a, b) - умножение
# div(self, a, b, mod=False) - деление. Если параметр mod == True, то метод должен возвращать остаток от деления вместо деления.
#                   По умолчанию mod=False.
# history(self, n) - этот метод должен возвращать строку с операцией по ее номеру относительно текущего момента (1 - последняя, 2 - предпоследняя).
#                   Формат вывода: sum(5, 15) == 20
# last - строка того же формата, что в предыдущем пункте, в которой содержится информация о последней операции по всем созданным объектам калькулятора.
#                   Т.е. это последняя операция последнего использованного объекта калькулятор. Если операций пока не было, то None.
# clear(cls) - метод, который очищает last, т.е. присваивает ему значение None.
# Формат вывода
# При сохранении строк в history и last нужно выводить только один знак после запятой дробного числа.
# При выполнении деления с mod сам параметр mod не нужно записывать в лог.

class Calculator:
    last = None

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