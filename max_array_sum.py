# def rec(arr, i, flag):
#     if i == len(arr):
#         return 0
#     if (i,flag) in dp:
#         return dp[(i,flag)]
#     best = rec(arr,i+1,True)
#     if flag == True:
#         best = max(rec(arr,i+1,False)+arr[i], best)
#     dp[(i,flag)] = best
#     return best

n = int(input())
arr = list(map(int, input().split()))
dp = [0,0]
for i in range(n):
    dp.append(max(dp[i]+arr[i],dp[i+1]))
print(dp[n+1])