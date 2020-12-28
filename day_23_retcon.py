from __future__ import annotations


class LL:
    def __init__(self, r=None):
        self.cache = dict()
        if r is not None:
            self.add(r)
        self.curr = r

    def add(self, data):
        if self.curr is not None:
            self.cache[self.curr] = data
        self.cache[data] = None
        assert self.curr != data
        self.curr = data

    def peek(self, data):
        return self.cache[data]

    def next(self):
        r = self.cache[self.curr]
        self.curr = r
        return r

    def fuse(self, data):
        if self.cache[self.curr] is None:
            self.cache[self.curr] = data
        self.curr = data


def part01(puzzle_input):
    ll = LL()
    for i in puzzle_input:
        ll.add(int(i))
    ll.fuse(int(puzzle_input[0]))

    max_puzzle_input = max(puzzle_input)

    for _ in range(100):
        curr = ll.curr
        p1 = ll.next()
        p2 = ll.next()
        p3 = ll.next()

        num = curr - 1 if curr != 1 else max_puzzle_input
        while num == p1 or num == p2 or num == p3:
            num -= 1

        if num < 1:
            num = max_puzzle_input
            while num == p1 or num == p2 or num == p3:
                num -= 1

        ll.cache[curr] = ll.next()
        ll.cache[p3] = ll.peek(num)
        ll.cache[num] = p1

    ans = ""
    r = ll.peek(1)
    while r != 1:
        ans += f"{r}"
        # print(r, end='')
        r = ll.peek(r)
    return int(ans)


def part02(puzzle_input):
    ll = LL()
    for i in puzzle_input:
        ll.add(int(i))
    ll.fuse(int(puzzle_input[0]))

    max_puzzle_input = max(puzzle_input)

    for _ in range(10_000_000):
        curr = ll.curr
        p1 = ll.next()
        p2 = ll.next()
        p3 = ll.next()

        num = curr - 1 if curr != 1 else max_puzzle_input
        while num == p1 or num == p2 or num == p3:
            num -= 1

        if num < 1:
            num = max_puzzle_input
            while num == p1 or num == p2 or num == p3:
                num -= 1

        ll.cache[curr] = ll.next()
        ll.cache[p3] = ll.peek(num)
        ll.cache[num] = p1

    a = ll.peek(1)
    b = ll.peek(a)
    return a * b


def run():
    puzzle_input_test = "389125467"
    puzzle_input = "739862541"
    puzzle_input = puzzle_input
    pi1 = [int(i) for i in puzzle_input]
    pi2 = [int(i) for i in puzzle_input] + [x for x in range(9 + 1, 1_000_001)]
    assert part01(pi1) == 94238657
    assert part02(pi2) == 3072905352


if __name__ == "__main__":
    run()
