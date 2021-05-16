def rec(num,repeats):
    if len(num) <= 1 and repeats == 1  :
        return num 
    acc = 0 
    for c in num:
        acc += int(c)
    acc *= repeats
    return rec(str(acc),1)


while True:
    try:
        num, repeats = input().split()
        print(rec(num,int(repeats)))
    except:
        break