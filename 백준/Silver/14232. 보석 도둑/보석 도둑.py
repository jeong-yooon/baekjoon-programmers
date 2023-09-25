import sys
from math import sqrt, ceil # 제곱근, 올림
input = sys.stdin.readline

k = int(input())
j = [] # 보석 무게 리스트

# k의 제곱근 이상의 요소로 k가 나누어지지 않기 때문에 제곱근까지만 검사
for i in range(2, ceil(sqrt(k)) + 1):
    while k % i == 0: # 나누어 떨어지는 k값 구하기
        j.append(i)
        k //= i # 해당 i 값으로 나눈 후 다시 순환

if k != 1: # 소인수분해 되지 않은 값이 있다면
    j.append(k) # 해당값 저장

print(len(j))
print(*j)