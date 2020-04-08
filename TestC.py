a1, a2, a3 = map(int, input().split())

n = a1 + a2 + a3

if a1 == a2 == a3:
    print(1)
    exit()

num = []
for i in range(1,n+1):
    num.append(i)
t1 = []
t2=[]
t3=[]
for i in range(a1):
    t1.append(0)
for i in range(a2):
    t2.append(0)
for i in range(a3):
    t3.append(0)

tall = []
tall.append(a1)
tall.append(a2)
tall.append(a3)
cnt = 0
for i in tall[0]:
    for x in range(n):
        tall[0][i] = x
        for j in tall[1]:
            for y in range(n):
                tall[1][j] = y
                for k in tall[2]:
                    for z in range(n):
                        tall[2][k] = z
                        print(tall)