import sys
input = sys.stdin.readline

n,m = map(int,input().split()) # 영토 크기
area = [list(map(int,input().split())) for _ in range(n)] # 구역별 인구수

dp = [[0]*(m+1) for _ in range(n+1)] # 영토 크기만큼 dp 생성
# 일정 좌표까지의 총 인구수 구하기
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = area[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

# 직사각형 범위 인구수 구하기
for _ in range(int(input())):
    x,y,i,j = map(int,input().split())
    print(dp[i][j] - dp[x-1][j] - dp[i][y-1] + dp[x-1][y-1])
