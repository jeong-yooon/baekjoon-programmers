import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n) # 로봇 위치
res = 0 # 걸린 시간

while 1:
    belt.rotate(1) # 벨트 한칸 회전
    robot.rotate(1) # 로봇 한칸 회전
    robot[-1] = 0  # 로봇이 내려가는 부분이니 0
    if sum(robot):  # 로봇이 존재하면
        for i in range(n - 2, -1, -1):  # 로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터 역순
            # 현재 위치에 로봇이 있고, 다음 위치에 로봇 없을 때 다음 벨트의 내구성이 1이상이면
            if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
                robot[i + 1] = 1 # 로봇 한칸 이동
                robot[i] = 0 # 현위치 로봇 내림
                belt[i + 1] -= 1 # 다음 위치 내구성 1 감소
        robot[-1] = 0  # 벨트 끝 내려가는 부분은 로봇 내림
    if robot[0] == 0 and belt[0] >= 1: # 첫 위치에 로봇 없고, 내구성 1이상일 때
        robot[0] = 1 # 첫 위치에 로봇 올림
        belt[0] -= 1 # 벨트 내구성 1 감소
    res += 1 # 시간 카운팅
    if belt.count(0) >= k: # 내구성 0인 칸 수가 k 이상일 때
        break

print(res)