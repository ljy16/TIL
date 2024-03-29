# 0125~0126 정리
## (1) Data Work Flow
    데이터 수집       데이터 전처리          모델링 - 규칙을 찾는다.      과정평가/결과해석/시각화
    데이터 선택 ---> (preprocessing)   ---> (Model)                   ---> (Evaluation/interpret/visualization)


## (2) 통계학 vs 빅데이터
    표본조사  전수조사
      질        양
    인과관계  상관관계  :: cf) 두 관계의 차이점은 한 변수가 다른 변수를 설명할 수 있느냐의 여부
    사전처리  사후관계 

cf) 인과관계를 나타내는 용어(회귀분석)

    (y변수 = 종속변수 = 반응변수 = 목표/목적변수(target) = 레이블(Label))
    매출액 = 100 * 영업사원수 + 0
                        (X변수 = 독립변수 = 설명변수 = data)

## (3) 통계학의 정의 (ch1.)
    기술통계학 - 하나의 집단의 자료의 분포, 대표값(평균 등) 등을 파악하는 통계학
    추리통계학 - 표본(모집단의 일부)을 통해 모집단의 특성(- 모평균, 모분산, 모분포)을 추리하는 통계학


        추리 ->   모수통계학 :: 모집단의 분포 ~ 정규분포 / 자료가 연속형(=비율척도)
              -> 비모수통계학 :: 그 딴 거 없음. 1) 데이터의 수가 작아도
                                                        2) 데이터가 정규분포를 따르지 않아도
                                                        3) 데이터가 비율척도가 아니더라도~


## (4) 자료의 종류와 변수의 척도 (ch2.)
    질적변수(문자)
    양적변수(숫자) - 이산형(정수)
                    연속형(실수) 

   - 변수의 척도 
      - 명목 :: 선호도, 선수의 등번호, 종교, 성별...  (x :: 사칙연산 no!)
      - 서열(순서) :: 선착순, 반 석차 (x :: 사칙연산 no!)
      - 등간(구간) :: 아날로그 시계, 아날로그 체중계 
         - 가. 덧빼만 된다.
         - 나. 절대영(0)점이라는 개념이 없다
      - 비율 :: 위의 3개 척도 빼고 다(실수형)
         -  가. 사칙연산
         -  나. 절대영(0)점이라는 개념이 있다.

   **명서등비**

## (5) 대표값 (ch3.)
    대표값 - 평균값(산술, 기하, 조화), 최빈값, 중앙값

   - 분산도 - 범위, 평균편차, 분산, 표준편차
  
   - 왜도 - 비대칭도 -> 왼쪽꼬리-음수(대표값의 위치) - 평균,최빈,중앙 vs 오른쪽꼬리-양수(대표값의 위치) 
 

# 0127
## 분산도 : 관찰값의 흩어져 있는 정도 
 - 분산도를 나타내는 방법으로 **범위**, **평균편차**, **표준편차**, **분산** 등이 있다.

>1. 범위 : 관찰값들 중에서 가장 큰 수치와 가장 작은 수치의 차
- 단점 : 극단적인 수치들 사이에서의 분포양상은 설명할 수 없음

>2. 평균편차 : 편차(관찰값 - 평균) 절대값의 평균

> 3. 분산 : 편차(관찰값-평균)의 제곱의 합을 갯수로 나눈 값

- 표본에서 평균값을 알고 있다면, 분산을 구할때, n-1을 빼줘야한다.
- 평균값을 맞춰주기 위해 마지막 값은 특정 값이 정해져있으니까 자유도가 없다.

- 모집단을 알 수 없기 때문에 표본을 설정하는 것

- 기술통계에서는 모집단/표본 구분하지 않기때문에 분산/표준편차를 구할때 분모에 n 그대로 사용              

# 0130

> **1. 조건부 확률**
    - 앞서 발생한 사건으로 인해 표본공간이 변화하게 됨
    - 어떤 사건이 일어난 또는 일어날 조건에서, 변화된 표본공간에서 어떤 사건이 일어날 확률

> **2. 베이즈 정리**
    - 실험의 사건이 다음에 일어날 사건에 아무런 영향을 주지 않을때, 두 사건을 독립사건이라고 정의

> **3. 확률변수**
    - 일정한 확률을 가지고 발생하는 사건에 수치를 부여한 것

ex) 주사위를 한 번 던질때 나오는 숫자를 확률변수라고 한다면, 표본공간은 s는

```
S = {1,2,3,4,5,6}
```
```
P(X=1) = 1/6,

P(X=2) = 1/6,

P(X=3) = 1/6,

P(X=4) = 1/6,

P(X=5) = 1/6,

P(X=6) = 1/6
```

> **4. 확률분포**
    - 어떤 확률변수가 취할 수 있는 모든 값들과 이 값들이 나타날 확률을 표시한 것

ex) 동전을 두 번 던질때 나타날 수 있는 가능한 사건들을 확률변수와 이에 대응하는 확률로 정의해보자 -> 확률분포

|확률변수(Xi) = (앞면의 수) | P(Xi) = (각 사건의 확률)|
|-|-|
|0|1/4|
|1|2/4|
|2|1/4|

> 5. **이산확률변수와 연속확률변수**
> 
![alt text](./%EC%97%B0%EC%86%8D%ED%99%95%EB%A5%A0%EB%B3%80%EC%88%98%20%EC%9D%B4%EC%82%B0%ED%99%95%EB%A5%A0%EB%B3%80%EC%88%98%20.png)

> **6. 확률함수**
    - 확률변수 : 확률시행으로 나타날 수 있는 여러 사건들에 일정한 수치를 부여한 것
    - 확률분포 : 확률변수가 취하는 값에 대해 합이 1인 확률이 어떻게 분포되어 있는지 나타낸 것

  - 확률변수가 취할 수 있는 모든 값에 대해 그 값을 가질 확률이 얼마인지 알려주는 함수

![alt text](./%ED%99%95%EB%A5%A0%EB%B0%80%EB%8F%84%ED%95%A8%EC%88%98.png)


# 0131 

> **1.베르누이 시행의 조건**
> 
    1. 각 시행의 결과는 상호배타적인 두 사건으로 구분가능하다.
    - 한 사건은 성공(S) , 다른 사건은 실패(F)
    2.각 시행에서 성공의 결과가 나타날 확률은 p = P(S), 실패가 나타날 확률은 q = P(F) = 1-p로 나타낸다. 
     즉, 성공이 나타날 확률 + 실패가 나타날 확률 -> `p+q = 1`이다.
    3. 각 시행은 서로 독립적, `한 시행의 결과는 다음 시행의 결과에 아무런 영향을 주지 못한다.`
    4. 바꿔 말하면 한 시행의 결과가 다른 시행의 결과에 영향을 주면 그것은 베르누이 시행이 아니다.

> **2. 이항확률변수와 이항확률분포**
    이항확률변수 : 어떤 시행에서의 성공확률 또는 실패확률
    이항확률분포 : 이항확률변수의 확률분포
 
- **시행횟수 n**과 **성공 확률 p**값만 알고 있다면 그 분포의 모양과 확률변수의 확률을 알 수 있다.
 
![alt text](./%EC%9D%B4%ED%99%A9%ED%99%95%EB%A5%A0%ED%95%A8%EC%88%98.png)

- 이항분포의 모양
    1. p=0.5일때, 이항실험횟수 n이 작더라도 확률분포는 항상 대칭
    2. p=0.5가 아니어도 이항실험횟수 n이 커짐에 따라 확률분포는 대칭에 가까워진다.
 
![alt text](./%EC%9D%B4%ED%95%AD%EB%B6%84%ED%8F%AC%20%EA%B8%B0%EB%8C%93%EA%B0%92%2C%EB%B6%84%EC%82%B0.png)

    - A공장의 제품은 70%만 정상품/30% 불량품
    - 임의 추출로 100개를 뽑을때, 몇개가 정상제품일지 기댓값과 분산은?
```
기댓값 : np이니까, n=100, p=0.7
        100 * 0.7 = 70개
분산 : np(1-p)이니까, 100 * 0.7 * 0.3
        = 21
```

> **3. 다항분포**
- 확률실험의  결과로 k개의 가능한 경우가 발생할 때 나타나는 분포
 
![alt text](./%EB%8B%A4%ED%95%AD%ED%99%95%EB%A5%A0%ED%95%A8%EC%88%98.png)

ex)
|구슬색깔|확률|
|-|-|
|빨강|0.40|
|파랑|0.30|
|노랑|0.20|
|주황|0.10|

복원추출의 방법으로 10개의 구슬 추출할때,
빨강구슬3개, 파랑구슬4개, 노랑구슬3개, 주황구슬은 하나도 뽑히지 않을 확률은?

p(빨강3개, 파랑4개,노랑3개,주황0개)

= 10! / 3! 4! 3! 0! * (0.40)** 3 * (0.30)** 4 * (0.20)** 3 * (0.10)** 0 = 0.017



# 0201 
## **Chapter 7. 연속확률분포**
> 1.균일분포
    - 확률변수가 취하는 모든 구간에서 각 사건의 발생확률이 일정한 것
### 2.정규분포
    - 가우스분포라고도 하며, 연속확률분포 중 가장 널리되는 분포
1) 정규분포의 확률밀도함수
![alt text](./%EC%A0%95%EA%B7%9C%EB%B6%84%ED%8F%AC%EC%9D%98%20%ED%99%95%EB%A5%A0%EB%B0%80%EB%8F%84%ED%95%A8%EC%88%98.png)

2) 표준정규분포표
![alt text](./%ED%91%9C%EC%A4%80%EC%A0%95%EA%B7%9C%EB%B6%84%ED%8F%AC.png)
- 여러 확률분포의 경우, 평균과 표준편차가 다 다르므로 이를 표준정규분포로 변환하는 작업을 **표준화**라고 한다. 
- 표준화 작업할때 사용하는 분포를 표준정규분포 또는 z-분포 라고 한다.

예시)
```
A초등학교 전교생의 IQ의 평균은 100, 표준편차 10이었다. 이 초등학교 학생들의 IQ분포가 정규분포를 이룬다고 가정할때, IQ가 100~110사이인 학생의 비율은?
```
- P(100<=X<=110) 
- 표준화 작업을 통해 P(0<=Z<=1)을 알 수 있고
- 표준정규분포표를 통해 이 값이 **0.3413**을 추출할 수 있다.


## **Chapter 8. 표본 및 표집분포**
>1.확률표본추출
    - 모집단에 속해 있는 각 구성원이 표본으로 선택될 가능성이 일정하게 되도록 하는 표본추출방법

  **1) 단순무작위추출** : 난수표 활용 및 기타방법동원

  **2) 층화추출** : 모집단의 성격에 따라 여러 집단 또는 여러 층으로 분류한 후 추출

  **3) 군집추출** : 직접 개별적인 구성원이 아닌 자연적 또는 인위적인 집단을 추출

  **4) 체계적 추출** : 모집단배열이 무작위일때 체계적 수단을 동원하여 추출

> 2.비확률표본추출
    - 확률표본추출(무작위추출)이 불가능하거나, 비경제적일 경우, 연구자가 모집단과 비슷하다고 생각되는 표본을 임의로 추출해내는 방법

**1) 편의추출** : 연구자가 가장 손쉽게 구할 수 있는 구성원을 선택하여 표본으로 삼는 표본추출

**2) 판단추출** : 전문성이 있는 연구자가 임의로 표본추출을 하는 방법

**3) 할당추출** : 모집단의 특성을 대표할 수 있게 몇 개의 하위집단을 구성한 후 각 집단별로 표본의 수를 할당하여 임의로 표본을 추출하는 방법

**4) 눈덩이추출** : 이미 참가하고 있는 사람들에게 그들이 알고 있는 사람들로부터 다른 설문조사 참가자들을 모집해 달라고 요청하는 것

# 0202 
>1.표본추출오차
   - 모집단을 대표할 수 있는 전형적인 구성요소를 표본으로 선택하지 못했기 때문에 발생하는 오류

>2.비표본추출오차
   - 표본의 특성값을 측정하는 방법이 부정확하기 때문에 발생하는 오류

카이제곱 -> 분산과 관련되있다.

## **Chapter 9 통계적 추정**
- 모집단의 특성을 추정하는 방법
  1. 점추정 : 모집단의 특성을 하나의 값으로 추정하는 방법
  2. 구간추정 : 적절한 구간을 가지고 모수를 추정하는 방법

- 점추정을 위해 추정값과 추정량을 알아보자
- 추정량의 결정기준
    - 1)불편성
    - 2)효율성
    - 3)일치성
    - 4)충분성

1) 불편성
   - 추정량의 기대값이 추정할 모수의 실제값과 일치하거나 그 값에 가까울수록 바람직한 추정량
   - 기대값과 실제값과 차이가 나면 그 추정량은 편의가 있다고 한다.
   - 이상적 추정량은 0의 편의를 가짐
   - 이때의 추정량을 불편추정량이라고 함

2) 효율성
  - 한 표본에서 계산된 추정량은 되도록 모수에 접근해야함
  - 분산이 작을수록 모수를 정확하게 추정할 수 있다.
  - 추정량 중에서 최소의 분산을 가진 추정량이 가장 효율적이다.

3)일치성
- 표본의 크기 n이 무한히 증가하면 그 표본에서 얻을 추정량이 모수에 근접하게 되는 것
- 표본으 크기가 커질수록 추정량과 모수 간의 차이는 작아지게됨

4)충분성
- 동일한 표본으로부터 얻은 추정량이 다른 추정량보다 모수에 관해 가장 많은 정보를 제공
- 어떤 추정량도 선택된 추정량보다 더 많은 정보를 제공할 수 없을때, 이 추정량을 충분성이 있는 추정량이라고 한다.

# 0203
## **Chapter 10. 가설검정**
>1.통계적 가설검정
- 표본에서 얻은 사실을 근거로, 모집단에 대한 가설이 맞는지, 틀린지 통계적으로 검정하는 분석방법

>2.가설검정의 기본용어
- 가설의 설정은 확신에 근거를 두고 이루어지는 것이 아니며, 단지 후에 경험적 또는 논리적으로 검정될 수 있는 조건, 원리, 명제를 제시하는 것에 불과하다.
#### 1.귀무가설(null hypothesis) : 검정의 대상이 되는 가설

#### 2.대립가설(alternative hypothesis) : 귀무가설이 받아들여질 수 없을때 대신 받아들여지는 가설

```
귀무가설은 직접 검정대상이 되는 가설을 말하며 H0으로 표시 - 다른 다수의 생각

대립가설은 귀무가설이 기각될 때 받아들여지는 가설로서 H1로  표시한다. - 연구자의 생각
```

#### 3.신뢰구간 : 귀무가설을 채택할 수 있도록 설정한 구간 / 신뢰구간과 유의수준은 다르다.

#### 4. 유의수준: 귀무가설이 참인데도 귀무가설을 기각할 확률

#### 5. 임계값 : 주어진 유의수준에서 귀무가설의 채택과 기각에 관련된 의사결정을 할 때, 그 기준이 되는 점



>3. 양측검정
- 귀무가설이 기각되면 대립가설이 채택된다.
- 즉, 모수에 대한 가설검정을 할때 귀무가설:H0과 대립가설:H1을 나타낼 수 있다.
- 첫번째는, μ가 어떤 수와 꼭 같다는 가설이며, 다른 하나는 모수 μ가 어떤 수보다 크거나 작다고 하는 가설이다.

![alt text](./%EC%96%91%EC%B8%A1%2C%EB%8B%A8%EC%B8%A1%EA%B2%80%EC%A0%95-1.png)
- (1)과 같이 귀무가설이 𝜇 = q로, 대립가설이 𝜇 ≠ q로 설정되어 있는 경우를 생각해보면, 표본을 뽑아서 그 표본에서 얻은 통계량이 𝜇 = q과 매우 근접하여 있으면 귀무가설을 채택할 것이지만, 그렇지 않고 통게량이 q보다 매우 크거나, q보다 현저히 작을 때에는 귀무가설을 채택할 수 없게 된다.
- 따라서 귀무가설을 기각하는 영역은 확률부높의 양측에 있게 된다. 
- 이때, 가설검정에서 기각영역이 양쪽에 있는 것을 양측검정이라고 한다.
- 또한, 유의수준 α도 양쪽 극단으로 갈리게 되어 한쪽의 면적이 α/2가 된다.
![alt text](./%EC%96%91%EC%B8%A1%EA%B2%80%EC%A0%95%20%EB%8B%A8%EC%B8%A1%EA%B2%80%EC%A0%95%20%EC%9D%B4%EB%AF%B8%EC%A7%80.png)

>4. 단측검정
- (2)와 같이 귀무가설을 𝜇 ≥ q라 하고 대립가설을 𝜇 < q라고 설정하여 가설검정을 할때에는 선택된 표본의 통계량이 q보다 현저히 작지 않으면 귀무가설을 채택하게 된다.
- 따라서 확률분포의 오른쪽 극단에는 귀무가설의 기각영역이 없다.
- 다만 통계량이 q보다 현저히 작으면 귀무가설을 기각하게 된다.
- 가설검정에서 기각영역이 어느 한쪽에만 있게 되는 경우를 단측검정이라고 한다.

---
문제1
```
어느 초등학교의 5학년과 6학년이 같은 문제를 가지고 시험을 보았다. 
6학년의 평균 성적은 80점이었고, 5학년의 평균성적은 60점이었다.
두 분포가 정규분포라 가정하고 한 학생의 점수가 70점이라면, 해당 학생은 5학년일까? 6학년일까?
```

풀이

- H0 : 그 학생은 6학년이다.
- H1 : 그 학생은 5학년이다.

어떤 점수에서부터 6학년으로 보아야 하는가?

    - 70점 이상을 6학년으로 보게 된다면, 6학년 중에서 5학년으로 간주될 학생은 a1만큼이며, 비율은 0.1587
    - 하지만 15% 오류는 매우 크기 때문에 이러한 오류를 줄이기 위해 α를 5%로 한다면, z값은 -1.64가 되며 이에 대응하는 X는 63.6이 된다.

![alt text](./%EA%B7%80%EB%AC%B4%EA%B0%80%EC%84%A4%20%EC%98%88%EC%A0%9C-1.png)

    - 즉 63.6점을 기준으로 하여 그 점수 이상의 학생을 6학년이라고 한다면, 실제로는 6학년이지만 5학년으로 분류되는 오류가 발생될 확률은 약 5%가 된다.
    - 5%의 오류를 감수할 때 6학년의 분포와 현저하게 차이가 볼 수 있다는 기준값(임계치)은 63.6이 되고 이에 해당하는 Z값은 -1.64가 되는 것이다.
    - 이 임계치를 기준으로 귀무가설의 기각영역과 채택영역이 결정된다. 

---
문제2
```
EX 통조림회사에서 수출용 참치 통조림을 생산하는데, 통조림의 무게가 16온스이고, 무게의 분포가 정규분포라 한다.
그러나 해외에서는 통조림 무게가 16온스가 아니라고 의심한다. 
회사측에서는 이를 확인하기 위해 25개의 통조림을 표본으로 뽑아 평균을 조사하였더니 표본의 평균이 15.5온스였다. 
모집단의 표준편차는 1.5온스라는 것을 과거의 경험으로 알고 있다고 할때, 𝛼=0.05로 하면, 위의 결과로부터 이 회사의 통조림 무게가 16온스라고 말할 수 있을까?
```

풀이

무게가(모집단이) 정규분포이므로, n=25일때 표집분포도 정규분포이다.
표본평균의 평균은 모집단의 평균과 같으므로 16온스이고, 표본표준편차 = 모표준편차 / sqrt 25 = 1.5/5 = 0.3이다.
![alt text](./%EA%B0%80%EC%84%A4%EA%B2%80%EC%A0%95%20%EC%98%88%EC%8B%9C-1.png)

>1. 양측검정 풀이
1) 𝐻0 : μ = 16<br/>
    𝐻1 : μ ≠ 16

2) 𝛼 = 0.05
3) 채택영역 : -1.96 ≤ Z ≤ 1.96<br/> 
    기각영역 : Z > 1.96 또는 Z < -1.96

4) 표본평균 = 15.5에 해당하는 Z값을 계산하면,<br/>
Z = 표본평균 - μ / 표본표준편차 = 15.5-16/0.3 = -1.67 <br/>
Z = -1.67은 채택영역 안에 있으므로 H0을 기각할 수 없다.
5) 𝛼=0.05 수준에서 통조림의 무게가 16온스라는 기존의 주장을 기각할 수 없다.
![alt text](./%ED%86%B5%EC%A1%B0%EB%A6%BC-%EC%96%91%EC%B8%A1%EA%B2%80%EC%A0%95.png)

>2. 단측검정 풀이
1) 𝐻0 : μ = 16<br/>
   𝐻1 : μ < 16

2) 𝛼 = 0.05
3) 채택영역 : Z ≥ -1.64<br/>
   기각영역 : Z < -1.64
4) 표본평균 = 15.5에 해당하는 Z값을 계산하면,
Z =  표본평균 - μ / 표본표준편차 = 15.5-16/0.3 = -1.67
5) 양측검정의 결과와는 달리 내용량이 16온스라고 고객들한테 주장할 수 없다.

# 0207
## **Chapter 14 상관분석과 회귀분석의 기초**
두 변수가 연속형일때 단순회귀분석/상관분석 

>1. 통계분석의 목적<br/>
- 차이에 집중 : z검정, t검정<br/>
- 관계에 집중 : 상관분석

>2. 상관분석
- x값과 y값, 두 변수 간 상관관계를 탐색한다.
- 연속적인 두 변수 간의 선형관계 탐식 및 확인하는 방법
- 회귀분석을 하기 위해서는 상관분석을 먼저 해야 한다.
- 상관분석이 선형인지 비선형인지에 따라 선형회귀분석, 비선형회귀분석으로 나뉜다.
- 두 변수 간의 관계의 강도, 즉 얼마나 밀접하게 관련되어 있는지를 분석하는 것이다.
- **두 변수 간의 관련성만을 의미할 뿐 인과관계를 밝히진 못한다.**

>2.1 상관계수
- 두 변수의 **관련성의 정도**를 의미한다.(-1과 1 사이의 값으로 나타냄)
- 두 변수의 상관관계가 존재하지 않을 경우에는 상관계수가 0이다.
- 상관관계가 높다고 인과관계가 있다고 할 수 없다.
- 상관계수에는 피어슨 상관계수와 스피어만 상관계수가 있다.
- 피어슨 상관계수는 두 변수 간의 선형적인 크기만 측정 가능하고,
- 스피어만 상관계수는 두 변수간의 비선형적인 관계도 나타낼 수 있다.
- 귀무가설은 상관관계가 0이다
- 대립가설은 상관관계가 0이 아니다.

>2.1.1 피어슨 상관계수
- 모집단에 분포가 정규분포에 가까우면 사용
- 두 변수가 양적자료(등간척도, 비율척도)인 경우에 사용한다.
- 두 변수간의 **선형적인 크기만 측정** 가능
- 대부분 많이 사용한다.
- x,y의 공분산을 x,y의 표준편차곱으로 나눈 값

>2.1.2 스피어만 상관계수
- 모집단이 비정규분포를 나타낼 때 사용한다.
- 두 변수가 하나라도 서열척도인 경우에 사용한다.
- 두 변수 간의 **비선형적인 관계**를 나타낼 수 있다.
- 연속형 외에 이산형도 가능하다.
- 원시 데이터가 아니라 각 변수에 대해 순위를 매긴 값을 기반으로 한다.
- 두 변수 안의 순위가 완전 일치하면 1, 완전 반대이면 -1

>2.2 공분산
- Covariance, 2개의 확률변수의 선형관계를 나타내는 값
- 하나의 변수가 상승하는 경향을 보일 때 다른 값도 상승하는 선형 상관성이 있다면 양의 공분산을 갖음
- 공분산이 0이면 서로 독립이고, 관측값들이 4면에 균일하게 분포되어 있다고 추정할 수 있다.
![alt text](./%EA%B3%B5%EB%B6%84%EC%82%B0.png)
---
>3. 회귀분석
- 변수와 변수 사이의 관계를 알아보기 위한 통계적 분석 방법
- 독립변수의 값에 의해 종속변수의 값을 예측하기 위함
- 일반 선형회귀는 종속변수가 연속형 변수일 때 가능하다.
- 이산형(범주형) - 명목,서열척도
- 연속형 - 구간, 비율척도

>3.1용어정리
- 독립변수 : 다른 변수에 영향을 받지 않고, 독립적으로 변화하는 수 , 설명변수라고도 한다.
  - 입력 값이나 원인을 나타내는 변수, y=f(x)에서 x에 해당하는 것

- 종속변수 : 독립변수의 영향을 받아 값이 변화하는 수, 분석의 대상이 되는 변수
    - 결과물이나 효과를 나타내는 변수, y=f(x)에서 y에 해당하는 것

- 잔차(오차항) : 계산에 의해 얻어진 이론 값과 실체 관측이나 측정에 의해 얻어진 값의 차이
    - 오차(Error) - 모집단
    - 잔차(Residual) - 표본집단

>3.2 회귀분석의 종류
1. 단순선형회귀분석 : 한 독립변수와 한 종속변수의 관계
- 두 변수 간의 인과관계를 조사하는 것
2. 다중선형회귀분석 : 여러 독립변수와 한 종속변수의 관계
- 두개 이상의 독립변수들과 하나의 종속변수 간의 관계를 분석하는 기법으로 단순회귀분석을 확장한 것
![alt text](./%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D%20%EC%A2%85%EB%A5%98.png)

>3.2.1 단순선형회귀분석
![alt text](./%EB%8B%A8%EC%88%9C%EC%84%A0%ED%98%95%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D.png)
- 𝜷1 = 회귀계수

>3.2.2 다중선형회귀분석
![alt text](./%EB%8B%A4%EC%A4%91%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D.png)

>3.3 선형회귀분석의 가정
1. 선형성 : X(독립변수)와 Y(종속변수)의 관계가 선형이다.(가장 중요한 가정)
![alt text](./%EC%84%A0%ED%98%95%EC%84%B1.png) 
1. 정규성 : Q-Q plot이 직선으로 표현되어 잔차(오차의 분포)가 정규분포를 따른다.
    - 히스토그램,Q-Q plot, Kolomogolov-Smirnov 검정, Shaprio-Wilk test 등을 활용하여 정규성 확인
![alt text](./%EC%A0%95%EA%B7%9C%EC%84%B1.png) 
1. 독립성 : 입력변수와 오차는 관련이 없다.
    - 더빈왓슨 통계량이 2에 가까울수록 오차항의 자기상관이 없다.(= 오차항이 독립적)
2. 등분산성 : X(독립변수)에 대한 잔차의 산점도를 그렸을 때 잔차들이 일정해야 한다.
![alt text](./%EB%93%B1%EB%B6%84%EC%82%B0%EC%84%B1%20%EB%A7%8C%EC%A0%81.png)
![alt text](./%EB%93%B1%EB%B6%84%EC%82%B0%EC%84%B1%20%EB%B6%88%EC%B6%A9%EB%B6%84.png) 
1. 비상관성 : 관측치들의 잔차들끼리 상관성이 없어야 한다.

>3.4 최소제곱법
- y=f(x)의 측정값(관찰값) yi와 함수값(예측값) f(xi)의 차이를 제곱한 것의 합이 최소가 되도록 y=f(x)를 구하는 것
- y=aX+b 일 때 잔차를 제곱한 것의 합이 최소가 되도록 하는 상수 a,b를 찾는 것
- 즉, (측정값 – 함수값)제곱의 합이 최소가 되는 직선의 그래프를 찾는 것
- 큰 폭의 잔차에 대해 보다 더 큰 가중치를 부여하여, 독립변수 값이 동일한 평균치를 갖는 경우 가능한 한 변동 폭이 적은 표본회귀선을 도출하기 위한 것

>3.5 회귀모형 해석(평가방법)
1. 표본 회귀성의 유의성 검정 : 두 변수 사이에 선형관계가 성립하는지 검정하는 것으로, 회귀식의 기울기 계수  𝜷1 =0 일때 귀무가설, 𝜷1≠0일때 대립가설로 설정한다.
2. 회귀모형 해석
    1. 모형이 통계적으로 유의미한가?<br/>
    -> F통계량, 유의확률(p-value)로 확인
    2. 회귀계수들이 유의미한가?<br/>
    -> 회귀계수의 t값, 유의확률(p-value)로 확인
    3. 모형이 얼마나 설명력을 갖는가?<br/>
    -> 결정계수(R제곱)확인
    4. 모형이 데이터를 잘 적합하고 있는가?<br/>
    -> 잔차 통계량 확인, 회귀진단 진행(선형성~정상성)
3. F 통계량
- 모델의 통계적 유의성을 검정하기 위한 검정 통계량(분산 분석)
- F 통계량이 클수록 회귀모형은 통계적으로 유의하다. p-value < 0.05일 때 유의함
4. 결정계수(R제곱 = SSR/SST)
- 회귀식의 적합도를 재는 척도
- 결정계수는 0~1 사이의 범위를 갖는다.
- 결정계수가 커질수록 회귀방정식의 설명력이 높아진다.
![alt text](./%EA%B2%B0%EC%A0%95%EA%B3%84%EC%88%98.png) 

>3.6 다중 공선성
- 모형의 일부 설명변수(=예측변수)가 다른 설명변수와 상관되어 있을 때 발생하는 조건
- 중대한 다중공선성은 회귀계수의 분산을 증가시켜 불안정하고 해석하기 어렵게 만들기 때문에 문제가 된다.

>3.7 설명 변수(독립 변수) 선택 방법
1. 모든 가능한 조합 독립변수들의 조합에 대한 회귀모형을 고려해, AIC, BIC의 기준으로 가장 적합한 회귀 모형 선택
    - AIC,BIC : 최소제곱법의 R제곱과 비슷한 역할을 하며, 적합성을 측정해주는 지표로, R제곱은 큰 값이 좋지만, AIC, BIC는 작은 값이 좋음

2. 전진선택법
    - 절편만 있는 모델에서 출발해 기준 통계치를 가장 많이 개선시키는 변수를 차례로 추가하는 방법