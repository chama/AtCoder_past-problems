n = int(input())
an = list(map(int, input().split())) #map object is iterable
ans = 0
flg = 0

while not flg :
    for i, v in enumerate(an):
        if v % 2 == 0:
            v = int(v / 2)
            an[i] = v
            if i == len(an)-1:
                ans +=1
        else:
            flg = 1
            break

print(ans)