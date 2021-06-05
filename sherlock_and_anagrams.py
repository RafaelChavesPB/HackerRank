def sherlockAndAnagrams(s):
    answer = 0
    for i in range(1,len(s)):
        for j in range(len(s)-i+1):
            substr = sorted(s[j:j+i])
            for k in range(j+1,len(s)-i+1):
                answer+=substr==sorted(s[k:k+i])
    return answer


print(sherlockAndAnagrams("abba"))
print(sherlockAndAnagrams("abcd"))
print(sherlockAndAnagrams("ifailuhkqq"))
print(sherlockAndAnagrams("kkkk"))
print(sherlockAndAnagrams("cdcd"))





            