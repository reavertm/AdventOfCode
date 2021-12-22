from array import *

def num_boards(boards):
    return int(len(boards) / 25)

def mark(boards, hitmask, b, n):
    for i in range(0, 5):
        for j in range(0, 5):
            if boards[b * 25 + i * 5 + j] == n:
                hitmask[b][i] |= (1 << (5 - 1 - j))

def is_bingo(hitmask, b):
    hit = 0b11111
    found = False
    for i in range(0, 5):
        row_mask = hitmask[b][i]
        if row_mask == 0b11111:
            found = True
            break
        hit &= row_mask
    if hit > 0:
        found = True
    return found

def sum_unmarked(boards, hitmask, b):
    sum = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if hitmask[b][i] & (1 << (5 - 1 - j)) == 0:
                sum += boards[b * 25 + i * 5 + j]
    return sum

with open('input', mode = 'rt') as f:
    numbers = array('i', (int(x) for x in f.readline().split(',')))
    boards = array('i', (int(x) for l in f for x in l.split())) # [board][row][col]
#    print(numbers)
#    print(boards)
    hitmask = [array('i', (0 for i in range(0, 5))) for b in range(0, num_boards(boards))] # [board][row]
    remaining = array('i', (b for b in range(0, num_boards(boards))))
    for n in numbers:
        idx = 0
        while idx < len(remaining):
            b = remaining[idx]
            mark(boards, hitmask, b, n)
            if is_bingo(hitmask, b):
#                print(f"found in board {b} at {n}")
                remaining.remove(b)
                idx -= 1
                if not remaining:
                    print(sum_unmarked(boards, hitmask, b) * n)
                    break
            idx += 1
        else:
            continue
        break
#    print(hitmask)
