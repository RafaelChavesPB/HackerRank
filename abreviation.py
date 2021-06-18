# a = AF b = A - inválido 
# a = AA b = A - inválido 
# a = a b = AF - inválido
# a = Aa b = AAA - inválido
# a = aa b = A - válido

from collections import Counter



cap_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
letters = "QWERTYUIOPASDFGHJKLZXCVBNM".lower()
a_maiusculas = []
a_minusculas = []
a = input()
x = Counter(a)
index = {}
for i in range(26):
    if cap_letters[i] in x:
        a_maiusculas.append(x[cap_letters[i]])
    else:    
        a_maiusculas.append(0)
    if letters[i] in x:
        a_minusculas.append(x[letters[i]])
    else:
        a_minusculas.append(0)
    index[cap_letters[i]]=i+26
    index[letters[i]]=i
print(index)
print(a_maiusculas)
# b = input()
