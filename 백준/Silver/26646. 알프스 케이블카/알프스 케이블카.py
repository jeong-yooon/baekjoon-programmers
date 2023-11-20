import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = 0

# c**2 = a**2 + b**2
for i in range(n-1):
    answer += (arr[i] + arr[i+1])**2 + (arr[i] - arr[i+1])**2
print(answer)