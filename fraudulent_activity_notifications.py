n, s = map(int, input().split())
v = [int(i) for i in input().split()]
acc = [0]*201
notifications = 0
for i in range(n):
    if i >= s:
        median = 0
        q = 0
        if s % 2:
            for j in range(201):
                q += acc[j]
                if q >= s//2 + 1:
                    median = j
                    break
        else:
            flag = False
            for j in range(201):
                q += acc[j]
                if not flag:
                    if q == s//2:
                        flag = True
                        median += j
                    elif q > s//2:
                        median = j
                        break
                else:
                    if q > s//2:
                        median += j
                        median/=2
                        break
        if v[i] >= 2*median:
            notifications += 1
    acc[v[i]] += 1
    if i>= s:
        acc[v[i-s]]-=1
print(notifications)