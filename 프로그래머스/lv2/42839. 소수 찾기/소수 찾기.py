import itertools
def is_prime(num): # 소수 판단 함수
    if num < 2: # 2보다 작으면 소수가 아니다.
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: # 0~num으로 나누었을때 나누어지는 수가 있으면 소수가 아니다.
            return False
    return True

def solution(numbers):
    answer = []
    for n in range(1, len(numbers) + 1): # nP1, nP2, nP3, ... , nPn 구하기
        nPr = itertools.permutations(numbers, n)
        pt = [''.join(p) for p in nPr] # join으로 튜플을 문자열로 바꾸어 리스트화 한다.
        for l in pt:
            if is_prime(int(l)): # 소수일때 정답리스트에 저장
                answer.append(int(l))
    return len(set(answer)) # 중복수 제거