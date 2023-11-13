# xi+1 = xi / 2
# xi+1 = 3*xi + 1

# 예제1 로직 과정
# 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# 8 4 2 1

import sys
input = sys.stdin.readline

while True:
    A, B = map(int,input().split()) # 두 양의 정수

    # 종료 조건
    if A == 0 and B == 0: break

    # 정수 A에 대한 비교
    temp = A
    a = [-1, A] # 첫 번재 수에 대한 수열
    while True:
        # 종료 조건
        if temp == 1: break
        # 홀수일 때
        if temp % 2:
            temp = 3 * temp + 1
            a.append(temp)
        # 짝수일 때
        else:
            temp //= 2
            a.append(temp)

    # 정수 B에 대한 비교
    temp = B
    b = [-2, B] # 두 번째 수에 대한 수열
    while True:
        # 종료 조건
        if temp == 1: break
        # 홀수일 때
        if temp % 2:
            temp = 3 * temp + 1
            b.append(temp)
        # 짝수일 때
        else:
            temp //= 2
            b.append(temp)
    # 리스트 거꾸로 순환
    for i in range(-1, -1000000000, -1):
        if a[i] != b[i]:
            break

    print(f'{A} needs {len(a) + i} steps, {B} needs {len(b) + i} steps, they meet at {a[i + 1]}')