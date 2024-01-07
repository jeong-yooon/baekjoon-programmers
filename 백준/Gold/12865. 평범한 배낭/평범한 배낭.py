import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [[0,0]]
dp = [[0]*(k+1) for _ in range(n+1)]
# 물건 무게, 가치 입력받기
for i in range(n):
    bag.append(list(map(int, input().split())))
bag.sort() # 무게에 대하여 오름차순 배열

for i in range(1, n+1):
    for j in range(1, k+1):
        w = bag[i][0]
        v = bag[i][1]

        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[n][k])