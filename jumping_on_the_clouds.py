n = int(input())
clouds =  list(map(int,input().split()))
current_pos = 0
answer = 0 
while current_pos!=n-1:
    if current_pos == n-2:
        answer+=1
        current_pos+=1
    else:
        if not clouds[current_pos+2]:
            current_pos+=2
        else:
            current_pos+=1
        answer+=1
print(answer)
