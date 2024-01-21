import sys
input = sys.stdin.readline

N, K = map(int, input().split())
p = 1000000007

# 팩토리얼 값 계산(나머지 연산 적용)
def factorial(N):
    n = 1
    for i in range(2, N + 1):
        n = (n * i) % p
    return n

# 거듭제곱 계산(나머지 연산 적용)
def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = square(n, k // 2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p

# 분자에 해당하는 팩토리얼 계산
top = factorial(N)
# 분모에 해당하는 팩토리얼 계산 및 역원(페르마의 소정리) 적용
bot = factorial(N - K) * factorial(K) % p

# 조합 공식을 페르마의 소정리를 이용하여 구현
result = top * square(bot, p - 2) % p

# 결과 출력
print(result)
