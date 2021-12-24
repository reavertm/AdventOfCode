from array import *

with open('input', mode = 'rt') as f:
    fishes = array('i', (int(x) for x in f.read().split(',')))
    n = 80
    while n > 0:
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] -= 1
        n -= 1
    print(len(fishes))
