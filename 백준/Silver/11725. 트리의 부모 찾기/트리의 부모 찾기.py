import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# N 입력
N = int(input())

# tree, parent 초기화
tree = [[] for _ in range(N + 1)] # 해당 인덱스의 노드와 연결되어 있는 자식노드 저장
parent = [None for _ in range(N + 1)]

# DFS
def DFS(graph, vertex, visited):
    # 트리를 순환하며 탐색
    for i in graph[vertex]:
        # 만약 방문하지 않았을 경우 방문할 정점의 값을 할당하고 재귀함수 호출
        if not visited[i]:
            visited[i] = vertex
            DFS(graph, i, visited)

# 주어진 노드로 트리 값 할당
for _ in range(N - 1):
    node_a, node_b = map(int, input().split())
    tree[node_a].append(node_b)
    tree[node_b].append(node_a)

# DFS 함수 사용하여 parent 값 할당
DFS(tree, 1, parent)

# 각 노드의 부모 노드 번호를 2번부터 순서대로 출력
for i in range(2, N + 1):
    print(parent[i])