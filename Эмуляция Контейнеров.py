import re
# def check_string(string):
#     phone = re.sub(r'\b\D', '', string)
#     phone_cleared = re.sub(r'[\ \(]?', '', phone)
#
#     if re.findall(r'^[\+7|8|7]*?\d{10}$', phone_cleared) or re.match(r'^\w+[\.]?(\w+)*\@(\w+\.)*\w{2,}$', string):
#         return (bool(string))
#     else:
#         return (False)
class Field(dict):
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        """Функция, которая используется для текстового представления объекта в случаях, когда это происходит не
        через функцию str(obj)"""
        return str(self)

    def check_pattern(key):
        if (re.findall(r'^[A-Za-z]\w{1}(\d+)$', )):
            return bool(key)
        else:
            return ValueError
    def check_key (key, value):
        if (type(key) != tuple or type(key != str)):
            return TypeError
        else:
            if (check_pattern(key)):
                if type (key) == tuple:
                    key = ''.join(key)
                key_low = key.lower()
                key_frozen = frozenset(key_low)
                return key_frozen
    def __setitem__(self, key, value):
        key = check_key(key)
        super(Field, self).__setitem__(key, value)
    def __delitem__(self, key, value):
        super(Field, self).__delitem__(key)
    def __missing__(self, key, value):
        return False
    def __contains__(self, item):
        return self[item] != self.__missing__(1)
