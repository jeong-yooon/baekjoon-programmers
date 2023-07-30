n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1 # 방문처리

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and dp[i][j] != 0:
            if i + arr[i][j]<n: # 세로 방향 추가
                dp[i+arr[i][j]][j] += dp[i][j]
            if j + arr[i][j]<n: # 가로 방향 추가
                dp[i][j+arr[i][j]] += dp[i][j]
print(dp[n-1][n-1])