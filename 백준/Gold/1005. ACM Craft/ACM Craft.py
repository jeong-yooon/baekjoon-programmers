import sys
from collections import deque
input = sys.stdin.readline

# 테스트 케이스의 개수 T를 입력받음
t = int(input())

# 각 테스트 케이스에 대해 반복
for _ in range(t):
    # 건물의 개수 N과 건물간의 건설순서 규칙의 총 개수 K를 입력받음
    n, k = map(int, input().rstrip().split())

    # 각 건물당 건설에 걸리는 시간 D1, D2, ..., DN을 입력받음
    d = list(map(int, input().rstrip().split()))

    # 건물간의 건설 순서를 저장할 그래프와 각 건물의 진입차수를 저장할 리스트 초기화
    graph = [[] for _ in range(n + 1)]
    inDegree = [0 for _ in range(n + 1)]

    # 각 건물의 건설시간을 저장할 리스트와 큐 초기화
    dp = [0 for _ in range(n + 1)]
    queue = deque()

    # 건설 순서를 입력받아 그래프와 진입차수를 설정
    for i in range(k):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        inDegree[b] += 1

    # 승리하기 위해 건설해야 할 건물의 번호 W를 입력받음
    w = int(input().rstrip())

    # 진입차수가 0인 건물을 큐에 추가하고 해당 건물의 건설시간을 초기화
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)
            dp[i] = d[i - 1]

    # 큐가 빌 때까지 반복
    while queue:
        tmp = queue.popleft()
        # 현재 건물과 연결된 건물들에 대해 진입차수를 감소시키고 건설시간을 업데이트
        for i in graph[tmp]:
            inDegree[i] -= 1
            dp[i] = max(dp[i], dp[tmp] + d[i - 1])

            # 만약 진입차수가 0이 되면 큐에 추가
            if inDegree[i] == 0:
                queue.append(i)

    # 승리하기 위해 건설해야 할 건물 W의 건설완료에 필요한 최소 시간 출력
    print(dp[w])
