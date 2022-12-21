# 함수(function) 1
    - 특정한 기능(function)을 하는 코드의 묶음

## 함수를 쓰는 이유
1. 가독성
2. 재사용성
3. 유지보수

## 1. 함수의 선언과 호출
 - 함수의 선언은 `def` 키워드를 사용한다.
 - 함수는 `매개변수(parameter)`를 넘겨줄 수 있다.
 - 함수는 동작후에 `return`을 통해 결과값을 전달한다.
   - 반드시 하나의 객체를 반환한다.(`return`값이 없으면, `None`을 반환한다.)
 - 함수는 호출은 `함수명()`으로 한다.
   - ex) `func(), func(val1, val2)`

### 함수 연습 1
    - 거듭 제곱 연산자를 활용하여 입력 받은 매개변수를 `세제곱`하여 변수에 할당하는 코드 작성하기

```
 def cube(n):
    result = n ** 3
    return result
```

### 함수 연습 2
    - 정수 두개를 받아서 큰 값을 반환한다.
```
    풀이방법 1

    def my_max(x, y):
        if x > y :
            return x
        else:
            return y

    풀이방법 2

    def my_max(x, y)
        result = x

        if x < y
            result = y
        return result
```

## 2. 함수의 Output
### 함수의 `return`
- 함수는 반환되는 값이 있다.
- 어떠한 종류(의 객체)라도 상관없다.
- 단 하나의 객체만 반환된다.
- 함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아간다.


### 함수 연습 3
- 너비와 높이를 입력 받아 사각형의 넓이와 둘레를 반환하는 함수

```
def rectangle(width, height):
    area = width * height
    peri = 2 * (width + height)

    return area, peri
```

### 함수 연습 4
- 리스트 두개를 받아 각각 더한 결과를 비교하여 값이 큰 리스트를 반환하는 함수

```
def my_list_max(list_a, list_b):
    작성해보자
```

## 3. 함수의 입력(input)
### `매개변수(parameter) & 전달인자(argument)`

매개변수(parameter)
```
    def func(x):
    return x+2
```
- x가 매개변수
- 입력을 받아 함수 내부에서 활용할 변수
- 함수를 `정의`하는 부분에서 확인가능

전달인자(argument)
```
    func(2)
```
- 2는 전달인자
- 실제로 전달되는 값
- 함수를 `호출`하는 부분에서 확인가능

### 함수 연습 4
- 원기둥의 반지름과 높이를 받아서 부피를 return하는 함수 작성
```
    def cylinder(r, h):
        v = (3.14 * r ** 2) * h
        return v
```

### 기본 인자 값(Default Argument Values)
- 함수를 정의할 때, 기본값을 지정하여 함수를 호출할 때 인자의 값을 설정하지 않아도 된다.
- 정의된 것보다 더 적은 개수의 인자들로 호출 될 수 있다.

### 함수 연습 5
- 이름을 받아서 다음과 같이 인사하는 함수 `greeting()` 작성하기
- 이름이 길동이면, "길동아 안녕?", 이름이 없으면 "익명,안녕?"으로 출력하기
```
    def greeting(name = '익명'):
        return f'{name}, 안녕?'

print(greeting('재용'))
```

*주의*   
기본 인자값을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수 없음.
```
    ex) 
    def greeting(name='john', age):
        return f'{name]은 {age}살입니다.'

    greeting(26)
    -> 오류 
```
```
    def greeting(age, name='jaeyong'):
        return f'{name}은 {age}살입니다.'
    
    greeting(26)
    -> 정상 작동
```

### 키워드 인자(Keyword Arguments)
- 함수를 호출할 때 키워드 인자를 활용하여 직접 변수의 이름으로 특정 인자를 전달할 수 있다.

```
    def greeting(age, name, address, major):
    return f'{name}은 {age}살이고 {}에 살고 있습니다. 전공은 {major}입니다.'

greeting(26, 'ljy', '강동', '전기전자')


```

### 가변(임의) 인자 리스트(Arbitrary Argument Lists)
- print()처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 함수를 정의할때 가변 인자 리스트 `*args`를 활용한다.
- 가변 인자 리스트는 `tuple` 형태로 처리되며, 매개변수에 `*`로 표현한다.

```
    def func(a, b, *args):
```

### 함수 연습 1
- 정수를 여러 개 받아서 가장 큰 값을 반환하는 함수 작성
- max 내장 함수 사용 금지

```
def my_max()

```

### 가변(임의) 키워드 인자 (Arbitrary Keyword Arguments)
- 정해지지 않은 키워드 인자들은 함수를 정의할때 가변 키워드 인자 `**kwargs`를 활용한다.
- 가변 키워드 인자는 `dict` 형태로 처리가 되며, 매개변수에 `**`로 표현한다.

```
    def func(**kwargs):
        **kwargs : 임의의 개수의 키워드 인자를 받음을 의미한다.
```

### 연습 2
- my_url() 함수를 만들어 완성된 url을 반환하는 함수 작성

```
    def my url(url, **kwargs) :

```


# 함수(function) 2

1. 함수와 스코프
2. 재귀 함수
3. 함수 응용

## 1. 함수와 스코프(scope)

- 함수는 코드 내부에 스코프를 생성한다.
- 함수로 생성된 공간은 `지역 스코프(local scope)`라고 하며
- 그 외 공간은  `전역 스코프(global scope` 이다.

### 예시

```
    # 전역 스코프
    a = 10

    def func(b):
        b = 10 # 지역 스코프
        c = 20 # 지역 변수
        print(a, b, c)

    func(a)
```

## 2. 재귀함수

### 연습문제
> 현재 단계가 1단계라면 더 이상 재귀호출을 하지않고 1을 반환한다.
> 그렇지 않은 경우에는 (현재 단계의 숫자 * 이전 단계의 재귀 함수의 실행결과)를 반환한다.

```
    def factorial(n):
        if n == 1 :
            return 1
        
        return n * factorial(n-1)
```

## 3. 함수 응용

### map(function, iterable)
- 순회가능한 데이터 구조(iterable)의 모든 요소에 function을 적용한 후 그 결과를 돌려준다.
- return은 `map_object` 형태이다.

```
    # 문자열을 숫자로 변환해보자
    s = '3 3 4 5 8' # [3, 3, 4, 5, 8]로 바꿔야함.

    new_list = []
    for 
```

### filter(function, iterable)
- iterable에서 function의 반환된 결과과 `True`인 것들만 구성하여 반환한다.
- `filter object`를 반환한다.
- 