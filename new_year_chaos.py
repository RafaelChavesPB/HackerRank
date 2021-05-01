def verify(arr):
    for i in range(len(arr)):
        if arr[i]-i-1>2:
            return False
    return True 

def inversions(arr):
    if len(arr)==1:
        return arr, 0
    mid = len(arr)//2
    left, acc0 = inversions(arr[:mid]) 
    right, acc1 = inversions(arr[mid:])
    acc = acc0 + acc1
    l = 0
    r = 0
    sorted_arr = []
    for it in range(len(arr)):
        if l==len(left):
            sorted_arr.append(right[r])
            r+=1
        elif r==len(right):
            sorted_arr.append(left[l])
            l+=1
        else:
            if left[l] < right[r]:
                sorted_arr.append(left[l])
                l+=1
            else:
                sorted_arr.append(right[r])
                acc +=  mid + r - it
                r+=1
    return sorted_arr, acc

t = int(input())
for cases in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if verify(arr):
        print(inversions(arr)[1])
    else:
        print('Too chaotic')