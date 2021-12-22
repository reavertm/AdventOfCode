import functools

class window:
    values = []
    def full(self):
        return len(self.values) == 3
    def add(self, v):
        self.values.append(v)
        if len(self.values) > 3:
            self.values.pop(0)
    def sum(self):
        return functools.reduce((lambda a, b: a + b), self.values)

with open('input', mode = 'rt') as f:
    wnd = window()
    last_sum = None
    times = 0
    while True:
        l = f.readline()
        if not l:
            break
        wnd.add(int(l))
        if wnd.full():
            sum = wnd.sum()
            if last_sum is not None:
                if sum > last_sum:
                    times += 1
            last_sum = sum
    print(times)
