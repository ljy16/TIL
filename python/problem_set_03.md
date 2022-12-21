1. 종합소득세 계산하기

|과세표준|세율|산출세액 계산방법
|-|-|-|
|1200만원 이하|6%|과세표준액 x 6%|


2. 카쉐어링 요금 계산하기

3. 문자열 탐색
> 문자열 요소로만 이루어진 리스트를 넣었을 때, 문자열 길이가 2 이상이고 주어진 문자열의 첫번째와 마지막 문자가 같은 문자열의 수를 세는 함수 작성
    ex) strart_end(['level', 'asdwe', 's', 'abca', 'gsdfag']) -> 3

```
    def start_end(numbers):
        cnt = 0
        for num in numbers :
            if num > 2 and len(num[0]) == len(num[-1])
            cnt += 1
        return cnt
```

틀린 부분
```
    문자열 길이가 2 이상이니까 1보다 크게 조건 수정해야함.
    길이가 같은게 아님 len(num[0]) -> num[0]
    if 문 마지막 콜론 빠짐

    수정본
    def start_end(numbers):
        cnt = 0
        for num in numbers :
            if num > 1 and num[0] == num[-1]:
                cnt += 1
        return cnt
```
1. 이상한 덧셈
> 숫자들을 받아서 양의 정수의 합을 구하는 함수 작성
    ex) positive_sum(1,3,-1, 2) -> 6
        positive_sum(-1, -2, -3, -4) -> 0

```
    def positive_sum(*numbers):
        total = 0
        for num in numbers:
            if num > 0 :
                total += num
        return total
```

5. Collatz 추측
> 1. 입력된 수가 짝수면 2로 나눈다.
> 2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다.
> 3. 결과로 나온 수에 같은 작업을 1이 될때까지 반복한다.
> 4. 단, 작업을 500번 반복해도 1이 되지 않는다면 -1을 반환한다.
    ex) collatz(6) -> 8
        collatz(16) -> 4
        collatz(27) -> 111
        collatz(621354) -> -1

```
    def collatz(n) :
        cnt = 0

        while n != 1 :
            if cnt >= 500
                return -1

            if n % 2 :
                n = n // 2
                cnt += 1
            else :
                n = 3*n + 1
                cnt += 1
            return 
         


```

6. 솔로 천국 만들기