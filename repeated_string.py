repeated_string = input()
n = int(input())
size = len(repeated_string) 
substr_q = repeated_string.count('a')
answer = (n//size)*substr_q
n%=size
for it in range(0,n):
    if repeated_string[it]=='a':
        answer+=1
print(answer)