r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input()))
    
ans = 0
alphas = set() # 집합 선언 중복값 x

# 좌표이동 변수
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4): # 상하좌우 비교
        nx = x + dx[i]
        ny = y + dy[i]
        # 배열 내에 있고 중복 알파벳이 아닐 때
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
            alphas.add(maps[nx][ny]) # 집합에 해당 좌표값 추가
            dfs(nx, ny, count+1) # 카운팅하고 dfs 탐색 진행
            alphas.remove(maps[nx][ny])
            
alphas.add(maps[0][0]) # 첫 값 추가
dfs(0, 0, 1)
print(ans)