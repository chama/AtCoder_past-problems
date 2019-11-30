a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
for i in reversed(range(a + 1)):
    for j in reversed(range(b + 1)):
        for k in reversed(range(c + 1)):
            if 500 * i + 100 * j + 50 * k == x:
                ans += 1

print(ans)