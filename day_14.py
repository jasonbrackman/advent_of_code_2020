import re
from itertools import combinations

import helpers

p = re.compile(r"mem.(\d+). = (\d+)")


def part01(lines):
    collection = dict()
    # current_value = None
    current_mask = None
    for line in lines:
        if line.startswith("mask"):
            current_mask = list(line.split()[2])

        if line.startswith("mem"):
            s = p.search(line)
            mem, val = [int(i) for i in s.groups()]
            val = list(str(bin(val))[2:])
            current_value = collection.get(mem, ["0"] * 36)

            val = ["0"] * (36 - len(val)) + val

            r = []
            for old, msk, new in zip(
                reversed(current_value), reversed(current_mask), reversed(val)
            ):
                if msk == "X":
                    r.append(new)
                elif msk == "1":
                    r.append("1")
                elif msk == "0":
                    r.append("0")
            r.reverse()
            collection[mem] = r

    return sum(int("".join(v), 2) for k, v in collection.items())


def part02(lines):
    collection = dict()
    current_mask = None
    for line in lines:
        if line.startswith("mask"):
            current_mask = list(line.split()[2])

        if line.startswith("mem"):
            s = p.search(line)
            mem, val = [int(i) for i in s.groups()]

            mem = list(str(bin(mem))[2:])
            mem = ["0"] * (36 - len(mem)) + mem

            val = list(str(bin(val))[2:])
            val = ["0"] * (36 - len(val)) + val

            r = []
            for msk, new in zip(reversed(current_mask), reversed(mem)):
                if msk == "X":
                    r.append("X")
                elif msk == "1":
                    r.append("1")
                elif msk == "0":
                    r.append(new)
            r.reverse()

            for perm in get_permutations(r):
                collection[int("".join(perm), 2)] = val

    return sum(int("".join(v), 2) for k, v in collection.items())


def get_permutations(items):
    perms = []

    num = items.count("X")
    com = combinations(["0", "1"] * num, num)
    for c in set(com):

        count = 0
        new = []
        for item in items:
            if item == "X":
                new.append(c[count])
                count += 1
            else:
                new.append(item)
        perms.append(new)

    return perms


def run():
    lines = iter(helpers.get_lines(r"./data/day_14.txt"))
    assert part01(lines) == 12135523360904
    lines = iter(helpers.get_lines(r"./data/day_14.txt"))
    assert part02(lines) == 2741969047858


if __name__ == "__main__":
    run()
