# branch
> 독립적으로 어떤 작업을 진행하기 위한 개념이다.
필요에 의해 만들어지는 각각의 브랜치는 다른 브랜치의 영향을 받지 않기 때문에, 여러 작업을 동시에 진행할 수 있다.

> 독립적인 작업흐름을 만들고 관리

```bash
$ git branch <이름>
#브랜치 생성
```
```bash
$ git checkout <이름>
# 브래치 이동
```
```bash
$ git checkout -b <이름>
# 브랜치 생성 및 이동
# 더 많이 사용한다 편함
```
```bash
$ git branch -d <이름>
# 브랜치 삭제
```
```bash
$ git branch
# 브랜치 목록
```
> 각 branch에서 작업을 한 이후 이력을 합치기 위해 merge 명령어를 사용

> 병합을 진행할 때, 서로 다른 이력(commit)에서
  * 동일한 파일을 수정한 경우 충돌이 발생
    * 이 경우에는 반드시 직접 해당 파일을 확인하고 적절하게 수정
    * 수정한 이후에 직접 커밋 실행
  * 다른 파일을 수정한 경우
    * 충돌 없이 자동으로 Merge Commit이 생성됨
```bash
$ git merge <이름>
# 브랜치 병합
```
```bash
(hi) $ touch 12월29일.md
# 브랜치 hi에서 파일 생성
```

* master처럼 hi에서도 똑같이 add/commit

```bash
(hi) git log --oneline
# e8023a5 (HEAD -> hi) hi_Update893b517 (origin/master, master) Update
```
```bash
$ git merge hi
# merge로 master /hi 병합
```
```bash
$ git branch -d hi
#브랜치 hi 삭제
```

## GitHub Flow 기본원칙
1. master branch는 반드시 배포 가능한 상태여야한다.
2. feature branch는 각 기능의 의도를 알 수 있도록 작성한다.
3. Commit message는 매우 중요하며, 명확하게 작성한다.
4. Pull Request를 통해 협업을 진행한다.
5. 변경사항을 반영하고 싶다면, master branch에 병합한다.

## 좋은 git 커밋 메시지를 작성하기 위한 7가지
1. 제목과 본문을 한 줄 띄워 분리하기
2. 제목은 영문 기준 50자 이내로
3. 제목 첫글자를 대문자로
4. 제목 끝에 . 금지
5. 제목은 명령조로
6. 본문은 영문 기준 72자마다 줄 바꾸기
7. 본문은 어떻게보다 무엇을, 왜에 맞춰 작성하기

## github Pull Request

1. github 찾아가서 fork 한다
2. fork후 url을 복사해 내 저장소에 clone 한다
3. 내용 수정후 add commit push
4. pull request



