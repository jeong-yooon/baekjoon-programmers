N, K = map(int,input().split())
x = [int(input()) for _ in range(N)]
 
start,end = min(x),max(x)+K # 레벨 최소값, 최대값
while start <= end:
    mid = (start+end)//2
    need_level = sum([mid-lv for lv in x if mid >= lv]) # 중앙값이 레벨보다 클때만 합한다.
    
    if need_level <= K:
        result = mid
        start = mid + 1
    elif need_level > K:
        end = mid - 1
 
print(result)