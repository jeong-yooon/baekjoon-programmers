import sys
input = sys.stdin.readline

def calculate(m, n, x, y):
    k = x #k를 x로 초기화: k-x가 m의 배수여야 하기 때문
    while k <= m * n: #k의 범위는 m*n(카잉 달력의 총 년도 수 = m과 n의 최소공배수)을 넘을 수 없기 때문
        # x와 y가 각자의 주기(m과 n)에 맞게 증가하는 것
        if (k - x) % m == 0 and (k - y) % n == 0: #2개의 조건을 만족하는 k값을 찾는다.
            return k
        k += m # 처음에 k를 x로 설정했으므로 다음 가능한 후보는 x + m일 것이기 때문
    return -1

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())

    print(calculate(m, n, x, y))