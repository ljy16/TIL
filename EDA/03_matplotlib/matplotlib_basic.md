# 0131 정리
1. matplotlib 라이브러리 임포트
```
import matplotlib.pyplot as plt
```

2. x값, y값 넣어주기
```
plt.plot([1,2,3,4],[15,16,48,60])
plt.show()
```
- plt.show()가 없어도 출력되긴 하지만 마지막에 꼭 쓰는 것을 습관화하자!

3. 축 레이블 설정
```
import numpy as np

plt.plot([1,2,3,4],[1,4,9,16])
plt.xlabel('X축')
plt.ylabel('Y축')
plt.show()
```
![alt text](./x%2Cy%EC%B6%95%20%EC%84%A4%EC%A0%95.png)

4. 여백 지정하기
```
import matplotlib.pyplot as plt

plt.plot([1,2,3,4],[2,3,5,10])
plt.xlabel('X-축', labelpad=15, loc='right)
plt.ylabel('Y-축', labelpad=20, loc='top')
```
![alt text](./x%2Cy%EC%B6%95%20%EC%97%AC%EB%B0%B1%EC%A7%80%EC%A0%95.png)
