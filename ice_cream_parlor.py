cases = int(input())
for t in range(cases): 
    money = int(input())
    size = int(input())
    arr = [int(x) for x in input().split()]
    map = {}
    for it in range(size):
        map[arr[it]] = it + 1
    for it in range(size):
        searched = money - arr[it]
        if searched in map:
            pos = map[searched]
            if pos!=it+1:
                print(min(pos,it+1),max(pos,it+1)) 
                break
    
    
    
