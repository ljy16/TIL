# 데이터 구조(Data Structure)

## 순서가  있는 데이터 구조

## 1. 문자열(String)
    > 변경할 수 없고, 순서가 있고, 순회 가능한

`find(x)`
- x의 첫 번째 위치 반환 , 리스트 내에 x가 없으면 `-1` 반환
```
    ex)

    a = 'apple'
    a.find('p')

    # 출력값 -> 2
```

`index(x`
- x의 첫번째 위치 반환, 리스트 내에 x가 없으면 `오류` 발생 (index와 기능은 동일하나 리스트 내에 인자가 없을 때 어떤 값을 반환하는지가 차이점)

## 문자열 변경
`.replace(old, new[, count])`

- 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
- count를 지정하면 해당 갯수만큼 시행

```
    ex)

    a = 'yaya'
    b = 'woowoo'

    a.replace('y', 'h')
    # 출력값 : 'yaya' /  왜냐? -> 문자열은 불변형이기 때문

    b.replace('o', '_', 2)
    # 출력값 : 'w__woo
```

`.strip([chars])`
- 특정한 문자들을 지정하면, 양쪽을 제거하거나(`strip`), 왼쪽을 제거하거나(`lstrip`), 오른쪽을 제거합니다.(`rstrip`)

