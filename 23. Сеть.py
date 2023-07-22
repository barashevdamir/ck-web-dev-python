# 23. Сеть
#Задание
# Здесь описано некоторое API, в котором есть доступ к базе пользователей, постов, комментариев и т.д.
# Методы, которые мы будем использовать, описаны в разделе Resources.
# Примеры использования API (правда, на JavaScript'е) описаны на том же сайте по ссылке Guide.
# Вам нужно для каждого пользователя посчитать количество оставленных постов и количество оставленных комментариев.
# Всю информацию для этого нужно стягивать GET-запросами по API.
# Результат нужно отправить в ваше пространство в https://webhook.site в виде POST-запроса, содержащего JSON следующего формата:
#
#   "statistics": [
#     {
#       "id": 1,
#       "username": "lolkek",
#       "email": "user1@mail.dot",
#       "posts": 125,
#       "comments": 1358
#     },
#     {
#       "id": 2,
#       "username": "cheburek",
#       "email": "user2@mail.dot",
#       "posts": 5,
#       "comments": 12
#     }
#   ]
# }
# Поскольку среда исполнения Яндекс-контеста не имеет доступа к интернету,
# проверить правильность выполнения задания вы можете, отправив в качестве ответа на задание "Сеть" pickle объекта ответа запроса:
#
# response = requests.post(.....)
# with open("solution.pickle", 'wb') as f:
#     pickle.dump(response, f)
# И отправляйте тот файл, который появится в результате исполнения этого кода.

import requests
import json
import urllib.parse
import pickle
def posts_count(json_string, id):
    count = 0
    for x in json_string :
        if x["userId"] == id:
            count += 1
    return count
def comments_count(json_string, email):
    count = 0
    for x in json_string :
        if x["email"] == email:
            count += 1
    return count
users = requests.get('https://jsonplaceholder.typicode.com/users')
posts = requests.get('https://jsonplaceholder.typicode.com/posts')
comments = requests.get('https://jsonplaceholder.typicode.com/comments')
r = []
res: dict = {}
for x in users.json():
    res['id'] = x['id']
    res['username'] = x['username']
    res['email'] = x['email']
    res['posts'] = posts_count(posts.json(), x['id'])
    res['comments'] = comments_count(comments.json(), x['email'])
    r.append(res)
    res = {}
result = {'statistics': r}
__response = json.dumps(result)
print(__response)
BASE_URL = "https://webhook.site/ee6c9327-f6ba-4e69-84e5-1a7dba0cc18a"
response = requests.post(BASE_URL, data=__response)
with open("solution.pickle", 'wb') as f:
    pickle.dump(response, f)