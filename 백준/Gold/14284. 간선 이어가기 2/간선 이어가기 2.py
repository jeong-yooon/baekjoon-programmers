import heapq
import sys
INF = sys.maxsize # 무한대
input = sys.stdin.readline

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드 큐에 추가, 거리 0
    dis[start] = 0 # 시작 노드 거리 0 초기화
    while q: # 큐가 빌때까지 반복
        d, now = heapq.heappop(q) # 거리 d와 현재 노드 now를 꺼냄
        if dis[now] < d: # 현재 노드까지의 거리가 이미 더 짧다면 스킵
            continue
        for v, w in graph[now]: # 현재 노드에서 갈 수 있는 모든 인접 노드에 대해
            cost = d + w # 시작 노드에서 현재 노드까지의 거리 d에 해당 간선의 가중치 w를 더하여 다음 노드까지의 거리 cost를 계산
            if cost < dis[v]: #  거리 cost가 기존의 거리 dis[v]보다 짧으면
                dis[v] = cost # 다음 노드까지의 거리를 업데이트
                heapq.heappush(q, (cost, v)) # 큐에 다음 노드와 새로운 거리 cost를 추가

n, m = map(int, input().split()) # 정점 개수, 간선리스트의 간선 수
graph = [[] for _ in range(n+1)] # a, b, c
dis = [INF]*(n+1) # 거리 무한대로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 노드 a에서 b로 가는 간선 가중치 c를 그래프에 추가
    graph[b].append((a, c)) # 노드 b에서 a로 가는 간선 가중치 c도 그래프에 추가
s, t = map(int, input().split()) # 시작 노드 s와 목표 노드 t
dijkstra(s)
print(dis[t])