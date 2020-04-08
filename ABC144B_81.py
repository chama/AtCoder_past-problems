n = int(input())

kakezan = []
for i in range(1,10):
    for j in range(1,10):
        kakezan.append(i * j)

if n in kakezan:
    print('Yes')
    exit()

print('No')