import sys
input = sys.stdin.readline

while True:
    A = int(input())
    if A == 0:
        break

    A2 = A**2
    # 삼각형이 될 조건
    # c < a + b
    # a^2 = c^2 - b^2
    # a^2 = (c - b)(c + b)
    cnt = 0
    for i in range(1, A + 1):
        if A2 % i == 0: # A의 약수인 i 구하기
            B = i
            C = A2 // i
            if (C - B) // 2 > A and (B + C) % 2 == 0: # 삼각형이 될 조건: 삼각형 한변의 길이, 삼각형 둘레가 짝수인가
                cnt += 1

    print(cnt)

