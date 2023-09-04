import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

def bfs(start):
	cnt = 1
	queue = deque([start])
	visit = [False for _ in range(n+1)]
	visit[start] = True # 첫 노드는 방문으로 표시

	while queue:
		cur = queue.popleft()

		for nx in graph[cur]:
			if not visit[nx]: # 첫방문 노드라면
				visit[nx] = True # 방문 표시
				cnt += 1 # 카운팅
				queue.append(nx) # 큐에 저장

	return cnt

graph = [[] for _ in range(n+1)]

for _ in range(m): # 신뢰관계 입력받기
	a,b = map(int,input().split())
	graph[b].append(a)

maxCnt = 1
ans = []

for i in range(1,n+1):
	cnt = bfs(i) # bfs 얻은 값 비교
	if cnt > maxCnt: # 최댓값 갱신
		maxCnt = cnt
		ans.clear() # 초기화
		ans.append(i) # 새 값으로 갱신
	elif cnt == maxCnt:
		ans.append(i)

print(*ans) # 리스트 언패킹