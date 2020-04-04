n = int(input())
s = input() 

ans = 0
for i in range(1,n):
    x = list(set(s[:i]))
    y = list(set(s[i:]))
    if len(x) >= len(y):
        ans = max(ans, len(x) - len(list(set(x)- set(y))))
    else:
        ans = max(ans, len(y) - len(list(set(y)- set(x))))


print(ans)