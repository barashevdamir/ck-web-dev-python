# 9. Даты
# С клавиатуры вводится дата в формате DD-MM-YYYY.
# Нужно вывести дату начала недели, к которой относится введенная дата (дата понедельника недели), в таком же формате.
# Примечания
# Если введен понедельник - нужно вывести его же.

import datetime

deadline = datetime.datetime.strptime(input(), "%d-%m-%Y")
date1 = deadline - datetime.timedelta(deadline.weekday())

print(datetime.datetime.strftime(date1,"%d-%m-%Y"))
