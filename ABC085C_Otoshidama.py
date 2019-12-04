n , y = map(int, input().split())

ans = '-1 -1 -1'
for a in range(n + 1):
    for b in range(n + 1):
        if 10000 * a + 5000 * b + (n - a - b) * 1000 == y and (n-a-b) >= 0:
            ans = '{} {} {}'.format(a, b, (n-a-b))
            break
    if ans != '-1 -1 -1':
        break

print(ans)