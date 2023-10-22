import sys
input = sys.stdin.readline

start = -1000000000000000000 # 최솟값
end = 1000000000000000000 # 최댓값

q = int(input())
index = 0

for i in range(1, q + 1):
    line = input().split()
    x = int(line[0]) # 숫자 부분 저장

    if line[1] == "^": # 최솟값 재설정
        start = max(start, x + 1)
    elif line[1] == "v": # 최댓값 재설정
        end = min(end, x - 1)

    if start == end and index == 0: # 정답 발견시 index에 저장
        index = i
    elif start > end: # 모순 발생
        print("Paradox!\n{}".format(i))
        sys.exit()

if index == 0: # 정답이 없으면
    print("Hmm...")
else: # 정답이 있으면
    print("I got it!\n{}".format(index))

