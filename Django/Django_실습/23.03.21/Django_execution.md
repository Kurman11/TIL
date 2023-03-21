# git bash

1. 폴더 생성후 폴더에서 git bash Here를 실행

2. 명령 프롬프트에서 가상환경을 생성한다.
  * python -m venv venv

3. 명령 프롬프트에서 가상환경 활성화 한다.
  * source vevn/Scripts/activate

4. 명령 프롬프트에서 django 설치한다.
  * pip install django==3.2.18

5. 명령 프롬프트에서 의존성 파일 생성(패키지 설치시마다 진행)
  * pip freeze > requirements.txt

6. vscode로 이동

7. .gitignore 파일 생성(첫 add전)
  * https://www.toptal.com/developers/gitignore에서 .gitignore에 들어갈 내용 찾아서 복사해서 넣기(windows,macOS,python, Django, VisualStudioCode)
**6,7번은 git관련 설정 시에 실행**

8.  vscode에서 ctrl + shift + P를 눌러 Python: Select interpreter를 검색하고 선택이후 Python 3.9.xx('venv':venv)를 선택

9. 이후 ctrl + shift + `를 눌러 터미널을 새로 생성

10. django 프로젝트 생성
  * django-admin startproject 프로젝트명 .

11. 서버 실행
  * python manage.py runserver

# VScode

1. 터미널에서 가상환경을 생성한다.
  * python -m venv venv

2. ctrl + shift + p를 눌러 Python: Select interpreter를 검색하고 선택이후 Python 3.9.xx('venv':venv)를 선택

3. 이후 ctrl + shift + `를 눌러 터미널을 새로 생성

4. 터미널에서 장고를 설치한다.
  * pip install django==3.2.18

5. 터미널에서 의존성 파일 생성(패키지 설치시마다 진행)
  * pip freeze > requirementes.txt

6. django 프로젝트 생성
  * django-admin startproject 이름 .

7. 서버 실행
  * python manage.py runserver

8. 앱 생성 
> 위의 서버에서 빠져나와 앱(articles) 생성
  * ctrl + C 이후 python manage.py startapp articles

9. 앱 등록
> 아까 생성한 프로젝트(practice)폴더를 열고 settings.py 파일을 열어 앱을 등록해준다.
  * 단 앱 등록 권장 순서를 생각하자!
  1. local app
  2. 3rd party app(설치를 통해 추가하는 앱)
  3. 기본 django app
  
  일단 맨위 상단에 아까 만든 app 이름을 추가
  'articles',

10. URLs
> 프로젝트(practice)에있는 urls.py 파일을 열고 기본적으로 적혀있는
path('admin/', admin.site.urls), 밑에 새로운 path('articles/',articles의 모듈명을 적어준다.)

11. View
> articles폴더에 있는 views.py에 10번의 urls.py에 들어가 모듈명 함수를 만들어준다.

12. URLs
> 다시 프로젝트(practice)에 urls.py로 돌아와서 from articles import views를 선언해준다.

13. app(articles)에 templates 폴더를 생성해준다.

14. templates안에 views.py의 생성한 함수명.html을 만들고 내용을 작성한다.

15. 다시 views.py로 넘어와서 return 을 작성해준다
return(request,'index.html' 경로를 적어주자')

16. 다시 프로젝트(practice)의 urls.py로 넘어와서 10번의 모듈명 자리에 views.index **여기서 index()를 적으면 안된다.**

17. 이제 http://127.0.0.1:8000/로 들어가면 해당 페이지는 404페이지로 나온다 http://127.0.0.1:8000/articles로 접속하여 작성한 html 내용이 출력되는지 확인한다!!