# 6. Коллекции. Списки
# С клавиатуры подается 5 чисел, разделенных концом строки.
# Нужно вывести их на экран от большего к меньшему, также разделяя их концом строки.

my_list = []
for i in range(5):
    s = int(input())
    my_list.append(s)
my_list_sorted = sorted(my_list, reverse=True)
for elem in my_list_sorted:
    print(elem)
