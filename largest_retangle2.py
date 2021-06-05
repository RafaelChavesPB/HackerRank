n =  int(input())
heights = [int(x) for x in input().split()]
heights.append(0)
stack_h = []
stack_p = []
max_area = 0
for i in range(len(heights)):
    init = i 
    while len(stack_h) and stack_h[-1]>heights[i]:
        init = stack_p[-1] 
        max_area =  max(stack_h.pop()*(i-stack_p.pop()),max_area)
    if len(stack_h)==0 or stack_h[-1]<heights[i]:
        stack_h.append(heights[i])
        stack_p.append(init)
print(max_area)
        
            