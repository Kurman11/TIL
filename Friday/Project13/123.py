import requests


def popular_count():
    url =f'https://api.themoviedb.org/3/movie/76341?api_key=0b62813d9d8d3c1c77f760c5d3ef3f52'
    # BASE_URL = 'https://api.themoviedb.org/3'
    # path = '/movie/'
    # params = { 
    #     'api_key' :'0b62813d9d8d3c1c77f760c5d3ef3f52',
    #     'language' : 'ko-KR'
    # }
    response =  response.get(url).json()
    print(response)
    pass 
    # 여기에 코드를 작성합니다.  