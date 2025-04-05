t=int(input())
arr=list(map(int,input().split()))
count=0
for i in range(1,6):
    if (sum(arr)+i)%(t+1)!=1:
        count+=1
print(count)