import math
n = int(input())
x = list(map(int, input().split()))

# print(sum(x)/len(x))
mean = math.floor(sum(x)/len(x))
mean2 = mean + 1
ans = 0
ans2 = 0
for i in x:
    ans += (i - mean) ** 2
    ans2 += (i - mean2) ** 2

if ans <= ans2:
    print(ans)
    exit()
else:
    print(ans2)
    exit()