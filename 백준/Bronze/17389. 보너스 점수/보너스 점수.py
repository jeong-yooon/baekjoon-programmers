import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()  # 문자열 양끝의 공백 제거

total_score = 0
bonus = 0

for i in range(n):
    if s[i] == 'O':
        basic_score = i + 1
        total_score += basic_score + bonus
        bonus += 1
    else:
        bonus = 0

print(total_score)