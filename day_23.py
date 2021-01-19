from __future__ import annotations

from typing import NamedTuple, Optional

puzzle_input = "739862541"
puzzle_input_test = "389125467"


def circle(input_, times_to_run):
    c = [int(i) for i in input_]
    count = 0
    for _i in range(0, times_to_run):
        prefix = [c.pop(0)]
        next_needle = prefix[0]
        c = c + prefix

        collect = [c.pop(0), c.pop(0), c.pop(0)]

        test = next_needle - 1
        test_index = None

        while test_index is None:
            if test >= min(c):
                if test in c:
                    test_index = c.index(test)  # very expensive
                else:
                    test -= 1
            else:
                max_c = max(c)
                max_prefix = max(prefix)
                if max_c > max_prefix:
                    test_index = c.index(max_c)
                else:
                    test_index = prefix.index(max_prefix)

        c = c[0 : test_index + 1] + collect + c[test_index + 1 :]
        count += 1

    return c


def part01():

    r = circle(puzzle_input, 100)
    r = list(r)
    s = r.index(1)
    for x in r[s + 1 :] + r[0:s]:
        print(x, end="")


import cProfile

cProfile.run("part01()")
# part01()

# puzzle_input = puzzle_input_test
# puzzle_input = [int(x) for x in puzzle_input]
# puzzle_input = puzzle_input + [x for x in range(max(puzzle_input) + 1, 1_000_001)]
# r = circle2(puzzle_input, 10_000_000)
# r = list(r)
# s = r.index(1)
# print("=*=" * 20)
# print(r[s+1:s+3])
# print(math.prod(r[s+1:s+3]))
