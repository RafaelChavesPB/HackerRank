import math 

def getMean(arr):
    return sum(arr)/len(arr)

def getSD(arr, mean):
    acc = 0 
    for x in arr:
        acc += (x-mean)**2
    return math.sqrt(acc/len(arr))
 
n = int(input())
arr = [int(x) for x in input().split()]
mean = getMean(arr)
print(f"{getSD(arr,mean):.1f}")