# 건물 N개, 도로 M개
# i번째 도로 = 서로 다른 두 건물 Ai 번과 Bi 번 사이를 1 시간에 양방향으로 이동할 수 있는 도로
# 2개의 건물을 골라 치킨집 오픈
# 모든 거물에서의 접근성의 합 최소화
# 접근성 = 가장 가까운 치킨집까지 왕복하는 최단 시간
# "모든 건물에서 가장 가까운 치킨집까지 왕복하는 최단 시간의 총합"을 최소화할 수 있는 건물 2개 선택

import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 건물 n, 도로 m
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)] # 그래프 초기화

# 도로 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1 # a -> b 가는 도로 존재
    graph[b][a] = 1 # b -> a 가는 도로 존재

# 자기 자신은 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0 # 모든 건물로부터 자기 자신으로 가는 거리는 0으로 초기화

# 1. 모든 정점에서 모든 정점으로 가는  최소 거리 구하기
for k in range(1, n + 1): # 모든 건물 쌍 사이의 최단 거리 계산
    for a in range(1, n + 1):   # 출발 노드
        for b in range(1, n + 1):   # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # 최단 거리 갱신

# 2. 2개의 건물을 선택하여(예상 치킨집) 모든 집을 방문해서 걸리는 거리를 측정
min_sum = INF
result = list()
for i in range(1, n):  # 건물 2개를 뽑는다.
    for j in range(2, n + 1):
        sum_ = 0 # 모든 건물로부터의 접근성 합
        for k in range(1, n + 1):  # 모든 집을 방문하면서 거리를 측정
            sum_ += min(graph[k][i], graph[k][j]) * 2  # k -> i, k -> j 중에 짧은 거리 합치기
        if sum_ < min_sum:
            min_sum = sum_
            result = [i, j, sum_]

print(*result)