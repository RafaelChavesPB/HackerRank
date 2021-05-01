n = int(input())
steps = input()
level = 0 
answer = 0
for it in steps:
    if level==-1 and it=='U':
        answer+=1
    if it=='U':
        level+=1
    if it=='D':
        level-=1
print(answer)
        

