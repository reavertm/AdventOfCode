class Node:
    def __init__(self):
        self.node = [None, None]
        self.visits = [0, 0]
    def add(self, b):
        if self.node[b] is None:
            self.node[b] = Node()
        self.visits[b] += 1
        return self.node[b]

def dump(node, level = 0):
    if node is None:
        return
    print('['.rjust(level * 2), end = '')
    print(f"{node.visits[0]},{node.visits[1]}")
    dump(node.node[0], level + 1)
    dump(node.node[1], level + 1)
    print(']'.rjust(level * 2))

with open('input', mode = 'rt') as f:
    num_bits = 0
    values_root = Node()
    n = 0
    for l in f:
        values = values_root
        if n == 0:
            num_bits = len(l) - 1
        for i in range(len(l) - 1):
            b = int(l[i])
            values = values.add(b)
        n += 1
    n /= 2
    #dump(values_root)
    oxygen_generator_rating = co2_scrubber_rating = 0
    most_common_bits_node = least_common_bits_node = values_root
    i = 0
    while i < num_bits:
        if most_common_bits_node is not None:
            most_common_bit = 1 if most_common_bits_node.node[1] and (most_common_bits_node.visits[1] >= most_common_bits_node.visits[0]) else 0
            if most_common_bit == 1:
                oxygen_generator_rating |= 1 << (num_bits - 1 - i)
            most_common_bits_node = most_common_bits_node.node[most_common_bit]
        if least_common_bits_node is not None:
            least_common_bit = 0 if least_common_bits_node.node[0] and (least_common_bits_node.visits[0] <= least_common_bits_node.visits[1] or not least_common_bits_node.node[1]) else 1
            if least_common_bit == 1:
                co2_scrubber_rating |= 1 << (num_bits - 1 - i)
            least_common_bits_node = least_common_bits_node.node[least_common_bit]
        i += 1
    print(oxygen_generator_rating * co2_scrubber_rating)
