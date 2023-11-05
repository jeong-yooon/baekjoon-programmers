import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split()) # 문제 수, 학생 수

s = [0] * m # 문제 해결 능력
answer = 0 # 모든 문제가 해결됨
flag = 0

for i in range(n): # 팀이 이기려면 모든 문제를 해결해야 함
    answer |= (1 << i)

for i in range(m): # 학생의 문제 해결 능력에 대한 비트마스크 생성
    tmp = (list(map(int, input().split())))
    for j in tmp[1:]:
        s[i] |= (1 << j - 1)

def find(): # 모든 문제를 해결하기 위해 필요한 최소 학생 수 탐색
    for i in range(1, m + 1):
        d = list(combinations(s, i)) # 각 팀 크기에 대해 가능한 모든 학생 조합을 생성
        for probs in d:
            tmp = 0
            for prob in probs: # 각 조합에 대해 학생들의 문제 해결 능력의 합집합을 계산
                tmp |= (prob)
                if answer == tmp: # answer 비트 마스크오 같아면 모든 문제 해결
                    return i # 최소 학생 수로 팀 크기 반환
    return -1


print(find())