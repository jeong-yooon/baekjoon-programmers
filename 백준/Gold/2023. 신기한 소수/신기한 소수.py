import sys
input = sys.stdin.readline

n = int(input())

# 소수 판별
def isPrime(a):
    if (a < 2):
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if (a % i == 0):
            return False
    return True

def dfs(num):
    # 목표 길이 도달 시 멈춤
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if isPrime(temp):
                dfs(temp)

# 한자리수 소수 = 2,3,5,7
dfs(2)
dfs(3)
dfs(5)
dfs(7)