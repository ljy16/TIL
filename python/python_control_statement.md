# 제어문 (Control Statement)

## 1. 조건문(Conditional Statement)

### if 조건문의 구성

- 문법

```
    if <expression>:
        <code block>
    else:
        <code block>
```

- `expression`에는 일반적으로 참/거짓에 대한 조건식이 들어간다.
- 조건이 참인경우 `:` 이후의 문장을 수행한다.
- 조건이 거짓인 경우 `else:` 이후의 문장을 수행한다.
- 여러개의 `elif`부가 있을 수 있고(없을 수도 있음), `else`는 선택적으로 사용한다.

### 연습문제1
- 조건문을 사용해 사용자가 입력한 날짜가 크리스마스인지 확인하기

```
    date = input('날짜를 입력하세요 ex)12/26')
```

### 조건 표현식(Conditional Expression)
- 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 활용된다.
- 삼항 연산자라고 부르기도 한다.

활용법
```
    true_value if <조건식> else false_value
```

## 2. 반복문(Loop Statement)
- while
- for

### While 반복문
- While 문은 조건식이 참(`True`)인 경우 반복적으로 코드를 실행한다.

> ex) 
> while True:
>   print('조건식이 참일 때까지')
>   print('계속 반복')

주의사항
- 조건식 뒤에 콜론(`:`)이 필요하며, 이후 실행될 코드 블럭은 들여쓰기 해야한다.
- 반드시 종료조건을 설정해야 한다.

### for 문
- for 문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소들을 순회한다.

> ex)
> for fruit in ['apple', 'mango', 'banana']:
>   print(fruit)
> print('끝')