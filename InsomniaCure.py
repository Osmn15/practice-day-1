n=int(input())
lst=list(map(int,input().split()))
m=int(input())
queries=list(map(int,input().split()))
d= {}
for i in range(n):
    d[lst[i]]=i
vasya=0
petya=0
for q in queries:
    index=d[q]
    vasya+=d[q]+1
    petya+=n-d[q]
print(vasya,petya)