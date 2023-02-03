# 0203
## 1. 사이킷런이란?
- 파이썬 머신러닝 라이브러리 중 가장 많이 사용되는 라이브러리
- 쉽고 가장 파이썬스러운 API제공한다.
---
- ## 실습해보기
> 1.데이터 로딩 및 데이터프레임 변환
```python
import sklearn.datasets import load_iris
import pandas as pd
import numpy as np

# 불꽃 데이터 세트 로딩
iris = load_iris()

# iris데이터(numpy로 가지고 있음) 변수에 저장
X_features = iris.data

# iris.target은 레이블(결정 값)데이터를 numpy로 가지고 있고 이를 변수에 저장
y_label = iris.target

# 컬럼명 설정
col_names = ['sep.len', 'sep.wid', 'pet.len', 'pet.wid']

# 데이터프레임으로 변환
iris_df = pd.DataFrame(data=X_features, columns = col_names)
```
![alt text](./%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84%20%EC%B6%9C%EB%A0%A5%EA%B0%92.png)

>2. 학습용 데이터와 테스트용 데이터 분리해보기
- 분리하는 이유?
- 학습데이터로 학습된 모델이 얼마나 뛰어난 성능을 가지는지 평가하려면 테스트 데이터 세트가 필요하기 때문에 
  - 사이킷런은 train_test_split() API 제공한다.
  - 이 API를 사용하면 학습 데이터와 테스트 데이터를 **test_size** 파라미터 값의 비율로 쉽게 분할 가능 
```python
from sklearn.model_selection import train_test_split

# test_size : 전체 데이터 중 테스트 데이터가 20%, 학습용 데이터가 80%로 데이터 분할

# random_state : 호출할때마다 같은 학습/테스트 용 데이터 세트를 생성하기 위해 주어진 난수 발생 값

x_train, x_test, y_train, y_test = train_test_split(X_features, y_label, test_size=0.2, random_state=11)
```

> 3. 의사 결정 트리를 이용해 학습, 예측 수행하기

```python
# DecisionTreeClassfier를 객체 생성
dt_clf = DecisionTreeClassfier(random_state=11)

# 학습수행
dt_clf.fit(x_train, y_train)
```
- DecisionClassfier객체는 학습데이터 기반으로 학습이 완료된 상태
- 예측은 반드시 학습데이터가 아닌 다른데이터로 이용해야하며, 일반적으로 테스트 데이터 세트를 이용한다.

```python
# 학습이 완료된 DecisionTreeClassfier 객체에서 테스트 데이터 세트로 예측 수행
pred = dt_clf.predict(x_test)
```

```python
# 예측값
pred
```
![alt text](./%EC%98%88%EC%B8%A1%EA%B0%92.png)

```python
# 실제값
y_test
```
![alt text](./%EC%8B%A4%EC%A0%9C%EA%B0%92.png)

>4. 정확도 측정하기
- 사이킷런은 정확도 측정을 위해 accuracy_score()함수를 활용한다.

```python
from sklearn.metrics import accuracy_score as acc_sc
print('예측 정확도: {0}'.format(acc_sc(y_test,pred)))
```
![alt text](./%EC%98%88%EC%B8%A1%EC%A0%95%ED%99%95%EB%8F%84.png)
