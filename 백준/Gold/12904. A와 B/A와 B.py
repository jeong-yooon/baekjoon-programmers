import sys
input = sys.stdin.readline

# 입력으로부터 문자열 S와 T를 받아 리스트로 변환
s = list(input().rstrip())
t = list(input().rstrip())

switch = False  # S를 T로 바꿀 수 있는지 여부를 나타내는 변수 초기화
while t:
    if t[-1] == 'A':  # T의 마지막 문자가 'A'일 경우
        t.pop()  # T의 마지막 문자를 제거
    elif t[-1] == 'B':  # T의 마지막 문자가 'B'일 경우
        t.pop()  # T의 마지막 문자를 제거
        t.reverse()  # T를 뒤집음
    if s == t:  # 만약 S와 T가 같아졌다면
        switch = True  # switch 변수를 True로 변경하고 반복문 종료
        break

# 결과 출력
if switch:
    print(1)  # S를 T로 바꿀 수 있는 경우
else:
    print(0)  # S를 T로 바꿀 수 없는 경우