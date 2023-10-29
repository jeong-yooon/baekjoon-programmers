import sys
input = sys.stdin.readline

N = int(input()) # 원판 갯수
targetNum = N # 목표 숫자
cnt = 0 # 옮긴횟수
result = [] # 옮긴루트
First = [] # 첫번째 장대
Second = [] # 두번째 장대

numbers = list(map(int, input().split())) # 원판 반경 정보

for num in numbers:
    First.append(num)

while targetNum > 0: # 타겟 숫자가 0이 될 때까지 반복
    if targetNum in First: # First 장대 스택에 targetNum이 있을 때
        while First:
            now = First.pop() # 스택의 가장 위에 있는 숫자를 꺼내서 now에 저장
            if now == targetNum:
                result.append("1 3") # 첫 번째 스택에서 세 번째 스택으로 이동
                cnt += 1 # 옮긴횟수
                targetNum -= 1
                break
            else:
                result.append("1 2") # 첫 번째 스택에서 두 번째 스택으로 이동
                cnt += 1
                Second.append(now)
    elif targetNum in Second:
        while Second:
            now = Second.pop() # Second 장대 스택의 가장 위에 있는 숫자를 꺼내서 now에 저장
            if now == targetNum:
                result.append("2 3") # 두 번째 스택에서 세 번째 스택으로 이동
                cnt += 1
                targetNum -= 1
                break
            else:
                result.append("2 1") # 두 번째 스택에서 첫 번째 스택으로 이동
                cnt += 1
                First.append(now)

print(cnt)
print("\n".join(result))
