k = int(input())

lunlun = [i for i in range(1, 10)]

for i in lunlun:
    stri = str(i)
    if stri[-1] == '0':
        tmp = stri + '0' 
        lunlun.append(int(tmp))
        tmp = stri + '1'
        lunlun.append(int(tmp))
        if len(lunlun) >= k:
            print(lunlun[k-1])
            exit()
    elif stri[-1] == '9':
        tmp = stri + '8'
        lunlun.append(int(tmp))
        tmp = stri + '9'
        lunlun.append(int(tmp))
        if len(lunlun) >= k:
            print(lunlun[k-1])
            exit()
    else:
        tmp = stri + str(int(stri[-1]) - 1)
        lunlun.append(tmp)
        tmp = stri + str(int(stri[-1]))
        lunlun.append(tmp)
        tmp = stri + str(int(stri[-1]) + 1)
        lunlun.append(tmp)
        if len(lunlun) >= k:
            print(lunlun[k-1])
            exit()