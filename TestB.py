n = int(input())
s = []
for i in range(n):
    x,c = input().split()
    x = int(x)
    s.append([x,c])

r = []
b = []
for i in range(len(s)):
    if s[i][1] == 'R':
        r.append(s[i][0])
    else:
        b.append(s[i][0])

r.sort()
b.sort()

for i in r:
    print(i)
for i in b:
    print(i)