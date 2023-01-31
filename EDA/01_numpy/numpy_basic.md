# Numpy 기초

- `import numpy as np`

## 1. 차원의 사례
---

###  1차원 자료 생성
```
a = [1,2,3]
b = np.array(a)

print(b)
```
-> `[1 2 3]` 으로 콤마 없이 출력됨.
 
---

### 2차원 자료 생성
```
arr2d = np.array([[1,2,3], [4,5,6]])
print(arr2d)
print(arr2d.shape)
```
-  `[[1 2 3] [4 5 6]]` 
- `(2,3)으로 출력됨`
 - -> np.array로 설정하면 리스트 안에 콤마 없이 출력됨 
 - -> 2가 2차원, 3이 1차원을 의미한다.

### 3차원 자료 생성
```
arr3d = np.array([
    [[1,2,3],[11,22,33]], [[12,34,56],[7,8,9]]
    ])
print(arr3d.shape)
```
 - `(2,2,3)`으로 출력됨 -> 3차원 내에 2개가 있고 2차원 내에 2개가 있고 1차원 내에는 3개의 컬럼 존재

---

## 2. ndarray 편리하게 생성 - arange, zeros, ones
### - arange
```
seq_arr = np.arange(1,11)
print(seq_arr)
```
- 출력값 : `[ 1 2 3 4 5 6 7 8 9 10]`

### - zeros
```
zero_arr = np.zeros((3,2), dtype='int32')
print(zero_arr)
```
- 출력값 : `[[0 0] [0 0] [0 0]]`

### - ones
```
one_arr = np.ones((3,2), dtype='float64')\
print(one_arr)
```
- 출력값 : `[[1. 1.] [1. 1.] [1. 1.]]`

## 3. reshape의 용례
```
seq_arr.reshape(2,5)
```
- 출력값 : `array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])`

## 4. numpy의 dtype
### numpy의 데이터 타입은 다 같은 타입으로 구성된다
```
l3 = [1,2,5.5]
arr_l3 = np.array(l3)
print(arr_l3, arr_l3.dtype)
```
`[1.  2.  5.5] float64`로 출력됨.

### 6. dtype의 상호 변환