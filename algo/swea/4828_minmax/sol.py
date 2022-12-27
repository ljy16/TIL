import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_value = numbers[0]
    min_value = numbers[0]
    for idx in numbers[:] :
        if idx > max_value :
            max_value = idx
        elif idx < min_value :
            min_value = idx
        else :
            pass

    answer = max_value - min_value
    print(f'#{tc} {answer}')