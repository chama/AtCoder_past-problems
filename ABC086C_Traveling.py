n = int(input())
ls = [[0,0,0]]
for x in range(n):
    tmp = list(map(int, input().split()))
    ls.append(tmp)

for i in range(len(ls)-1):
    t = ls[i+1][0] - ls[i][0]
    minkyori = abs(ls[i+1][1] - ls[i][1]) + abs(ls[i+1][2] - ls[i][2])
    if (t - minkyori) % 2 != 0 or (t - minkyori) < 0: #到着不可能,今回であればt=minkyori+2nなら到着できる
        print('No')
        exit()
print('Yes')
