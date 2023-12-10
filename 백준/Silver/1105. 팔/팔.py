# 입력으로 두 개의 문자열 A와 B를 공백을 기준으로 받음
A, B = map(str, input().split(' '))

# 매치된 숫자의 개수를 세기 위한 변수 초기화
ret = 0

# 두 문자열의 길이가 다르면 매치할 수 없으므로 0을 출력하고 종료
if len(A) != len(B):
    print(0)
else:
    # 두 문자열의 길이가 같으면 각 위치의 문자를 비교하면서 매치된 '8'의 개수를 센다
    for i in range(len(A)):
        if A[i] == B[i]:
            if A[i] == '8':
                ret += 1
        else:
            # 문자가 다르면 더 이상 매치할 필요가 없으므로 반복문 종료
            break
    # 매치된 '8'의 개수 출력
    print(ret)