import math
a,b = map(int,input().split())

ans = 0
for i in range(1, 1251):
    if (math.floor(i*0.08) == a) and (math.floor(i*0.1) == b): 
        print(i)
        exit()
    else:
        ans+=1

if ans == 1250:
    print("-1")