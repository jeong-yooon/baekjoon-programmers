from collections import deque

# 방향 변수 지정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b)) # 큐에 값이 1인 좌표 저장
    graph[a][b] = 0 # 0으로 변경하여 방문표시
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 해당 좌표 기준으로 상하좌우 비교
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1: # 상하좌우 중에 집이 존재하면
                graph[nx][ny] = 0 # 방문표시해주고
                queue.append((nx, ny)) # 해당 좌표를 큐에 저장
                count += 1 # 집의 개수 +1 카운팅해준다.
    return count


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

cnt = [] # 각 단지의 집 수를 셀 변수
for i in range(n):
    for j in range(n): # 2차원배열을 돌며
        if graph[i][j] == 1: # 집이 있을 때
            cnt.append(bfs(graph, i, j)) # bfs 탐색 진행하여 각 단지 집수 카운팅

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])