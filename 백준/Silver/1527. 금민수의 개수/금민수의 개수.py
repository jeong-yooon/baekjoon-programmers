import sys
from itertools import product
input = sys.stdin.readline

a, b = map(int, input().split())
x = len(str(a))
y = len(str(b))

cnt = 0

for i in range(x, y+1): # x부터 y까지의 자릿수에 대해 반복문
    # product는 여러 개의 이터러블을 받아 가능한 모든 조합을 생성
    lst = list(product([4, 7], repeat=i)) # 현재 자릿수 i에 대해 4, 7의 반복 가능한 조합을 생성
    for num in lst:
        n = int(''.join(map(str, num)))
        if a <= n <= b:
            cnt += 1

print(cnt)