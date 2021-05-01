def bubble_sort(arr):
    acc=0
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                acc+=1
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return acc
n = int(input())
arr = [int(x) for x in input().split()] 
print(f'Array is sorted in {bubble_sort(arr)} swaps.')
print(f'First Element: {arr[0]}')
print(f'Last Element: {arr[-1]}')