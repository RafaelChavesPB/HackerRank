def twoStrings(s1, s2):
    s1=set(s1)
    s2=set(s2)
    sbstr = s1.intersection(s2)
    if len(sbstr):
        return 'YES'
    else:
        return 'NO'

print(twoStrings('hello','world'))
print(twoStrings('hi','world'))
