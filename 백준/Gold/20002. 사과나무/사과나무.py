import sys

input = sys.stdin.readline

# 입력
N = int(input())

# 정사각 크기의 누적합을 저장할 2차원 배열
prefix = [[0] * (N + 1) for _ in range(N + 1)]

# 누적합 계산
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    for j in range(1, N + 1):
        prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1] + data[j - 1]

# 최댓값을 저장할 변수 초기화
answer = -1001

# 정사각형의 크기를 변화시켜가며 최댓값 찾기
for k in range(N):
    for r in range(1, N - k + 1):  # row
        for c in range(1, N - k + 1):  # col
            # (r, c) ~ (r+k, c+k) 정사각형일 때의 누적합 계산
            current_sum = prefix[r + k][c + k] - prefix[r - 1][c + k] - prefix[r + k][c - 1] + prefix[r - 1][c - 1]

            # 최댓값 갱신
            answer = max(answer, current_sum)

# 최댓값 출력
print(answer)
