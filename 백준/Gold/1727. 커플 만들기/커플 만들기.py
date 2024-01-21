import sys

input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
man = list(map(int, input().split()))
woman = list(map(int, input().split()))

# 남자와 여자의 성격을 오름차순으로 정렬
man.sort()
woman.sort()

# DP 테이블 초기화
d = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

# DP 테이블 갱신
for i in range(1, N + 1):
    for j in range(1, M + 1):
        # 현재 커플의 성격 차이를 계산하고 이전까지의 누적 차이를 더함
        d[i][j] = d[i - 1][j - 1] + abs(man[i - 1] - woman[j - 1])

        # i가 j보다 크면 i쪽이 사람이 더 많으므로, i-1쪽과의 차이 중 작은 값을 선택
        if i > j:
            d[i][j] = min(d[i][j], d[i - 1][j])
        # i가 j보다 작으면 j쪽이 사람이 더 많으므로, j-1쪽과의 차이 중 작은 값을 선택
        elif i < j:
            d[i][j] = min(d[i][j], d[i][j - 1])

# 결과 출력
print(d[N][M])
