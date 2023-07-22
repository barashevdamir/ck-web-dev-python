# 14. Файлы
# Напишите функцию get_popular_name_from_file(filename), которая считывает файл, в котором в каждой строке записаны имя и фамилия через пробел.
# filename - это имя файла, в котором записаны эти имена. Вам нужно вернуть строку - самое популярное имя в файле.
# Если таких имен несколько, они должны быть перечислены через запятую внутри строки в алфавитном порядке.

from collections import defaultdict


def get_popular_name_from_file(filename):
    a = list()
    with open(filename) as f:
        for line in f:
            s = line
            s = s.split(' ')[0]
            a.append(s)
    b = set(a)
    result = {}
    for e in b:
        result[e] = a.count(e)

    sorted_dict = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    result = []
    for key, value in sorted_dict.items():  # Проход по .items() возвращает кортеж (ключ, значение),
        if value == list(sorted_dict.values())[0]:
            result.append(key)

    return ", ".join(result)