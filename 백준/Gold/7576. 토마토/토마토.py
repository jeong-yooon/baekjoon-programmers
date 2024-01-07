import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = []
for i in range(n):
    box.append(list(map(int, input().split())))

queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 방향변수
res = 0 # 결과 변수

# n과 m을 사용하는걸 헷갈리지 말아야 함!
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

# bfs 함수. 한번 들어가면 다 돌고 나오니까 재귀 할 필요 없음
def bfs():
    while queue:
        # 처음 토마토 좌표 x, y에 꺼내고
        x, y = queue.popleft()
        # 처음 토마토 사분면의 익힐 토마토들을 찾아본다.
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            # 해당 좌표가 좌표 크기를 넘어가면 안되고, 그 좌표에 토마토가 익지 않은채로 있어야 함(0).
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                # 익히고 1을 더해주면서 횟수를 세어주기
                # 여기서 나온 제일 큰 값이 정답이 될 것임
                box[nx][ny] = box[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in box:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    res = max(res, max(i))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(res - 1)