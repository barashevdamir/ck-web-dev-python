# 17. Классы 2. Кошельки
# Написать классы, которые будут использованы как счета в банке.
# Каждый счет - в своей валюте.
# Соответственно, у каждого объекта счета должны быть атрибуты с суммой денег, хранящихся на нём, и название кошелька.
# Каждый класс счета должен в себе хранить коэффициент отношения стоимости своей валюты к базовой валюте.
#
# Нам понадобится один базовый класс BaseWallet, в котором будут реализованы общие для всех валютных счетов методы,
# и три класса для конкретных валютных счетов: RubbleWallet, DollarWallet, EuroWallet. Будем считать коэффициентами отношения валют к базовой валюте:
#
# Рубль: 1
# Доллар: 60
# Евро: 70
#
# Протокол взаимодействия объектов следующий:
#
# RubbleWallet("Первый кошелек", 10), где "Первый кошелек" - это название кошелька, а 10 - сумма денег на нём.
# аналогичные конструкторы для других счетов
# RubbleWallet("X", 10) + 20 == RubbleWallet("X", 30) - при сложении с числом считаем, что это та же валюта.
# RubbleWallet("X", 10) += 20 - должен поддерживаться и такой синтаксис
# 20 + RubbleWallet("X", 10) == RubbleWallet("X", 30) - radd для чисел
# RubbleWallet("X", 20) + DollarWallet("D", 10) == RubbleWallet("X", 620) - конвертация валюты при сложении счетов.
# DollarWallet("D", 2) + RubbleWallet("X", 60) == DollarWallet("D", 3) - результат - в валюте первого слагаемого.
# DollarWallet("D", 2) += RubbleWallet("X", 60) - здесь тоже должен поддерживаться этот синтаксис.
# предыдущие 6 пунктов реализовать и для вычитания
# RubbleWallet("X", 10) * 20 == RubbleWallet("X", 200) - умножение на число
# RubbleWallet("X", 10) *= 20 - тоже с таким синтаксисом
# те же 2 пункта для деления
# 20 * RubbleWallet("X", 10) == RubbleWallet("X", 200) - умножение числа на кошелек
# DollarWallet("A", 15) == DollarWallet("B", 15): два объекта равны, если у них совпадает тип кошелька и сумма на счете.
# RubbleWallet("X", 100).spend_all() - для любого типа кошелька релизовать функцию, которая обнуляет баланс, если он положительный
# DollarWallet("X", 1).to_base() == 60 - эта функция должна возвращать число денег в кошельке в базовой валюте
# print(DollarWallet("Q", 150)) - должна выводить строку: 'Dollar Wallet Q 150' (и аналогично Rubble и Euro для остальных кошельков)
# У каждого объекта должны быть доступны атрибуты:
#
# name - название кошелька
# amount - количество денег на счете
# exchange_rate - коэффициент стоимости валюты к базовой

class BaseWallet:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def __repr__(self):
        """Функция, которая используется для текстового представления объекта в случаях, когда это происходит не
        через функцию str(obj)"""
        return str(self)
    def _copy(self):
        return BaseWallet(self.name, self.amount)
    def __add__(self, other):
        """Функция, которая описывает прибавление к нашему объекту объекта other"""
        new = self._copy()
        # если у нас оба объекта данного класса, сложим их атрибуты
        if isinstance(other, BaseWallet):
            new.name = self.name
            new.amount = self.amount + other.amount * (other.exchange_rate / self.exchange_rate)
        else:
            # а если второй объект не этого класса, то попробуем его привести к типу float
            new.name = self.name
            new.amount = self.amount + float(other)
        return new
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        if isinstance(other, BaseWallet):
            self.amount += other.to_base() / self.exchange_rate
        else:
            self.amount += float(other)
        return self
    def __sub__(self, other):
        """Функция, которая описывает вычитание из нашего объекта объекта other"""
        new = self._copy()
        # если у нас оба объекта данного класса, сложим их атрибуты
        if isinstance(other, BaseWallet):
            new.name = self.name
            new.amount = self.amount - other.amount * (other.exchange_rate / self.exchange_rate)
        else:
            # а если второй объект не этого класса, то попробуем его привести к типу float
            new.name = self.name
            new.amount = self.amount - float(other)
        return new
    def __rsub__(self, other):
        tmp = self._copy()
        tmp.amount = other - self.amount
        return tmp
    def __isub__(self, other):
        if isinstance(other, BaseWallet):
            self.amount -= other.to_base() / self.exchange_rate
        else:
            self.amount -= float(other)
        return self
    def __mul__(self, other):
        new = self._copy()
        """Функция, которая описывает умножение нашего объекта на объект other"""
        new.name = self.name
        new.amount = self.amount * float(other)
        return new
    def __rmul__(self, other):
        return self.__mul__(other)
    def __imul__(self, other):
        self.amount *= float(other)
        return self
    def __truediv__(self, other):
        """Функция, которая описывает деление нашего объекта на объект other"""
        new = self._copy()
        new.amount = self.amount / float(other)
        return new
    def __itruediv__(self, other):
        self.amount /= other
        return self
    def __eq__(self, other):
        if (self.amount == other.amount) and (type(self) == type(other)):
            return(True)
        else:
            return(False)
    def spend_all(self):
        if (self.amount > 0 ):
            self.amount = 0
            return self
    def to_base(self):
        return(self.amount * self.exchange_rate)

class RubbleWallet(BaseWallet):
    exchange_rate = 1
    def __init__(self, name: str = "RubbleWallet", amount: float = 0):
        super(RubbleWallet, self).__init__(name, amount)
    def _copy(self):
        return RubbleWallet(self.name, self.amount)
    def __str__(self):
        return f"Rubble Wallet {self.name} {self.amount}"
class DollarWallet(BaseWallet):
    exchange_rate = 60
    def __init__(self, name: str = "DollarWallet", amount: float = 0):
        super(DollarWallet, self).__init__(name, amount)
    def _copy(self):
        return DollarWallet(self.name, self.amount)
    def __str__(self):
        return f"Dollar Wallet {self.name} {self.amount}"
class EuroWallet(BaseWallet):
    exchange_rate = 70
    def __init__(self, name: str = "EuroWallet", amount: float = 0):
        super(EuroWallet, self).__init__(name, amount)
    def _copy(self):
        return EuroWallet(self.name, self.amount)
    def __str__(self):
        return f"Euro Wallet {self.name} {self.amount}"