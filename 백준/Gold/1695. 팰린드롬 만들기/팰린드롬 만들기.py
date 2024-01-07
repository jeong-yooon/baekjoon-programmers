import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[0] * N for _ in range(2)]

# 뒷부분부터 탐색해야함
for i in reversed(range(N)):
    for j in range(i+1, N):
        # 짝수와 홀수 구분
        row = i % 2
        # 홀수행(i=1)일 때 i-1=0으로 짝수행을 가리킴, 짝수행(i=0)일 때 i-1=-1로 홀수행을 가리킴
        if arr[i] == arr[j]:
            dp[row][j] = dp[1-row][j-1]
        else:
            dp[row][j] = min(dp[row][j-1], dp[1-row][j]) + 1

print(dp[0][N-1])
