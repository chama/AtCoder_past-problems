k, n = map(int,input().split())
a = list(map(int,input().split()))

b = a
c = []
for i,v in enumerate(b):
    if i <= len(b)-2:
        c.append(b[i+1] - b[i])
    else: #最後は0番目との距離
        c.append(k-b[i]+b[0])

maxwidth = max(c)
print(k - maxwidth)