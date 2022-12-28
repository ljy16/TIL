import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]




