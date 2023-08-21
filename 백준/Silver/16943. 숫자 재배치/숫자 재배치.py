import sys
import itertools
input = sys.stdin.readline

if __name__ == '__main__':
    a, b = input().split()
    c = -1

    nPn = itertools.permutations(a, len(a)) # nPn 구하기
    pt = [''.join(p) for p in nPn] # join으로 튜플을 문자열로 바꾸어 리스트화 한다.

    for i in pt:
        if i[0] == '0':  # 0으로 시작하는 경우
            continue
        i = int(i)
        if int(i) < int(b): # b보다 작을 때
            c = max(c, int(i)) # 최댓값 저장
    print(c)