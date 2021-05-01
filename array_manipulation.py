n,m = [int(x) for x in input().split()]
arr = []
for i in range(n+1):
    arr.append(0)
for i in range(m):
    a,b,k = map(int,input().split())
    arr[a-1]+=k
    arr[b]-=k
acc=0
ans=0
for i in range(n):
    acc+=arr[i]
    ans=max(ans,acc)
print(ans)