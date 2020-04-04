x = int(input())
ans = 0

c500 = x // 500
ans += c500 * 1000
x -= c500 * 500
c50 = x // 5
ans += c50 * 5

print(ans)
