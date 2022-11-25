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