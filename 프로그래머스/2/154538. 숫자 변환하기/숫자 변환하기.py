from collections import deque

def solution(x, y, n):
    dis = [0 for _ in range(y+1)] # 연산횟수
    Q = deque()
    Q.append(x)
    if x == y: # 두 수가 같다면 연산 필요 x
        return 0
    
    while Q: # Q가 존재하는 동안
        nx = Q.popleft()
        for dir in range(3): # 세가지 연산중 하나
            if dir == 0:
                cur_x = nx * 2
            if dir == 1:
                cur_x = nx * 3
            if dir == 2:
                cur_x = nx + n
                
            if cur_x > y or dis[cur_x]: # x가 y보다 클 때
                continue
            if cur_x == y: # 연산결과가 y와 일치할 때
                return dis[nx] + 1 # 연산횟수 반환
            
            Q.append(cur_x) # 큐에 연산결과 저장
            dis[cur_x] = dis[nx] + 1 # 연산횟수 저장
    
    return -1 # return 조건 만족하지 않으면 -1