n = int(input())
d = list(map(int,[input() for i in range(n)]))
print(len(list(set(d))))