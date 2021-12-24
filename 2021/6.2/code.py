with open('input', mode = 'rt') as f:
    fishes = [0 for age in range(0, 8 + 1)]
    for x in f.read().split(','):
        fishes[int(x)] += 1
    age_offset = 0
    while age_offset < 256:
        a = (6 + age_offset + 1) % len(fishes)
        b = (0 + age_offset) % len(fishes)
        fishes[a] += fishes[b]
        age_offset += 1
        print(f'Day {abs(age_offset)}:')
        for i in range(0, len(fishes)):
            print(repr(fishes[(i + age_offset) % len(fishes)]).rjust(13), end='')
        print()
    print(sum(fishes))

# day 0 offset 0
# [0][1][2][3][4][5][6][7][8]
#     1  1  2  1

# day 1 offset -1
# [0][1][2][3][4][5][6][7][8]
#  1  1  2  1

# day 2 offset -2
# [0][1][2][3][4][5][6][7][8]
#  1  2  1           1     1

# day 3 offset -3
# [0][1][2][3][4][5][6][7][8]
#  2  1           1  1  1  1

# day 4 offset -4
# [0][1][2][3][4][5][6][7][8]
#  1           1  1  3  1  2
