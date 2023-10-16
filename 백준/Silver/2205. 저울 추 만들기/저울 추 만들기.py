import sys
input = sys.stdin.readline

n = int(input())
check = [] # 제곱 수 저장
idx = 2 # 제곱 수 생성

while True:
    if idx <= (2*n)+1: # 2의 거듭제곱 수 중에서 n보다 작거나 같은 값만 check에 저장
        check.append(idx)
    else:
        break
    idx *= 2

ir = [0 for i in range(0,n+1)] # 주석 질량
ir[0] = 1

for i in range(len(ir)-1,0,-1): # 주석 질량 역순환
    for k in range(0,len(check)): # 제곱수 길이만큼 순환
        if check[k] - i <= n and check[k] > i: # 제곱수에서 주석을 뺀값이 갯수보다 작고, 제곱수가 주석질량보다 클 때
            if ir[i] == 0 and ir[check[k]-i] == 0: # 주석 질량이 0이거나 제곱수에서 뺀 값이 0 일때 해당 주석 저장
                ir[i] = check[k] - i
                ir[check[k]- i] = i
                break
for i in range(1,len(ir)):
    print(ir[i]) # 주석의 질량