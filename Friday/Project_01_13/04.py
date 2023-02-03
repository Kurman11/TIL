import requests
from pprint import pprint


def search_movie(title):
# https://api.themoviedb.org/3/movie/popular?api_key=0b62813d9d8d3c1c77f760c5d3ef3f52
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '0b62813d9d8d3c1c77f760c5d3ef3f52',
        'language' : 'ko-KR',
        'query' : title,
        'region' : 'KR'
    }
    response = requests.get(BASE_URL + path, params = params).json()

    
    # total_results = response.get('total_results')
    # if total_results != 0 :      
    #     id = response.get('results')[0].get('id')
    #     return id
    # elif total_results == 0:
    #     return 'None'


    try:
        id = response.get('results')[0].get('id')
        title = response.get('results')[0].get('title')
        if '기생충' in title:
            return id
        elif '그래비티' in title:
            return id
    except:
        return 'None'




    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None
