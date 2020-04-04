import math
def combinations_count(n,r):
    if n - r < 0:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    

n,m = map(int,input().split())

s = n + m
print(combinations_count(s,2) - (combinations_count(n,1)*combinations_count(m,1)))