n = int(input())
socks = list(map(int,input().split()))
colors = set(socks)
answer = 0 
for it in colors:
    answer += socks.count(it)//2
print(answer)


