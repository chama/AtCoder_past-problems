n,k = map(int,input().split())

q = n // k
mod = n % k

if mod <= abs(mod - k):
    print(mod)
    exit()
print(abs(mod-k))