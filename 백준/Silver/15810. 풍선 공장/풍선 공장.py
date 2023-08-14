def isPossible(time):
    balloon=0
    for i in arr:
        balloon += time//i
    if balloon>=M: # 주어진 풍선개수보다 많으면
        return True
    return False

N,M = map(int,input().split()) # 스태프수, 풍선의 개수
arr = list(map(int,input().split())) # 풍선 만드는데 걸리는 시간

start = 0 # 최소 시간
end = 10000000000000 # 최대 시간
answer = 0
while start<=end:
    mid = (start+end)//2
    if isPossible(mid):
        end = mid-1
        answer=mid
    else:
        start = mid+1

print(int(answer))