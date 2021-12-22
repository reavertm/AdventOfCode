with open('input', mode = 'rt') as f:
    prev = None
    times = 0
    while True:
        l = f.readline()
        if not l:
            break
        curr = int(l)
        if prev is not None:
            if curr > prev:
                times += 1
        prev = curr
    print(times)
