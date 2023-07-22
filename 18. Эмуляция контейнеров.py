# 18. Эмуляция контейнеров
# Напишем свой аналог листа таблицы Excel.
# Нужно написать структуру данных Field, в которой доступ к значениям будет осуществляться по ключам.
# Ключом будет пара "буква" - "число", по аналогии с адресом ячейки в Excel. Возможные форматы обращения к одной и той же "ячейке" данных:
#
# field = Field()
#
# field[1, 'a'] = 25
# field['a', 1] = 25
# field['a', '1'] = 25
# field['1', 'a'] = 25
# field['1a'] = 25
# field['a1'] = 25
# field[1, 'A'] = 25
# field['A', 1] = 25
# field['A', '1'] = 25
# field['1', 'A'] = 25
# field['1A'] = 25
# field['A1'] = 25
# В этом списке каждая из этих строк записывает число 25 в ячейку с одним и тем же ключом.
# Соответственно, по любому из перечисленных ключей должно быть можно получить это число из объекта field.
# Также должны быть реализованы удаление элемента из структуры (через оператор del) и возможность использования оператора in, например:
#
# (1, 'a') in field: True
# "A1" in field: True
# ('D', '4') in field: False
# Таким образом, выходит, что ключом структуры может быть либо кортеж, либо строка.
# При попытке получить или записать значение по ключу другого типа должно быть вызвано исключение TypeError.
# При некорректном значении строки или элементов кортежа нужно вызывать исключение ValueError.
# Корректными значениями будет считать одиночные буквы и неотрицательное целое число любой длины, т.е. правильные варианты ключей:
#
# А1
# А222543
# Z89
# Неправильные варианты ключей:
#
# AA5
# Q2.5
# -6F
# A
# 27
# GG
# Кроме вышеперчисленного, по объекту должно быть возможно итерироваться.
# При проходе циклом по объекту должны возвращаться значения, хранящиеся в нём. Порядок возврата значений не важен.
#
# Если запрашивается правильный формат ячейки, но в нашем контейнере такого ключа нет, то нужно вернуть None. Например:
#
# field = Field()
# print(field["C5"] is None)
# > True
# Примечания
# В своем решении этого задания я использовал в качестве ключей хранимого словаря frozenset, а проверку на ValueError реализовал через регулярку.
# Также рекомендую проверку типов и преобразование поступившего ключа в тот вид, в котором он хранится "под капотом",
# вынести в отдельный метод и вызывать его из всех описываемых магических методов.

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
    def check_type_key(self, key):
        self.key = key
        if (type(self.key) != tuple or type(self.key) != str):
            raise TypeError
        else:
            return True
    def check_pattern_key(self, key):
        self.key = key
        if (re.findall(r'^[a-zA-Z]{1}\d{1,}$|^\d{1,}[a-zA-Z]{1}$', self.key)):
            return True
        else:
            raise ValueError
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
