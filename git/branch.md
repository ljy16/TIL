# 20230119

# 1. git 기초
파일 참조 : https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EC%88%98%EC%A0%95%ED%95%98%EA%B3%A0-%EC%A0%80%EC%9E%A5%EC%86%8C%EC%97%90-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0

- 워킹디렉토리 : 작업폴더
- Untracked : 관리대상 아님 -> 삭제의 의미가 아니라 git에서 내릴수 있다.
```
git rm --
```
- Tracked : 관리대상
  1. Unmodifed(수정하지 않음)
  2. Modified(수정함)
  3. staged
- untraced 파일은 tracked한다? -> `git add <filename>`

- add를 한다는것은 staged 단계로 올리는 것
- commit을 한다는 것은  Unmodifed상태가 된다는것

- commit을 한다는 의미 -> Unmodified(수정할게 없다.)

- 파일의 상태확인하는 법?
  ```
  git status
  ```

- 어떤 내용이 변경되었는지 보려면?
```
git diff
```
*git diff하고 `$`가 아닌 `:`가 나오면 `q`입력하고 빠져나오면된다.*

- commit한 메시지 보려면?
```
git log --oneline
```

<꿀팁>
1. ctrl + r -> 내가 이전에 썻던 코드 일부만 입력해도 바로 나옴 
- 밖으로 나오는 코드 `ctrl+c`

2. code ~/.bash_profile로 파일 들어가고
```
alias gl='git log --oneline --graph
alias jn='jupyter notebook
```
 - 본인이 단축키로 사용하고 싶은 명령어 설정할 수 있음 (alias 뒤)
 - *주의할점* -> `'='`좌우로 띄어쓰기 하면 안됨.
---
# 2. Git 브랜치 - 브랜치란 무엇인가
1. 브랜치 생성
```
git branch <b1>
```
브랜치는 스티커라고 생각하면 됨

```
git switch b1
```
- -> HEAD를 master에서 b1으로 이동하겠다.(switch의 역할 : 헤드 이동)
 - HEAD가 master에서 b1으로 갔다 = b1으로 브랜치를 이동하겠다
 - 내 헤드가 어디있느냐? -> master 또는 b1으로 구분

branch하는 이유? -> Merge하기 위해(나중에 합치기 위해)
합치는 과정에는 3가지가 있다.
### 1. Fast-foward (하나만 움직인다. / 추가커밋x)
- `도전을 여러번 해도 master는 안전함`
- 정상 동작하는 소프트웨어가 master임(배포 브랜치라고 생각해도됨. / 실제 사용자가 사용할 때가 master로 merge하는 시점)
```
git merge b1 
```
- 단, HEAD는 master에 있어야 함.

```
git switch -c b2
```
- 생성과 이동을 같이 하는 코드
- b2 브랜치를 생성하고(create) HEAD를 b2로 이동한다.

### 2. 자동 merge(commit이 자동으로 생김./ 흔하지 않음)
### 3. Conflict(흔한일, 추가commit 내가해야함.)

- branch다 했으면 지우자
- branch지우는 코드
```
git branch -d b1
```

- pull/push 케이스
1. push 함 -> 안됨 -> pull 함 -> 별일없음 -> push

2. push 함-> 안됨 -> pull 함-> 에러메시지 -> 고침 -> add/commit -> push

3. push 함 -> 잘됨 -> 끝