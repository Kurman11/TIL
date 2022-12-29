# CLI
1. 명령어 인터페이스 이다.
2. 내가 무엇인가를 알고 싶으면, 명령을 하고 그 결과를 읽어야한다.
3. 불편한 것이 아니라 `전혀 다르게` 생각하고 조작하자
***
내생각
CLI는 라즈베리파이 리눅스 느낌?? 이다
GUI는 파일?
***

## git.bash
git.bash 라즈베리파이 같음

1. 폴더 생성 mkdir
    - 폴더 삭제 rm
2. 파일 생성 touch
    - 파일 삭제 rm -rf

## GIT

리누스 토르발스가 만들었다.
- 버전관리!!
- git은 분산버전관리시스템을 코드의 버전을 관리하는 도구
  - 중앙집중식버전관리시스템
    - 로컬에서는 파일을 편집하고 서버에 반영
    - 중앙 서버에서만 버전을 관리
  - 분산버전관리시스템 -> git
    - `로컬에서도 버전을 기록`하고 관리
    - 원격 저장소를 활용하여 협업

## 명령어

git init

git 버전 관리 기초
1. 작업을 하고
2. 변경된 파일을 모아(add)
3. 버전으로 남긴다(commit)

***
내생각

git은 게임에서의 save 파일 같음

중간에 저장하면 그 지점부터 시작 가능 또한 최신 버전으로도 저장 가능

버전 이동이 자유롭다?
***

git add -> git commit 

git commit-m(커밋메시지) : 커밋 메시지는 변경 사항을 나타낼 수 있도록 명확하게 작성해야 함

Untracked files
- 트래킹되지 않은 파일들
- 상황 1.txt 를 만들었지만,add 하지 않음

Changes to be committed
- 커밋될 변경사항들
- 상황 보고서.txt 만들고 add함

nothing to commit, working tree clean

- 커밋할게 없습니다. 작업트리가 꺠끗 합니다.
- 1통,2통 비어있음!
- 상황 모두 add,commit 한 이후

changes not staged for commit
- 커밋을 위해 staged가 아닌 변경사항들
- 상황 커밋된적 있는 보고서.txt 파일을 수정한 상태!

>status로 확인할 수 있는 파일의 상태

- 1통 2통 확인

1. Tracked : 이전부터 버전으롤 관리되고 있는 파일 상태
 - Unmodfiled : git status에 나타나지 않음(X)
 - Modified : Changes not staged for commit(1통)
 - Staged : Changes to bo committed(2통)

 ># git 기초용어

- git init
  - 로컬 저장소 생성
- git add<파일명>
  - 특정 파일/폴더의 변경사항 추가
- git commit -m '<커밋메시지>'
  - 커밋(버전 기록)
- git status
  - 상태 확인
- git log
  - 버전 확인
- git show
  - 가장 최신 commit의 정보를 출력