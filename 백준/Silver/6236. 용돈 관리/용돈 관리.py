import sys
input = sys.stdin.readline

N, M = map(int, input().split())
days = []
for _ in range(N):
    days.append(int(input()))

# 모든 날에 필요한 총 금액, 최솟값, 최댓값
answer, left, right = sum(days), 0, sum(days)

# 이분탐색
while left <= right:
    mid = (left + right) // 2
    count, money = 0, 0
    lack = False # 돈이 부족한 날 체크

    # 각 날짜를 반복하며 필요한 금액 처리
    for d in days:
        if mid - d < 0:
            # 돈을 뽑아도 하루를 못 넘기면
            lack = True
            # 탐색 중지
            break
        elif money - d < 0: # 현재 소유한 금액에서 날짜에 필요한 금액을 빼고도 음수인 경우
            money = mid # 새로운 금액을 뽑아야 하므로
            count += 1 # count 증가
        money -= d # 필요한 금액을 현재 소유한 금액에서 빼준다.

    # 돈이 부족한 날이 없으면
    if not lack:
        # 목표 횟수보다 count가 같거나 작으면 돈을 줄임
        if count <= M:
            right = mid - 1
            if mid < answer:
                answer = mid
        # 목표 횟수보다 count가 크면 돈을 늘림
        elif count > M:
            left = mid + 1
    # 돈이 부족한 날이 있으면 무조건 돈을 늘림
    else:
        left = mid+1

print(answer)