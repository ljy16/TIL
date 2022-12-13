# git

## git 사용 시 주의사항
1. 현재 위치 잘 확인하기
2. repo 안에서 repo 만들지 않기. (repo -> master 표시되어 있음)
     1. 이미 git init을 한 곳에
     2. 다른 폴더 만들고
     3. 그 하위 폴더에서 git init하지 않기
     4. master 있으면 init 하면 안됨.
3. home(~) 폴더에서 init 하지 않기
4. (지금은)github에서 직접 수정하지 않기
     

## 계정 세팅
```sh
# (계정당 1회) 이름과 메일이 등록
$ git config --global user.name '이름'
$ git config --global user.email `github에서 쓸 메일주소`
# 서명이 정상적으로 등록되었는지 확인
$ cat ~/.gitconfig
```

### 프로젝트 생성 ~ push
```sh
# 프로젝트 폴더 생성
$ mkdir new_project

# 프로젝트 폴더로 이동
$ cd new_project

# README 파일 & .gitignore 생성
$ touch README.md .gitignore

# 생성한 폴더를 리포로 초기화
$ git init

# README & .gitignore 파일 add (tracking)
$ git add .

# commit
$ git commit -m 'first commit'

# 생성한 원격 저장소 등록 (origin은 별명)
$ git remote add origin <URL>

# 등록된 저장소 확인
$ git remote -v

# 지금까지의 commit한 것들 push
$ git push origin master
```
---





### 명령어 정리

`1. 리포 초기화 시점에 최초 1회만 입력`


```sh
$ git init
```
 - 비어 있는 dir에 `.git/` 이라는 파일을 생성시킴. (`.git/`이 있어야 관리가 되기 때문)
 - 아무 기능 없는 디렉토리가 `get init`에 의해 `.git/`을 가지게 되고 업그레이드 된 것.
 - 이것을 `repo(sitory)`라 부름. (dir -> repo가 된 것.)


`2. 작업 후 스테이징`

```sh
# 특정 파일만 add 할 때
$ git add <filename> .

# 현재 전체 폴더 add 할 때
$ git add .
```
 - `working directory`에 있는 파일을 `stage`로 이동시킴.

`3. 커밋 진행`
```sh
#메시지는 짧지만 내용은 담아서
$ git commit -m 'msg'
```

  - stage에 올라온 파일을 촬영하는 것.
  - 촬영을 다 마쳤으면 working directory로 이동함.

`4. 모니터링 명령어`
```sh
#현재 Working dir와 Stage 상황 학인
$ git status

#commit 로그
$ git log

#commit 로그 짧게
$ git log --oneline
```

`5. github에 원격 저장소(remote repo) 생성하기 (github site에서 'New Repository')`

`6. 원격 저장소 추가하기`

```sh
$ git remote add <name> <URL>
```
 - local repo과 remote repo를 연결시켜주는 작업
- 쉽게 말하면 local repo는 내컴퓨터이고 remote repo는 깃허브
- name은 origin이 디폴트 값이고 굳이 수정하지 않음.

`7. 원격 저장소 확인`

```sh
$ git remote -v
```

`8. 원격 저장소에 지금까지 commit한 것 push 하기`

```sh
$ git push origin master
```

9. 새로운 컴퓨터에서 기존 원격 저장소 복제하기
```sh
$ git clone <URL>
```

`10. 원격 저장소의 내용 받아오기`
```sh
$ git pull origin master
```
