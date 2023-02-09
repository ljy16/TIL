# 0208
### 1. 교차검증
1. 교차검증의 정의
- 모델 학습 시 데이터를 훈련용(train)과 검증용(test)로 나눈다.
- 고정된 test set을 통해 모델의 성능을 검증하고 수정하는 과정을 반복하다 보면 내가 만든 모델은 test set에만 잘 동작하는 모델이 되버리고 만다.
- 이 test set에 과적합(overfitting)이 발생하게 되므로 다른 데이터를 가져와 예측수행시 결과가 엉망으로 나온다.
- 이것을 해결하기 위한 것이 교차검증(데이터의 크기에 대한 문제, 모델선택에 대한 문제를 해결하기 위해)
- train set을 train set + validation set으로 분리한 뒤, validation set을 사용해 검증하는 방식이다.
- 과적합 : 모델이 학습 데이터에만 과도하게 최적화되어, 실제 예측을 다른 데이터로 수행할 경우에는 예측 성능이 과도하게 떨어지는 것

2.K Fold 교차 검증
```python
# 데이터 로드
from sklearn.datasets import load_iris

# 모델 분할
from sklearn.model selection import KFold
from sklearn.model_selection import train_test_split

# 알고리즘
from sklearn.tree import DecisionTreeClassifier

# 평가지표
from sklearn.metrics import accuracy_score as acc_sc

# 넘파이 판다스
import numpy as np
import pandas as pd

# 데이터 정의
iris = load_iris()
features = iris.data # x값
label = iris.target # y값

# 알고리즘 객체화
dt_clf = DecisionTreeClassifer(random_state=156)

# 5개의 폴드 세트로 분리하는 KFold 객체 생성
kfold = KFold(n_splits=5)

# 폴드 세트별 정확도를 담을 리스트 객체 생성
cv_accuracy = []

n_iter = 0

# KFold의 객체의 split()를 호출하면 폴드 별 학습용,검증용 테스트의 로우 인덱스를 array로 반환
for train_index, test_index in kfold.split(features): #features는 iris.data

# kfold.split()으로 반환된 인덱스를 이용해 학습용,검증용 테스트 데이터 추출
X_train, X_val = features[train_index], features[test_index]
y_train, y_val = label[train_index], label[test_index]

# 학습 및 예측
dt_clf.fit(X_train, y_train)
pred = dt_clf.predict(X_test)
n_iter += 1

# 반복 시마다 정확도 측정
accuracy = np.round(accurarcy_score(y_test,pred),4)
train_size = X_train.shape[0]
test_size = X_test.shape[0]
print('\n #{0} 교차 검증 정확도:{1}, 학습 데이터 크기 : {2}, 검증 데이터 크기 : {3}'.format(n_iter, accuracy, train_size, test_size))
print('#{0} 검증 세트 인덱스 : {1}'.format(n_iter, X_val))
cv_accuracy.append(accuracy)

# 개별 iteration별 정확도를 합하여 평균 정확도 계산
print('\n ## 평균 검증 정확도:', np.mean(cv_accuracy))
```

![alt text](./%EA%B5%90%EC%B0%A8%EA%B2%80%EC%A6%9D.png)

- 5차 검증 결과 평균 검증 정확도는 0.9다
- 교차 검증시마다 검증 세트의 인덱스가 달라짐을 알 수 있다.
- 학습 데이터 세트의 인덱스는 수가 많아서 출력하지 않았지만 검증 세트의 인덱스를 보면 교차 검증 시마다 split()함수가 어떻게 인덱스를 할당하는지 알 수 있다.
- 각각 30개의 검증 세트 인덱스를 생성했고, 이를 기반으로 검증세트를 추출하게 된다.