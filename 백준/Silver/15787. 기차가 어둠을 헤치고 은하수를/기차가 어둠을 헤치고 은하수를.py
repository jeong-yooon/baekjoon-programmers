from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())   # n: 기차 수, m: 명령 수
order = list(tuple(map(int, input().split())) for _ in range(m)) # m개의 명령 입력

train = [deque(0 for _ in range(20)) for _ in range(n)] # n개의 기차 좌석 선언

for i in range(m): # 명령 개수 만큼 탐색
  if order[i][0] == 1: # 1 i x
    train[order[i][1]-1][order[i][2]-1] = 1 # 탑승
  elif order[i][0] == 2: # 2 i x
    train[order[i][1]-1][order[i][2]-1] = 0 # 하차
  elif order[i][0] == 3: # 3 i
    train[order[i][1]-1].rotate(1) # 전체 +1
    train[order[i][1]-1][0] = 0 # 맨앞 비우기
  else: # 4 i
      train[order[i][1]-1].rotate(-1) # 전체 -1
      train[order[i][1]-1][-1] = 0 # 맨뒤 비우기

output_train = [] # 은하수를 건널 수 있는 기차
for i in range(n): # 기차 수 만큼 탐색
  if train[i] not in output_train: # 중복되지 않는다면 저장
    output_train.append(train[i])

print(len(output_train))