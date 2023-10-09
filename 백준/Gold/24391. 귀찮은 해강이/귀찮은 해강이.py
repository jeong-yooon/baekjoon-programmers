import sys
input=sys.stdin.readline

# 서로소 집합에서 특정 원소 x의 루트 노드를 찾음
def Find(x):

    if x!=disjoint[x]:
        disjoint[x]=Find(disjoint[x])
    return disjoint[x]

def Union(a,b):

    a=Find(a)
    b=Find(b)

    # 더 큰 쪽으로 합쳐서 하나의 집합으로 만든다
    if a>b:
        disjoint[a]=b
    else:
        disjoint[b]=a

N,M=map(int,input().split())

disjoint=[0]*(N+1) # 각 원소 부모노드 저장

for i in range(1,N+1): # 건물번호 초기화
    disjoint[i]=i


for i in range(M):
    a,b=map(int,input().split())
    Union(a,b) # 합집합

L=list(map(int,input().split()))
total=0
for i in range(1,len(L)):
    if Find(L[i-1])!=Find(L[i]): # 루트 노드가 다를 때
        total+=1

print(total)