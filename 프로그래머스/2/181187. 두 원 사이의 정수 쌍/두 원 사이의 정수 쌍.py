import math
import sys
input = sys.stdin.readline

def solution(r1, r2):
    answer = 0

    # i는 원의 반지름을 나타냄
    for i in range(1, r2+1):
        if i < r1:
            # i가 r1보다 작으면 중심이 (0, 0)인 원 내부에 위치하는 부분 계산
            s = math.ceil(math.sqrt((r1**2 - i**2)))
        else:
            s = 0

        # 중심이 (0, 0)인 원 내에서 i에 대한 가능한 높이 계산
        e = int(math.sqrt((r2**2 - i**2)))

        # 가능한 높이의 범위를 더하여 answer에 누적
        answer = answer + e - s + 1

    # 모든 경우의 수를 고려하므로 4를 곱하여 결과 반환
    return answer * 4
