import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성 
print(type(movie))
print(type(genres_list))
a =[]
p =[]
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
                p.sort(reverse=True)
print(p)

    # for x in movie['genre_ids'][0]:
    #     if x in i:
        
    # for x in a:
    #     for t in genre_ids:
    #         c.keys(t)

#     for key,value in c.items():
#         if key == 18 :
#             a.append(value)
#         elif key == 80 :
#             a.append(value)

# print(a)
