import sys
input = sys.stdin.readline

N, M = map(int, input().split())
house = []
space = []
ans = 400 # 20 * 20

for r in range(N): # 지도 입력받기
    row = list(input())
    for c in range(M): # 마을이 있는 곳과 없는 곳 좌표값 저장
        if row[c] == '1':
            house.append((r, c))
        else:
            space.append((r, c))

# 최단 거리 계산
for s1 in range(len(space)):
    for s2 in range(s1 + 1, len(space)):
        max_cst = 0
        for h in house:
            dist_s1_h = abs(space[s1][0] - h[0]) + abs(space[s1][1] - h[1]) # 독주머니1 - 마을
            dist_s2_h = abs(space[s2][0] - h[0]) + abs(space[s2][1] - h[1]) # 독주머니2 - 마을
            max_cst = max(max_cst, min(dist_s1_h, dist_s2_h)) # 둘 중에 더 거리가 긴 것

            if max_cst > ans: # ans 보다 현재 값이 더 크면 정답 x
                break

        ans = min(ans, max_cst) # 최솟값 갱신

print(ans)
