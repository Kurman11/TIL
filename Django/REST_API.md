1. djangorestframework 다운
pip install djangorestframework

이건 왜?
pip install markdown      
pip install django-filter

2. project > settings.py에 App 추가 'rest_framework'
3. project > urls.py에 ex) path('api/v1/articles/', include('articles.urls')) 작성
4. app >  urls.py 작성 ex) path('',views.article_list)
5. app > serializers.py 파일 생성
6. forms과 비슷하게 작성

> 지금 까지 배운 CRUD를 생각하며 접근했습니다.
* Create = POST
* Read = GET
* Update = PUT
* Delete = DELETE
