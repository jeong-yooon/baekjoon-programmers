import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
dp = [[0]*n for i in range(n)] # 2차원 dp 생성

for i in range(n): # s=e인 경우는 모두 팰린드롬
    dp[i][i]=1
# s와 e차이가 1인 경우
for i in range(n-1):
    if seq[i]==seq[i+1] : dp[i][i+1]=1
    else : dp[i][i+1]=0
# s와 e차이가 2이상인 경우
for cnt in range(n-2): # s와 e의 차이값
    for i in range(n-2-cnt): # 시작값
        j = i+2+cnt # 끝값
        if seq[i]==seq[j] and dp[i+1][j-1]==1 : # 양 끝값이 같고 그 사이 값이 팰린드롬일 때
            dp[i][j]=1 # 해당 값은 팰린드롬

m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1]) # 각 좌표에 대한 dp값 출력