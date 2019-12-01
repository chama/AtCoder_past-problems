n, a, b = map(int, input().split())

ans = 0

for i in range(1, n+1):
    wa = 0
    i = str(i)
    for j in range(len(i)):
        wa += int(i[j])
    if a <= wa <= b:
        ans += int(i)

print(ans)

# ans = 0
# for i in range(n + 1):
#     if a <= sum(list(map(int,list(str(i))))) <=b:
#         ans += i