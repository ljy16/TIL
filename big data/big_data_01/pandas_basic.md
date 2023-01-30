# 0130 정리

### pandas로 여러가지 해보기

0. pandas는 축약어 `pd`
   ```
    import pandas as pd
   ```

1. 상대경로 설정하는 법
 - * pd.read_csv('/폴더명/csv 파일명)

2. 데이터에서 상단 n개 컬럼만 추출하기
   - titan_df.head(n) / head함수 사용

3. 단일 요소 추출
   1. iloc 함수 (위치 기반 인덱싱)
    - titan_df.iloc[0,3]
    - titan_df라는 데이터프레임에서 0번째 행에서 3번 인덱스 컬럼 요소 추출

    2. loc 함수 (명칭기반 인덱싱)
    - titan_df.loc[0, '컬럼명']
    - 위와 동일

4. 원하는 컬럼 추출
   - titan_df[['컬럼명1', '컬럼명2', '컬럼명3']].head()
   - dataframe은 2차원이므로 리스트를 두개 사용해서 가져오고 싶은 컬럼명 n개 지정하고 head로 추출

5. 특정 컬럼명 갯수 추출
   - title_df[['컬럼명1', '컬럼명2']].value_counts()

6. 행과 열 추가/삭제
    1. 열 추가
   - titan_df['추가할 컬럼명'] = 넣을 값
   - ex) 'titan_df['Age'] = 10
  
    2. 열 삭제
    - titan_df.drip('Age', axis=1, inplace=True)
    - axis=1이 열의 의미고, inplace=True는 원본컬럼에서 지우는 방법

