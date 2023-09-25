import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip())) for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 2  # 방문한 곳 2로 초기화

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < m and 0 <= ny < n: # nx, ny가 내부 좌표일때
                if graph[nx][ny] == 0:  # 0은 흰색이므로 침투가능
                    graph[nx][ny] = 2 # 방문좌표를 방문표시해줌
                    q.append((nx, ny)) # 해당좌표 저장


for i in range(len(graph[0])):  # 위쪽 모든 좌표에서 침투시작
    bfs(0, i)

if graph[m - 1].count(2):  # 그래프 마지막 줄에 2가 있으면 침투 성공
    print("YES")
else:
    print("NO")