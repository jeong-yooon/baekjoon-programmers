import sys

input = sys.stdin.readline


def bf(start):
    # 시작 도시의 최단 시간을 0으로 초기화
    dist[start] = 0

    # 간선을 탐색하기 위한 for문. 간선은 n-1개여야 하므로 n번 반복
    for i in range(1, n + 1):
        # 각 도시에 대해 최단 거리 갱신을 위한 for문
        for a in range(1, n + 1):
            # 현재 도시에서 이동 가능한 도시와 걸리는 시간에 대해 반복
            for next, time in graph[a]:
                # 현재까지 계산된 최단 시간이 무한대가 아니고, 다음 도시로 가는 최단 시간이 현재까지의 최단 시간보다 작으면
                if dist[a] != float('inf') and dist[next] > dist[a] + time:
                    # 최단 시간 갱신
                    dist[next] = dist[a] + time
                    # n-1번 이후에도 값이 갱신되면 음수 사이클 존재
                    if i == n:
                        return True  # 음수 사이클 존재
    return False


# 도시 개수, 버스 개수 입력
n, m = map(int, input().split())
# 각 도시에서 이동 가능한 도시와 걸리는 시간을 저장하는 그래프 초기화
graph = [[] for i in range(n + 1)]
# 각 도시로 가는 최단 시간을 저장하는 리스트 초기화
dist = [float('inf') for i in range(n + 1)]

# 버스 노선 정보 입력 및 그래프 업데이트
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

# 음수 사이클 여부 확인
negative_cycle = bf(1)

# 음수 사이클이 존재하면 -1 출력
if negative_cycle:
    print(-1)
else:
    # 각 도시로 가는 최단 시간 출력
    for i in range(2, n + 1):
        # 도시로 가는 경로가 없으면 -1 출력, 그렇지 않으면 해당 도시로 가는 최단 시간 출력
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])
