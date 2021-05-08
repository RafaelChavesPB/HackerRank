def merge(left, right):
    size_l = len(left)
    size_r = len(right)
    size_t = size_l + size_r
    it_l = 0
    it_r = 0
    inversions = 0
    sorted_arr = [0]*size_t
    for i in range(size_t):
        if it_l == size_l:
            sorted_arr[i]=right[it_r]
            it_r += 1
        elif it_r == size_r:
            sorted_arr[i]=left[it_l]
            it_l += 1
        elif left[it_l] <= right[it_r]:
            sorted_arr[i]=left[it_l]
            it_l += 1
        else:
            sorted_arr[i]=right[it_r]
            inversions += size_l - it_l
            it_r += 1
    return sorted_arr, inversions

def mergesort(arr):
    size = len(arr)
    mid = size//2
    if size<=1:
        return arr,0
    left, inv_l = mergesort(arr[:mid])
    right, inv_r = mergesort(arr[mid:])
    arr, inv = merge(left,right)
    return arr, inv+inv_l+inv_r


d = int(input())
for case in range(d):
    n = int(input())
    arr = [int(x) for x in input().split()]
    sorted_arr, inv = mergesort(arr)
    print(inv)
