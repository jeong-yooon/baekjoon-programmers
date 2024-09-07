import sys
input = sys.stdin.readline

n = int(input()) # 입력값
arr = [0, 1]

for i in range(2, n+1): # 피보나치 수 계산 반복문
    arr.append(arr[i-1] + arr[i-2])

print(arr[n])