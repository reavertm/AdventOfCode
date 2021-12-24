SEGMENT_MASK = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

with open("input", mode="rt") as f:
    num_of_1_4_7_8 = 0;
    for s in f:
        s = s.rstrip().split(" | ")
        sig = s[0].split(" ")
        digit = s[1].split(" ")
        for d in digit:
            n = len(d)
            if n == 2 or n == 4 or n == 3 or n == 7:
                num_of_1_4_7_8 += 1
    print(num_of_1_4_7_8)
