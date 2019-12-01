n = int(input())
an = list(map(int, input().split()))

alice = 0
bob = 0
an.sort()
an.reverse()
for i,v in enumerate(an):
    if i % 2 ==0:
        alice += v
    else:
        bob += v

print(alice - bob)
