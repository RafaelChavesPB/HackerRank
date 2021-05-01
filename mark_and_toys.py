n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr.sort()
it = 0
count = 0
while arr[it] <= k:
    count+=1
    k-=arr[it]
    it+=1 
print(count)