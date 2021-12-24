def total_fuel(crabs, pos, cache):
    if pos in cache:
        return cache[pos]
    fuel = 0
    for p, n in crabs.items():
        fuel += abs(p - pos) * n
    cache[pos] = fuel
    return fuel

with open('input', mode = 'rt') as f:
    crabs = dict()
    left_pos = right_pos = None
    for pos in f.read().rstrip().split(','):
        pos = int(pos)
        crabs[pos] = crabs.setdefault(pos, 0) + 1
        if left_pos is None or pos < left_pos:
            left_pos = pos
        if right_pos is None or pos > right_pos:
            right_pos = pos
    cache = dict()
    left_fuel = total_fuel(crabs, left_pos, cache)
    right_fuel = total_fuel(crabs, right_pos, cache)
    while True:
        mid_pos = int((left_pos + right_pos) / 2)
        mid_fuel = total_fuel(crabs, mid_pos, cache)
        print(f'[{left_pos}]={left_fuel} [{mid_pos}]={mid_fuel} [{right_pos}]={right_fuel}]')
        if abs(left_pos - right_pos) == 1:
            mid_fuel = min(left_fuel, right_fuel)
            break
        if mid_fuel < left_fuel and mid_fuel < right_fuel:
            if left_fuel < right_fuel:
                right_pos = mid_pos
                right_fuel = mid_fuel
            else:
                left_pos = mid_pos
                left_fuel = mid_fuel
        elif mid_fuel < left_fuel:
            left_pos = mid_pos
            left_fuel = mid_fuel
        elif mid_fuel < right_fuel:
            right_pos = mid_pos
            right_fuel = mid_fuel
    print(mid_fuel)
