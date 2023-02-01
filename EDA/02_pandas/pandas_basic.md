# 0130 정리

### pandas로 여러가지 해보기

0. pandas는 축약어 `pd`
```
import pandas as pd
```

`1. 상대경로 설정하는 법`
```
pd.read_csv('/폴더명/csv 파일명)
```

`2. 데이터에서 상단 n개 컬럼만 추출하기`
```
titan_df.head(n) / head함수 사용
```

`3. 단일 요소 추출`
   1. iloc 함수 (위치 기반 인덱싱)
       - titan_df.iloc[0,3]
       - titan_df라는 데이터프레임에서 0번째 행에서 3번 인덱스 컬럼 요소 추출

   2. loc 함수 (명칭기반 인덱싱)
       - titan_df.loc[0, '컬럼명']
       - 위와 동일

`4. 원하는 컬럼 추출`
```
titan_df[['컬럼명1', '컬럼명2', '컬럼명3']].head()
```
   - dataframe은 2차원이므로 리스트를 두개 사용해서 가져오고 싶은 컬럼명 n개 지정하고 head로 추출

`5.  특정 컬럼명 갯수 추출`
```
title_df[['컬럼명1', '컬럼명2']].value_counts()
```

`6.행과 열 추가/삭제`
   1. 열 추가
  ```
  titan_df['추가할 컬럼명'] = 넣을 값
   ex) 'titan_df['Age'] = 10
  ```
  
   2. 열 삭제
   ```
   titan_df.drop('Age', axis=1, inplace=True)
   ```
   -  axis=1이 열의 의미고, inplace=True는 원본컬럼에서 지우는 방법

   3. 행 삭제
   ```
   titan_df.drop([1,3]), axis=0, inplace=True)
   ```
   - 1번, 3번 인덱스의 행을 삭제하겠다. (axis=0 -> 행 의미)

# 0131 정리

1. 결측치 확인
```
tian_df.isna().sum()
```  

2. 결측치 대치(imputation)
```
age_mean = titan_df['Age'].mean()
titan_df['Age'].fillna(age_mean, inplace=True)
```
- `Age`컬럼의 null값을 평균값으로 대체한다.

3. 범주형 데이터의 빈도값 확인 -> value_counts()함수
```
titan_df.Sex.value_counts()
```

4. 컬럼명 변경하기
```
titan_df.rename(columns={'Sex' : 'Gender'}, inplace=True)
```
# 0201 정리
1. 행렬의 정렬 - sort()
```
import numpy as np
org_arr = np.array([94,97,26,29])

# np.sort()로 정렬 시 원본 변하지 않음
sort_arr1 = np.sort(org_arr)

# ndarray.sort()로 정렬 시 원본 변함
sort_arr2 = org_arr.sort()
```

2. 행렬의 내적(행렬곱)


3. 연습문제 복습
   1. 50살 초과 사람들 추출하고 인덱스 초기화, 상위5개 데이터만
   ```
   titan_df[titan_df.Age > 50].reset_index().head(5)
   ```

   2. 특정 컬럼으로 구성된 데이터 프레임 정의하기
   ```
   new_df = chip_df[['quantitiy, 'item_name', 'item_price']]
   ```

   3. 특정 컬럼에서 특정 단어가 포함된 데이터 추출하기
   ```
   chip_df[chip_df.item_name.str.contains('Burrito)].item_name.value_counts()
   ```

   4. 전체 데이터 결측값 개수 구하기
   ```
   chip_df.isna().sum()
   ```