def checkMagazine(magazine, note):
    hash_table = {}
    for it in magazine:
        if it in hash_table:
            hash_table[it]+=1
        else:
            hash_table[it]=1
    for it in note:
        q = hash_table.get(it)
        if q==None or q<=0:
            print("No")
            return 
        else:
            hash_table[it]-=1

    print("Yes")


checkMagazine(list("ive got a lovely bunch of coconuts".split()),list("ive got some coconuts".split()))
checkMagazine(list("two times three is not four".split()),list("two times two is four".split()))
checkMagazine(list("give me one grand today night".split()),list("give one grand today".split()))
checkMagazine(list("one one one".split()),list("one one one one".split()))