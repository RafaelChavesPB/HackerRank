def getMedian(arr):
    n = len(arr)
    mid = n//2
    if n%2:
        return arr[mid]
    mid = n//2
    return (arr[mid-1]+arr[mid])/2

def sliceInMid(arr):
    n = len(arr)
    if n%2:
        mid = n//2
        return arr[:mid],arr[mid+1:]
    mid = n//2
    return arr[:mid],arr[mid:]

n = int(input())
values = [int(x) for x in input().split()]
freq = [int(x) for x in input().split()]
data = sorted(list(zip(values,freq)), key = lambda x: x[0])
arr = []
for x in data:
    arr += [x[0]]*x[1] 
q2 = getMedian(arr)
fhalf,shalf = sliceInMid(arr)
q1 = getMedian(fhalf)
q3 = getMedian(shalf)
print(f"{q3-q1:.1f}")

