with open('input', mode = 'rt') as f:
    ones = []
    n = 0
    while True:
        l = f.readline()
        if not l:
            break
        for i in range(len(l) - 1):
            v = int(l[i])
            if len(ones) == len(l) - 1:
                ones[i] += v
            else:
                ones.append(v)
        n += 1
    n /= 2
    gamma_rate = 0
    for i in range(len(ones)):
        if ones[i] == n:
            print("equal number at pos " + str(i))
        if ones[i] > n:
            gamma_rate |= 1 << (len(ones) - 1 - i)
    epsilon_rate = ~gamma_rate & ((1 << len(ones)) - 1)
    print(gamma_rate * epsilon_rate)
