import sys
sys.stdin = open('input.txt')

T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(str, input()))
#
#     count_list = {}
#     for n in numbers:
#         if n in count_list:
#             count_list[n] += 1
#         else:
#             count_list[n] = 1
#     print(f'#{tc} {}{}')


for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))

    count_list = [0] * 10 * 정상출력
    for idx in count_list:
        if idx == count_list[idx]:
            count_list[idx] += 1
        else:
            pass

