import sys
import heapq
input = sys.stdin.readline

# 입력 받기
n, m, k = map(int, sys.stdin.readline().split())

# 선호도 순서로 정렬하여 입력
beers = [list(map(int, input().split())) for _ in range(k)]
beers = sorted(beers, key=lambda x: (x[1], x[0]))

preference = 0
pq = []  # 우선순위 큐를 사용할 리스트

# 낮은 도수부터 먹어보면서 N을 만족하는지 확인
# 만족하지 않으면 -1 출력하고 종료
for i in beers:
    preference += i[0]  # 현재 맥주의 선호도를 더함
    heapq.heappush(pq, i[0])  # 현재 맥주의 선호도를 우선순위 큐에 추가

    if len(pq) == n:  # 현재까지의 맥주가 n개가 되었을 때
        if preference >= m:  # 만족도가 m 이상이면
            answer = i[1]  # 현재까지의 맥주 중 가장 높은 도수의 맥주를 선택
            break
        else:
            preference -= heapq.heappop(pq)  # 만족도를 만족하지 못하면 가장 낮은 선호도를 갖는 맥주를 제거

# for-else 구문: for문이 break 없이 정상적으로 종료되면 else 블록이 실행됨
else:
    print(-1)
    exit()

print(answer)
