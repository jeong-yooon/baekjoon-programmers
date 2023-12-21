# 세 화학 물질을 두개씩 혼합 가능
# 이익의 최댓값
# 가능한 모든 조합에 대해 이익을 계산하고 최대 이익 탐색

import sys
input = sys.stdin.readline

def max_profit(a, b, c, price):
    # 가능한 모든 조합에 대해 이익을 계산하고 최대 이익을 찾음
    max_price = 0
    for i in range(0, min(a,b)+1): # ab 화합물이 1개일때, 2개일때, 3개일때...
        for j in range(0, min(b-i,c)+1): # bc 화합물이 1개일때, 2개일때, 3개일때...
            k = min(a - i, c - j)  # ca 화합물은 남은 양만큼 사용
            max_price = max(max_price, i*price[0] + j*price[1] + k*price[2])

    return max_price

t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    price = list(map(int, input().split()))

    result = max_profit(a, b, c, price)
    print(result)


