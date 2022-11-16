class BaseWallet:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return ': '.join([self.name, str(self.amount)])

    def __repr__(self):
        """Функция, которая используется для текстового представления объекта в случаях, когда это происходит не
        через функцию str(obj)"""
        return str(self)

    def __add__(self, other):
        """Функция, которая описывает прибавление к нашему объекту объекта other"""
        # если у нас оба объекта данного класса, сложим их атрибуты
        if isinstance(other, BaseWallet):
            new_name = self.name
            new_amount = self.amount + other.amount * (other.exchange_rate / self.exchange_rate)
        else:
            # а если второй объект не этого класса, то попробуем его привести к типу float
            new_name = self.name
            new_amount = self.amount + float(other)
        return BaseWallet(new_name, new_amount)

    BaseWallet.__radd__ = BaseWallet.__add__
    BaseWallet.__iadd__ = BaseWallet.__add__

    def __sub__(self, other):
        """Функция, которая описывает вычитание из нашего объекта объекта other"""
        # если у нас оба объекта данного класса, сложим их атрибуты
        if isinstance(other, BaseWallet):
            new_name = self.name
            new_amount = self.amount - other.amount * (other.exchange_rate / self.exchange_rate)
        else:
            # а если второй объект не этого класса, то попробуем его привести к типу float
            new_name = self.name
            new_amount = self.amount - float(other)
        return BaseWallet(new_name, new_amount)

    BaseWallet.__rsub__ = BaseWallet.__sub__
    BaseWallet.__isub__ = BaseWallet.__sub__

    def __mul__(self, other):
        """Функция, которая описывает умножение нашего объекта на объект other"""
        new_name = self.name
        new_amount = self.amount * float(other)
        return BaseWallet(new_name, new_amount)

    BaseWallet.__rmul__ = BaseWallet.__mul__
    BaseWallet.__imul__ = BaseWallet.__mul__

    def __div__(self, other):
        """Функция, которая описывает деление нашего объекта на объект other"""
        new_name = self.name
        new_amount = self.amount / float(other)
        return BaseWallet(new_name, new_amount)

    BaseWallet.__idiv__ = BaseWallet.__div__

    def __eq__(self, other):
        if (self.amount == other.amount) & & (isinstance(BaseWallet, other)):


    def spend_all(self):
        if


class RubleWallet(BaseWallet):
    exchange_rate = 1
    def __init__(self):
        super().__init__()


class DollarWallet(BaseWallet):
    exchange_rate = 60
    def __init__(self):
        super().__init__()


class EuroWallet(BaseWallet):
    exchange_rate = 70
    def __init__(self):
        super().__init__()
