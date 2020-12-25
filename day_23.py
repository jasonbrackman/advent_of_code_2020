import math
from collections import deque
from itertools import cycle

puzzle_input = "739862541"
puzzle_input_test = "389125467"


def circle(input_, times_to_run):
    c = [int(i) for i in input_]
    count = 0
    for _i in range(0, times_to_run):
        # print(f"ROUND {_i+1}")

        # print("Next_needle Start:", c[0], c)
        prefix = [c.pop(0)]
        next_needle = prefix[0]
        c = c + prefix

        collect = [c.pop(0),
                   c.pop(0),
                   c.pop(0)]
        # print("\tCOLLECT:", collect, c)
        # print("C", c)
        test = next_needle - 1
        test_index = None

        while test_index is None:
            if test >= min(c):
                if test in c:
                    test_index = c.index(test)
                elif test in prefix:
                    test_index = prefix.index(test)
                else:
                    test -= 1
            else:
                max_c = max(c)
                max_prefix = max(prefix)
                if max_c > max_prefix:
                    test_index = c.index(max_c)
                else:
                    test_index = prefix.index(max_prefix)

        # print("\tTest INDEX:", test_index, f"=> '{c[test_index]}'")
        # print(c[test_index])
        # print("Next Needle:", next_needle)
        c = c[0:test_index+1] + collect + c[test_index+1:]

        # print("RESULT:", c)
        count += 1

        if count % 1 == 0:
            print(c[0:20], c[-10:])
            # r = c.index(1_000_000)
            # print(r, c[r+1: ])
    return c


def part01():

    r = circle(puzzle_input, 100)
    s = r.index(1)
    for x in (r[s+1:] + r[0:s]):
        print(x, end='')


puzzle_input = puzzle_input_test
puzzle_input = [int(x) for x in puzzle_input]
puzzle_input = puzzle_input + [x for x in range(max(puzzle_input) + 1, 1_000_001)]
r = circle(puzzle_input, 1000)
s = r.index(1)
print(math.prod(r[s+1:s+3]))
