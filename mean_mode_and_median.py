def getMedian(arr):
    n = len(arr)
    mid = n//2
    if n%2:
        return arr[mid]
    return (arr[mid-1]+arr[mid])/2 

def getMean(arr):
    return sum(arr)/len(arr)

def getModa(arr):
    prv = -1
    count = 0
    moda = (-1,0)
    for i in arr:
        if i==prv:
            count+=1
        else:
            if count>moda[1]:
                moda = (prv,count)
            count = 1
            prv = i
    return moda[0]

n = int(input())
arr = sorted([int(x) for x in input().split()])
print(f"{getMean(arr):.1f}")
print(f"{getMedian(arr):.1f}")
print(f"{getModa(arr)}")