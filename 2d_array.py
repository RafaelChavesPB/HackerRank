def hourglassSum(arr, i, j):
    sum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
    sum += arr[i][j]
    sum += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
    return sum
arr = []
answer = -63
for i in range(6):
    line = list(map(int,input().split()))
    arr.append(line)
for i in range(1,5):
    for j in range(1,5):
        answer = max(hourglassSum(arr,i,j),answer)
print(answer)

