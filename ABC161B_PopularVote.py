n,m = map(int,input().split())
a = list(map(int,input().split()))

s = sum(a)
chk =s * 1/(4*m)
x = sorted(a, reverse=True)
if x[m-1] < chk:
    print('No')
    exit()

print('Yes')