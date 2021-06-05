n = int(input())
heights = [int(x) for x in input().split()]
max_area = 0 
for i in range(n):
    min_height = heights[i]
    for j in range(i,n):
        min_height = min(heights[j], min_height)
        max_area = max((j-i+1)*min_height,max_area)
print(max_area)
