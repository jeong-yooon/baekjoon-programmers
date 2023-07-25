def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)] # 2차원 배열 행만큼 방문횟수 생성
    for com in range(n):
        if visited[com] == False: # 방문하지 않은 곳이라면
            DFS(n, computers, com, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True # 방문표시
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: #연결된 컴퓨터
            if visited[connect] == False: # 방문하지 않은 곳이라면 DFS 탐색 진행
                DFS(n, computers, connect, visited)