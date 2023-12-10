from collections import deque

n, r, e, ex, ey = map(int, input().split())
tops = {tuple(map(int, input().split())) for _ in range(n)}
answer = 0

def bfs(x, y):
    global answer, tops

    q = deque([(x, y, 0)])

    while q:
        x, y, depth = q.popleft()
        if depth:
            answer += e / (2 ** (depth - 1))

        # 거리 내에 있는 탑 찾기
        candidate = []
        for top in tops:
            if (x - top[0]) ** 2 + (y - top[1]) ** 2 <= r ** 2:
                candidate.append(top)
        # 탑 추가
        for top in candidate:
            q.append((top[0], top[1], depth + 1))
        # 탑 제거
        tops -= set(candidate)

bfs(ex, ey)
print(round(answer, 2)) if int(answer) != answer else print(f'{answer}.0')