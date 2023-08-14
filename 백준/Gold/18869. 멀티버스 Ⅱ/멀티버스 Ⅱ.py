from collections import defaultdict

m, n = map(int, input().split())
arr = defaultdict(int) # 딕셔너리 생성

for _ in range(m):
    # 행성 입력 받기
    planets = list(map(int, input().split()))
    
    # 행성 정렬 ( 구성 같은 행성 한개만 세기 )
    sp = sorted(list(set(planets))) # 중복제거
    
    # 행성 순위 지정
    rank = {sp[i] : i for i in range(len(sp))} # 0, 1, 2 ...
    
    # 입력 받은 행성에 맞게 순위 저장
    vector = tuple([rank[i] for i in planets])
    
    # 해당 순위 벡터에 대한 개수 추가
    arr[vector] += 1
    
sum = 0

for i in arr.values():
    # n개 중 2개의 우주를 엮어야 하기 때문에 n C 2 를 해줘야 함 (중복 제외)
    sum += (i * (i - 1)) // 2 # nC2
    
print(sum)