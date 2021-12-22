with open('input', mode = 'rt') as f:
    forward = 0
    depth = 0
    aim = 0
    while True:
        l = f.readline()
        if not l:
            break
        direction = l.split(' ', 2)
        units = int(direction[1])
        if direction[0] == 'forward':
            forward += units
            depth += aim * units
        elif direction[0] == 'down':
            aim += units
        elif direction[0] == 'up':
            aim -= units
    print(forward * depth)
