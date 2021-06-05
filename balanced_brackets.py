def solve(s):
    stack = []
    for c in s:
        if len(stack) == 0 and (c == '}' or c == ']' or c == ')'):
                return False
        else:
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
            else:
                if c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
    return len(stack) == 0

n = int(input())
while n > 0:
    n -= 1
    s = input()
    answer = solve(s)
    if answer:
        print("YES")
    else:
        print("NO")