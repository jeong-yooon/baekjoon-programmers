import sys
from itertools import permutations
input = sys.stdin.readline

if __name__ == '__main__':

    N = int(input())
    num = list(map(int, input().split()))
    op_num = list(map(int, input().split()))  # +, -, *, /
    op_list = ['+', '-', '*', '/']
    op = []

    for k in range(len(op_num)): # 사칙연산 순환
        for i in range(op_num[k]): # 해당 사칙연산에 대한 숫자 만큼
            op.append(op_list[k]) # op에 저장한다.

    maximum = -1000000000000000
    minimum = 1000000000000000

    for case in permutations(op, N - 1): # 사칙연산으로 만들 수 있는 경우의 수 모두 계산
        total = num[0]
        for r in range(1, N):
            if case[r - 1] == '+':
                total += num[r]
            elif case[r - 1] == '-':
                total -= num[r]
            elif case[r - 1] == '*':
                total *= num[r]
            elif case[r - 1] == '/':
                total = int(total / num[r])

        if total > maximum: # 최댓값
            maximum = total
        if total < minimum: # 최솟값
            minimum = total

    print(maximum)
    print(minimum)