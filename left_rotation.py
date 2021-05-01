n, d = map(int, input().split())
d %= n
arr = [int(x) for x in input().split()]
answer = ''
for i in range(n):
    answer += f"{arr[(i+d)%n]} "
print(answer)