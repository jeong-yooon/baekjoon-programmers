import sys
input = sys.stdin.readline

# 초기 상수 및 배열 선언
MXN = 10000  # 최대 사람 수를 나타내는 상수
dp = [[0, 0] for _ in range(MXN + 1)]  # 동적 계획법을 위한 2차원 배열
a, b, n = 1, 2, 0  # 현재 피보나치 수열 항의 앞 항, 뒷 항, 사람 수

# 입력 받기
n = int(input()) # 사람의 수

# DP 배열 초기화
for i in range(1, n + 1):
    dp[i][0] = float('inf')  # 최소 치킨 수를 무한대로 초기화

# DP 구현
while b <= n:
    for i in range(b, n + 1):
        # 최소치킨 수 갱신
        dp[i][0] = min(dp[i][0], dp[i - b][0] + a)
        # 최대치킨 수 갱신
        dp[i][1] = max(dp[i][1], dp[i - b][1] + a)
    b, a = b + a, b  # 다음 피보나치 수열 항으로 이동

# 결과 출력
print(dp[n][0], dp[n][1])  # 최소치킨 수와 최대치킨 수 출력
