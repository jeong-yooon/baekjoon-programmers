# 사용자로부터 입력을 받기 위해 표준 입력 모듈을 가져옵니다
from sys import stdin

# 부모 관계와 비용을 저장하기 위한 전역 변수
parents = []
charges = []

# x가 속한 집합의 대표(루트)를 찾기 위한 함수
def find(x: int) -> int:
    if parents[x] == x:
        return x
    # 경로 압축: 각 노드의 부모를 루트로 설정합니다
    parents[x] = find(parents[x])
    return parents[x]

# 두 집합을 비용을 기준으로 합치기 위한 함수
def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    # 랭크에 따른 합집합: 비용이 작은 집합을 비용이 큰 집합에 합칩니다
    if charges[x] < charges[y]:
        parents[y] = x
    else:
        parents[x] = y

# 메인 함수
def main():
    # 표준 입력에서 입력을 읽기 위해 input() 함수를 재정의합니다
    def input():
        return stdin.readline().rstrip()

    # 전역 변수를 사용하기 위해 선언
    global parents, charges

    # 친구의 수(n), 친구 관계의 수(m), 예산(k)을 입력으로 받습니다
    n, m, k = map(int, input().split())

    # 부모 관계와 비용 리스트를 초기화합니다
    parents = list(i for i in range(n + 1))
    charges = [0] + list(map(int, input().split()))

    # 각 친구 관계에 대해 합집합을 수행합니다
    for _ in range(m):
        v, w = map(int, input().split())
        union(v, w)

    # 유일한 대표(부모)를 저장하기 위한 집합
    friends = set()
    cost = 0

    # 유일한 대표의 비용을 합산하여 총 비용을 계산합니다
    for i in range(1, n + 1):
        if find(i) not in friends:
            cost += charges[parents[i]]
            friends.add(parents[i])

    # 총 비용이 예산을 초과하는지 확인하고 결과를 출력합니다
    if cost > k:
        print("Oh no")
    else:
        print(cost)

# 프로그램의 진입점
if __name__ == "__main__":
    main()
