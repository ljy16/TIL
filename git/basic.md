# git

## git 존재이유

     - 버전관리 

## git 기초 명령어
     git init
     git add .
     git restore --staged <file>
     git commit -m 'msg'
     git status
     git log
     git config --global user.name "name"
     git config --global user.email "email@com"


- `git init`

     - 비어 있는 dir에 `.git/` 이라는 파일을 생성시킴. (`.git/`이 있어야 관리가 되기 때문)
     - 아무 기능 없는 디렉토리가 `get init`에 의해 `.git/`을 가지게 되고 업그레이드 된 것.
     - 이것을 `repo(sitory)`라 부름. (dir -> repo가 된 것.)

- `git add`
     - `working directory`에 있는 파일을 `stage`로 이동시킴.

- git restore --staged <file>
     - stage에서 working directory로 내리고 싶을때 사용.

- `git commit`(사진첩)
     - stage에 올라온 파일을 촬영하는 것.
     - 촬영을 다 마쳤으면 working directory로 이동함.

- `git status`
     - 현재 공간의 상황을 알려줌.

- `git log`
     - 지금까지 commit한 내역을 확인할 수 있음.

- `git config --global user.name "name"`
   - 작성자가 누구인지 확인할 수 있도록 등록하는 것.

- `git config --global user.email "email@com"`
   - git 커밋 내역에 기록될 이메일 주소