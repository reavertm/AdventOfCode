with open('input', mode = 'rt') as f:
    forward = 0
    depth = 0
    while True:
        l = f.readline()
        if not l:
            break
        direction = l.split(' ', 2)
        if direction[0] == 'forward':
            forward += int(direction[1])
        elif direction[0] == 'down':
            depth += int(direction[1])
        elif direction[0] == 'up':
            depth -= int(direction[1])
    print(forward * depth)
