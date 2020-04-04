n,m = map(int,input().split())
s=[]
c=[]
for i in range(m):
    si,ci = map(int,input().split())
    s.append(si)
    c.append(ci)


keta = 0
start = 0
if n == 1:
    keta = 10
    start = 0
elif n == 2:
    keta = 100
    start = 10
elif n == 3:
    keta = 1000
    start = 100
    
def chk_num(num):
    num = str(num)
    flg = 0
    for i,v in enumerate(s):
        if num[v-1] != str(c[i]):
            flg = 1
            break
    return flg
    

for i in range(start,keta):
    if chk_num(i) == 0:
        print(i)
        exit()

print(-1)