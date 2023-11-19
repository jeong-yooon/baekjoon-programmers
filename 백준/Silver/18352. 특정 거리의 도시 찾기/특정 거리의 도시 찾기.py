from collections import deque
import sys
input = sys.stdin.readline

# 입력 및 초기화
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]  # 각 노드에서 이동 가능한 노드들의 리스트를 저장하는 인접 리스트
distance = [0] * (n+1)  # 시작 노드로부터의 거리를 저장하는 리스트
visited = [False] * (n+1)  # 각 노드의 방문 여부를 나타내는 리스트

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# BFS 함수
def bfs(start):
    answer = []  # 거리가 k인 노드들을 저장할 리스트
    q = deque([start])  # BFS를 위한 큐 초기화
    visited[start] = True
    distance[start] = 0

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

# BFS 함수 호출
bfs(x)
