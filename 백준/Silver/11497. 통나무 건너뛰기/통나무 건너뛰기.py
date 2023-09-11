import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스

for i in range(t):
    n = int(input()) # 통나무 개수
    a = list(map(int,input().split())) # 통나무 높이
    a.sort() # 정렬
    result = 0

    # 오른쪽 왼쪽 번갈아 놓으면 최대 높이 차이 인덱스 두 개 정도 차이난다.
    for j in range(2,n):
        c = a[j] - a[j - 2]
        result = max(c, result) # 차이의 최댓값
    print(result)