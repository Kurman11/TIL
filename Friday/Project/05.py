import json
from pprint import pprint
# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
print(type(movie))

# print(f"id:{movie['id']}")
# print(f"title:{movie['title']}")
# print(f"vote_average:{movie['vote_average']}")
# print(f"overview:{movie['overview']}")
# print(f"genre_ids:{movie['genre_ids']}")

a = {
    'id': movie['id'],
    'title' : movie['title'],
    'vote_average':movie['vote_average'],
    'overview':movie['overview'],
    'genre_ids':movie['genre_ids']
}

pprint(a)

