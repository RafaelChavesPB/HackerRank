pd = []
def rec(n, i):
    if i > n:
        return 0
    if i == n:
        return 1
    if pd[i] != -1:
        return pd[i]
    pd[i] = (rec(n, i+1)+rec(n, i+2)+rec(n, i+3))%10000000007
    return pd[i] 

cases = int(input())
for case in range(cases):
    pd = [-1]*37
    n = int(input())
    print(rec(n, 0))
