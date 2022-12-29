import sys
sys.stdin = open('input.txt')


# # 입력값에서 스위치 개수, 스위치 번호, 케이스 각각 출력
# T = int(input())  #T=1 출력값 : 8
switch_cnt = int(input())  #T=1 출력값 : 8
switch_num = list(map(int, input().split())) #T=2 -> [0,1,0,1,0,0,0,1]
switch_tc = int(input()) #T=3 -> 2
gencase1 = list(map(int, input().split())) # T = 4 ->[1,3]
gencase2 = list(map(int, input().split())) #  T = 5 -> [2,3]
genlist = [gencase1, gencase2]

change_sn_list = []
def adj_man():
    for i in range(switch_cnt):
        if switch_num[i] == 0:
            switch_num = 1
            change_sn_list.append(switch_num)
        else:
            switch_num = 0
            change_sn_list.append(switch_num)

def adj_woman():
    for i in range(switch_cnt):


# 스위치번호는 스위치 상태 인덱스값 + 1
for n in range(1, switch_cnt+1):
    # 남학생일때
    if gencase1[0] == 1 :
        if switch_num[n-1] % gencase1[1] == 0: # 배수판별
            adj_man() # 스위치 상태값 바꾼다.
        else :
            pass

    #여학생일때
    if gencase2[0] == 2 :
        while switch_num[n-1] == switch_num[n+1]:









