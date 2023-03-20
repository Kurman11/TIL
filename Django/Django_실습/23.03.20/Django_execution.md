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

