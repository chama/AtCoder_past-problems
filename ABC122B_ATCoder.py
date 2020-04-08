s = list(input())
n = len(s)

def atcg(s):
    slength = len(s)
    cnt = 0
    for i in range(slength):
        if s[i] == 'A' or s[i] == 'T' or s[i] == 'C' or s[i] == 'G':
            cnt +=1
        else:
            break
    return cnt

ans = []
for i in range(n):
    ans.append(atcg(s[i:]))


print(max(ans))