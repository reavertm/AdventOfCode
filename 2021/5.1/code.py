def draw(grid, p0, p1):
    dx = p1[0] - p0[0]
    if dx:
        dx = int(dx/abs(dx))
    dy = p1[1] - p0[1]
    if dy:
        dy = int(dy/abs(dy))
    x = p0[0]
    y = p0[1]
    while True:
        grid[(x, y)] = grid.setdefault((x, y), 0) + 1
        if x == p1[0] and y == p1[1]:
            break
        x += dx
        y += dy

with open('input', mode = 'rt') as f:
    grid = dict()
    for l in f:
        beg, end = l.split(' -> ')
        p0 = [int(p) for p in beg.split(',')]
        p1 = [int(p) for p in end.split(',')]
        if p0[0] == p1[0] or p0[1] == p1[1]:
            draw(grid, p0, p1)
    print(grid)
    print(len([v for v in grid.values() if v >= 2]))
