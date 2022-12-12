# markdown 기초문법

## 리스트

### 순서가 있는 리스트 (ordered list)
1. 손 씻기
   1. 물 틀기
   2. 손 뻗어
   3. 물 적셔
   4. 비누 칠해
2. 식당에 가기
3. 밥 먹기
4. 계산하기
5. 양치하기

### 순서가 없는 리스트(unordered list)
- 돈까스   
- 라볶이
    1. 1
    2. 2
    3. 3
    4. 4


## 인라인 강조
중요한 것은 **굵게 표시**하고 주의할 것은 *기울이고* `코드 혹은 명령어`는 따로 표시 하고싶다.

- 굵게 할 때는 * 두 개로 감싼다.(**bold**)
- 이탤릭 체는 *(Asterisk) 한 개로 감싼다. (*italic*)
- 코드 혹은 명령어는 backtick 두 개로 감싼다.(`code`)

---

## 블럭 강조

### 표
파이프로 구분하여 테이블 헤더를 생성한다.

|명령어|설명|예시|
|-|-|-|
|`mkdir`|폴더(디렉토리)를 생성한다.|`$ mkdir my_dir`|
|`touch`|파일을 생성한다.|`$ touch a.txt`| 
|`rm`|파일을 삭제한다.|`$ rm a.txt`|
|`rm -r`|폴더(디렉토리)를 삭제한다.|`$ rm -r my_dir`|
|`ls`|현재 위치 폴더의 모든 하위 항목 표시|`$ ls`|
|`ls -a`|숨겨진 파일까지 모두 표시|`$ ls -a`|
|`cd`|디렉토리로 이동한다.|`$ cd my_dir`|
|`ctrl + c`|취소(`c`ancle)|
|`ctrl + l`|터미널 정리(c`l`ear)
|`~`|홈(Home) 폴더 상징 기호|`$ cd ~`|
|`/`|최상단(Root) 폴더 상징 기호|`$ cd /`|
|`.`|현재 위치 상징 기호|`$ code .`|
|`..`|현재 기준 상위 폴더 상징 기호|`$ cd..`

### 코드
아래와 같이 진행한다.
```
$ mkdir my dir
$ cd mydir
$ touch a.txt
$ rm a.txt
```
## 기타

### 인용문

> 일단 유명해 져라. 그러면 너가 똥을 싸도 박수칠 것이다.



### 수식

$$
\mathbb{N} = \{ a \in \mathbb{Z} : a > 0 \}
$$


### 이미지 / 하이퍼링크
```
link

[표시 텍스트](링크)

image
![대체 텍스트](링크)

```

[구글](https://google.com)

![img](https://search.pstatic.net/sunny/?src=https%3A%2F%2Fwww.coinreaders.com%2Fdata%2Fcoinreaders_com%2Fmainimages%2F202108%2F133255_202104152404708.jpg%3Fti%3D1670501833&type=fff264_180)