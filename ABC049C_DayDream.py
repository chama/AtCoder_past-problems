s = input()
ans = 'NO'
t = ['dream', 'dreamer', 'erase', 'eraser']

t_t = []
for i in t:
    i = i[::-1]
    t_t.append(i)

s = s[::-1]

while s:
    if s[:len(t_t[0])] == t_t[0]:
        s = s[len(t_t[0]):]
    elif s[:len(t_t[1])] == t_t[1]:
        s = s[len(t_t[1]):]
    elif s[:len(t_t[2])] == t_t[2]:
        s = s[len(t_t[2]):]
    elif s[:len(t_t[3])] == t_t[3]:
        s = s[len(t_t[3]):]
    else:
        break
    if not s:
        ans = 'YES'

print(ans)