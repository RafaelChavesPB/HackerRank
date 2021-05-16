def getMedian(arr):
    n = len(arr)
    mid = n//2
    if n%2:
        return arr[mid]
    mid = n//2
    return (arr[mid-1]+arr[mid])//2

def sliceInMid(arr):
    n = len(arr)
    if n%2:
        mid = n//2
        return arr[:mid],arr[mid+1:]
    mid = n//2
    return arr[:mid],arr[mid:]

n = int(input())
arr = sorted(list(map(int, input().split())))
q2 = getMedian(arr)
fhalf,shalf = sliceInMid(arr)
q1 = getMedian(fhalf)
q3 = getMedian(shalf)
print(q1)
print(q2)
print(q3)

