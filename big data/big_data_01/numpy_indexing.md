# 0126 Numpy - indexing
* 넘파이에서 ndarray내의 일부 데이터 셋이나 특정 데이터만을 선택할 수 있도록 하는 인덱싱에 대해 공부해보았다.

## 1. 특정한 데이터만 추출
```
import numpy as np
arr1 = np.arange(1,10)
arr1d = arr1.copy()
(copy -> 주소값이 변경되지 않는 얕은 복사)
arr2d = arr1d.reshape(3,3)
print(2d)
```
[[1 2 3]

[4 5 6]

[7 8 9]]

```
print(arr2d[0,0])
print(arr2d[1,1])
```
 - 위와 같은 형태에서 `1` 또는 `5` 같은 특정 데이터를 추출할 수 있다.


## 2. 슬라이싱(Slicing)- 2차원
```
print(arr2d)
print(arr2d[0:2, 0:2])
print(arr2d[1:3, 0:3])
```
- arr2d에서 
    - 첫번째 `[0:2]`의미 : 0부터 1행까지 
    - 두번째 `[0:2]`의미 : 0부터 1열까지 
    
## 3. 팬시 인덱싱(Fancy Indexing)
```
arr2d[[0,2], 2:]
```
array( [[3], [9]] )

- 0과 2번 행에서 2열까지 슬라이싱 해서 가져오겠다 -> 2차원으로 가져와진다.