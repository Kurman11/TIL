import json
from pprint import pprint
# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
print(type(movie))
print(type(genres_list))
a = []
p = []
genre_ids = movie['genre_ids']
for i in genres_list:
    c = {
        i['id'] : i['name']
    }
    a.append(c)


    for key,value in c.items():
        for x in genre_ids:
            if key == x:
                p.append(value)
                d ={
                'id' : movie['id'],
                'vote_average' : movie['vote_average'],
                'overview' : movie['overview'],
                'genre_names' : p
            }
pprint(d)

