# 0209
### 1. 층화 kold(Stratified KFold)란?
- 불균형한 분포도를 가진 레이블(결정 클래스) 데이터 집합을 위한 K폴드 방식이다.
- 분포도를 가진 레이블 데이터 집합은 특정 레이블 값이 특이하게 많거나 매우 적어서 값의 분포가 한쪽으로 치우치는 것을 말한다.
 
## 2. 코드 진행
```python
# 넘파이 판다스
import numpy as np
import pandas as pd

# iris 데이터셋
from sklearn.datasets import load_iris

# 데이터 분할
from sklearn.model_selection import train_test_split

# kfold 호출
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold

# 필요 알고리즘
from sklearn.tree import DecisionTreeClassifier

# 평가지표
from sklearn.metrics import accuracy_score as acc_sc

# 데이터 정의
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['label'] = iris.target

# 층화 K-Fold 적용
skf = StratifiedKFold(n_split=3)

for train_index, val_index in skf.split(iris_df, iris_df['label']):
    label_train = iris_df['label'].iloc[train_index]
    label_val = iris_df['label'].iloc[val_index]

    print('학습 레이블의 데이터 분포:\n', label_train.value_counts())
    print('검증 레이블의 데이터 분포:\n', label_val.value_counts())
```
![alt text](./%EC%B8%B5%ED%99%94%EA%B2%80%EC%A6%9D.png)

### 2. StandardScaler
### 3. MinMaxScaler