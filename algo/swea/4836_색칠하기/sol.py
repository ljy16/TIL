import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    matrix = [[0 for _ in range(10)] for _ in range(10) ] # 뒤에 있는 횟수만큼 앞에를 채운다 / 10*10 0으로 채워진 매트릭스 코드

    # 색칠 시작
    for _ in range(N): # tc 1 and N : 2
        a = list(map(int, input().split())) #[2,2,4,4,1] 이렇게 들어오겠지?
        cnt = 0
        for row in range(10):
            for column in range(10):
                if matrix[row][column] == a[0] :
                    cnt += 1



    print(f'#{tc} {cnt}')