import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

def find_parent(x): # 부모 노드를 찾는 함수
    if parent[x] != x:
        parent[x] = find_parent(parent[x]) # 재귀 호출
    return parent[x]

def union_parent(a, b): # 두 노드를 합치는 함수
    a = find_parent(a) # 부모 노드 찾기
    b = find_parent(b)
    if a < b: # 두 노드 중 작은 번호를 가지는 노드를 부모로 설정
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(N+1)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split()) # 선 정보 컴퓨터A, 컴퓨터B, 비용C
    edges.append((c, a, b))

edges.sort()
result = 0
for c, a, b in edges:
    if find_parent(a) != find_parent(b): # 선이 연결하려는 두 컴퓨터가 같은 집합에 속하지 않는 경우
        union_parent(a, b) # 두 컴퓨터 연결
        result += c # 최소 비용 추가

print(result)