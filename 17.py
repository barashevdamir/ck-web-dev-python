class BaseWallet(object):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def __str__(self):
        return ' '.join([type(self) ,self.name, str(self.amount)])
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
    #def __radd__(self, other):
    #    BaseWallet.__radd__ = BaseWallet.__add__
    __radd__ = __add__
    #def __iadd__(self, other):
    __iadd__ = __add__
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
    __rsub__ = __sub__
    __isub__ = __sub__
    def __mul__(self, other):
        """Функция, которая описывает умножение нашего объекта на объект other"""
        new_name = self.name
        new_amount = self.amount * float(other)
        return BaseWallet(new_name, new_amount)
    __rmul__ = __mul__
    __imul__ = __mul__
    def __div__(self, other):
        """Функция, которая описывает деление нашего объекта на объект other"""
        new_name = self.name
        new_amount = self.amount / float(other)
        return BaseWallet(new_name, new_amount)
    __idiv__ = __div__
    def __eq__(self, other):
        if (self.amount == other.amount) and (isinstance(BaseWallet, other)):
            return(True)
        else:
            return(False)
    def spend_all(self):
        new_name = self.name
        if (self.amount > 0 ):
            new_amount = 0
            return BaseWallet(new_name, new_amount)
    def to_base(self):
        return(self.amount * self.exchange_rate)
class RubbleWallet(BaseWallet):
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
