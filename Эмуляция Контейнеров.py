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
        if (type(self.key) != tuple or type(self.key != str)):
            return TypeError
        else:
            return True
    def check_pattern_key(self, key):
        self.key = key
        if (re.findall(r'^[a-zA-Z]{1}\d{1,}$|^\d{1,}[a-zA-Z]{1}$', self.key)):
            return True
        else:
            return ValueError
    def check_key (self, key):
        if (self.check_pattern_key(self, key) and self.check_type_key(self, key)):
            if type (self.key) == str:
                word = "".join(" " if el.isdigit() else el for el in key).split()
                number = "".join(el if el.isdigit() else " " for el in key).split()
                word = list(map(lambda x: x.lower(), word))
                word = frozenset(word)
                number = frozenset(number)
                key_frozen = word.union(number)
            else:
                key_frozen = frozenset(key)
            #    self.key = convert_tuple(key)
            key_low = key.lower()
            self.key = key_frozen
            return self
    def __setitem__(self, key, value):
        super(Field, self).__setitem__(key, value)
    def __delitem__(self, key, value):
        super(Field, self).__delitem__(key)
    def __missing__(self, key, value):
        return False
    def __contains__(self, item):
        return self[item] != self.__missing__(1)
