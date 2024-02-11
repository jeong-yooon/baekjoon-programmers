import sys
import heapq

input = sys.stdin.readline

# 입력: 논의 수 N
N = int(input())
node_list = []  # (우물 파는 비용, 논 번호)를 저장하는 힙
pay_list = []   # 각 논의 우물 파는 비용을 저장하는 리스트

# 각 논의 우물 파는 비용을 입력받아 힙과 리스트에 저장
for i in range(N):
    pay = int(input())
    heapq.heappush(node_list, (pay, i))
    pay_list.append(pay)

# 각 논들 사이의 물을 끌어오는 비용을 2차원 리스트로 입력받음
connect_list = [list(map(int, input().split())) for _ in range(N)]

result = 0  # 결과 변수 초기화
visited = [False] * N  # 방문 여부를 저장하는 리스트 초기화

# 우선순위 큐(node_list)가 빌 때까지 반복
while node_list:
    pay, node = heapq.heappop(node_list)
    # 이미 방문한 논이면 스킵
    if visited[node]:
        continue
    visited[node] = True
    result += pay  # 결과에 현재 논의 우물 파는 비용 추가

    # 현재 논과 연결된 모든 논에 대해
    for next_node in range(N):
        if next_node != node:
            # 만약 더 저렴한 비용으로 물을 끌어올 수 있다면 업데이트 후 힙에 추가
            if pay_list[next_node] > connect_list[node][next_node]:
                pay_list[next_node] = connect_list[node][next_node]
                heapq.heappush(node_list, (pay_list[next_node], next_node))

# 결과 출력
print(result)