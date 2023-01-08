import json
from pprint import pprint
# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
print(type(movies_list))
a=[]
for i in movies_list:
    c ={
        'id' : i['id'],
        'title' : i['title'],
        'poster_path' : i['poster_path'],
        'vote_average' : i['vote_average'],
        'overview' : i['overview'],
        'genre_ids' : i['genre_ids'],
    }
    a.append(c)
pprint(a)
