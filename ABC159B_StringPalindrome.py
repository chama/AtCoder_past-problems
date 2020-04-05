s = input()
slist = []
for i in range(len(s)):
    slist.append(s[i])

def isKaibun(s): #s is list
    s2 = s[:]
    s2.reverse()
    if s == s2:
        return 1
    return 0

if isKaibun(slist) and isKaibun(slist[:(len(slist)-1)//2]) and isKaibun(slist[(len(slist)+3)//2 -  1:]):
    print('Yes')
    exit()
print('No')
