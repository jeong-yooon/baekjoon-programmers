from collections import deque

n, m = map(int, input().split())
arr = []

shark = deque() # 상어 위치 좌표
for i in range(n):
    temp = list(map(int, input().split()))
    for t in range(m):
        if temp[t] == 1: # 해당 좌표에 상어가 있다면
            shark.append((i,t)) # 큐에 좌표를 저장
    arr.append(temp)

mx = [-1, -1, -1, 0, 1, 0, 1, 1] # 대각선 방향까지 합쳐 총 8개
my = [-1, 0, 1, 1, 1, -1, 0, -1]


def bfs():
    while shark: # 상어가 있는 좌표를 돈다.
        x, y = shark.popleft() # x,y 는 상어가 있는 좌표이다.
        for k in range(8):
            dx = x + mx[k] # 이동 x 좌표
            dy = y + my[k] # 이동 y 좌표
            if 0 <= dx < n and 0 <= dy < m: # 이동 좌표가 공간크기 내에 있고
                if arr[dx][dy] == 0: # 해당 칸에 상어가 없다면
                    shark.append((dx,dy)) # 큐에 좌표 저장
                    arr[dx][dy] = arr[x][y] + 1 # 이동 좌표의 값 = 원래 좌표 +1
    return


bfs()
safe_dist = 0
# 전체 좌표를 돌며 탐색
for i in range(n):
    for j in range(m):
        safe_dist = max(safe_dist, arr[i][j]) # 최댓값 탐색

print(safe_dist - 1) # 원래 좌표값의 1은 빼준다.