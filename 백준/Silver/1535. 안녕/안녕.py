import sys
input = sys.stdin.readline

N = int(input()) # 사람 수
L = [int(x) for x in input().split()] # 체력
J = [int(x) for x in input().split()] # 기쁨
L, J = [0] + L, [0] + J # 0을 추가하여 인덱스 계산을 편리하게 한다.
dp = [[0 for _ in range(101)] for _ in range(N+1)] # j 체력을 사용했을 때 얻을 수 있는 최대 기쁨

for i in range(1, N+1): # 사람
    for j in range(1, 101): # 체력
        if L[i] <= j: # 이 사람을 선택할 경우와 선택하지 않을 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
        else: # 체력을 초과할 경우
            dp[i][j] = dp[i-1][j]

print(dp[N][99]) # 최대 체력에서 얻을 수 있는 최대 기쁨