# 19. Доступ к атрибутам
# Доработать класс Field так, чтобы вдобавок к реализованному функционалу появились следующие возможности:
#
# field = Field()
#
# Запись значения в ячейку:
# field.a1 = 25: эквивалентно field['a1'] = 25
# field.A1 = 25: то же самое
# Получение значения:
#   field['b', 2] = 100
#   field.b2
#   field.B2
# Удаление значения:
# del field.a1, del field.A1 - эквивалентно del field['a', 1]
#
# Таким образом, внутри класса Field методы работы с атрибутами должны работать с тем же объектом,
# в котором хранятся значения, обрабатываемые в методах __setitem__, __getitem__, __delitem__.
#
# Кроме того, обычное присвоение и получение атрибутов (тех, которые не являются адресом ячейки данных нашего класса)
# должно производиться по стандартному алгоритму питоновских объектов, т.е. они должны храниться в словаре __dict__ объекта.
#
# field = Field()
# field.abcde = 125
# print(field.abcde, field.__dict__['abcde'] == 125)
# 125 True
#
# Для таких атрибутов также должны быть реализованы получение, присваивание и удаление значения.

import re
def convert_tuple(c_tuple):
  my_str=''
  for i in c_tuple:
    my_str=my_str+str(i)
  return my_str
class Field(dict):
    def __init__(self):
        super(Field, self).__init__()
    def __repr__(self):
        """Функция, которая используется для текстового представления объекта в случаях, когда это происходит не
        через функцию str(obj) """
        return str(self)
    def key_normalize(self, key):
        comp_pat1 = re.compile(r'[a-zA-Z]\d+$')
        comp_pat2 = re.compile(r'\d+[a-zA-Z]$')
        if type(key) == tuple and len(key) == 2:
            key = list(key)
            for i in range(len(key)):
                if type(key[i]) == int:
                    key[i] = str(key[i])
                elif type(key[i]) == str:
                    pass
                else:
                    raise ValueError
            key = ''.join(key)
        if type(key) == str:
            key = key.lower()
        else:
            raise TypeError
        if comp_pat1.match(key):
            return key
        if comp_pat2.match(key):
            return key[::-1]
        else:
            raise ValueError
    def __getitem__(self, key):
        return super(Field, self).__getitem__(self.key_normalize(key))
    def __setitem__(self, key, value):
        super(Field, self).__setitem__(self.key_normalize(key), value)
    def __delitem__(self, key):
        super(Field, self).__delitem__(self.key_normalize(key))
    def __missing__(self, key):
        return None
    def __contains__(self, item):
        return self[item] != self.__missing__(1)
    def __iter__(self):
        for k, v in self.items():
            yield v
    def __getattr__(self, attr):
        comp_pat1 = re.compile(r'[a-zA-Z]\d+$')
        comp_pat2 = re.compile(r'\d+[a-zA-Z]$')
        if comp_pat1.match(attr) or comp_pat2.match(attr):
            return self.__getitem__(attr)
        else:
            self.__dict__.get(attr)
    def __setattr__(self, attr, value):
         comp_pat1 = re.compile(r'[a-zA-Z]\d+$')
         comp_pat2 = re.compile(r'\d+[a-zA-Z]$')
         if comp_pat1.match(attr) or comp_pat2.match(attr):
             self.__setitem__(self.key_normalize(attr), value)
         else:
            self.__dict__[attr] = value
    def __delattr__(self, attr):
        comp_pat1 = re.compile(r'[a-zA-Z]\d+$')
        comp_pat2 = re.compile(r'\d+[a-zA-Z]$')
        if comp_pat1.match(attr) or comp_pat2.match(attr):
            self.__delitem__(self.key_normalize(attr))
        else:
            super(Field, self).__delattr__(attr)
