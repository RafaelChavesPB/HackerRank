def counting(arr,i):
    acc = 0
    while i!=arr[i]:
        acc+=1
        j = arr[i]
        arr[j],arr[i]=arr[i],arr[j]
    return acc

n=int(input())
arr = [int(x)-1 for x in input().split()]
visited = [0]*len(arr)
acc = 0
for i in range(len(arr)):
    if arr[i]!=i:
       acc+=counting(arr,i)
print(acc)


