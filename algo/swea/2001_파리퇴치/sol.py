import  sys
sys.stdin = open('input.txt')

T = int(input())


def hit():
    for tc in range(1, T + 1):
        n, m = map(int, input().split())

        matrix = []
        for _ in range(n):
            matrix.append(
                list(map(int, input().split()))
            )


    # 전체 크기 N X N 크기
    for row in range(n - m + 1):  # range(4) -> 0,1,2,3
        for col in range(n - m + 1):  # range(4) -> 0,1,2,3 / 시작 : [row = 0, col = 0], [row = 0, col = 1] 쭊죽쭉
            sum_list = []
            # a = sum_list.append(matrix[row][col])

            # M X M 크기의 총합
            for x in range(m): # m이 2일때 -> x = 0 1 / m이 3일때에는 -> x = 0,1,2
                for y in range(m):
                    sum = matrix[x:m-1][y:m-1]
                    a = sum_list.append(sum)
            # sum = matrix[row][col] + matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1]
                    return sum_list



    hit()







