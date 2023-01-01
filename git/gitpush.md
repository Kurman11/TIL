# 12월 28일


## 원격 저장소 저장! TIL 만들기
* githun에서 Create a new repository 에서 먼저 test 만들기

```bash
$ git remote add origin URL
# 깃아 원격저장소에 추가해줘 오리진으로 URL로
```



## push
``` bash
$ git push origin master
# push 하고 github에 가서 확인!
# 최근 커밋 내용만 깃헙에서 확인가능!
```
## 내가 한 로컬 프로젝트 개발 공유
```bash
$ git push
```

## pull
```bash
$ git pull origin master
# origin에 저장 되어있는 최신 내용을 pull로 받아온다(업데이트!)
```
## 프로젝트 개발 중 다른 사람 커밋 받아오기?
```bash
$ git pull
# Pull : 원격저장소 커밋 가져오기
```

## 받아온다?
* 다운로드는 가장 최신 버전의 상태의 파일만 받는 것.
```bash
$ git clone URL
# clone는 git 저장소를 받아오는 것
# 모든 버전을 받은 것
```
``` bash
$ git clone
# 협업 프로젝트, 외부 오픈소스 참여
# git 저장소를 github에서 생성 후 시작
```


## 명령어 정리
```bash
$ git clone <URL>
# 원격 저장소 복제
$ git rermote -v
# 원격저장소 정보 확인
$ git remote add <원격저장소> <URL>
# 원격저장소 추가(일반적으로 origin)
$ git remote rm <원격저장소>
# 원격저장소 삭제
$ git push <원격저장소><브랜치>
# 원격저장소에 push
$ git pull <원격저장소><브랜치>
# 원격저장소로부터 pull
.gitignore 
# git 파일/폴더 등을 관리X 
# 버전관리랑 상관없는 파일
# 미리 .gitignore를 설정하자!!
# https://github.com/github/gitignore 나중에 사용하자 
# https://www.toptal.com/developers/gitignore/ 나중에 사용하자
```



