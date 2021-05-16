pd = [-1]*37
def rec(n):
    if n<=1:
        return n
    if pd[n]!=-1:
        return pd[n]
    pd[n]=rec(n-1)+rec(n-2)
    return pd[n]

n = int(input())
print(rec(n))