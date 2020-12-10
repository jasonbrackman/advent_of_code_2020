import helpers
from typing import List

INPUT_PATH = r"./data/day_09.txt"
PREAMBLE = 25


def is_pair(block: List[int], i: int) -> bool:
    for b in block:
        test = i - b if i > b else b - i
        if test in block and b != test:
            return True
    return False


def part01(nums):
    current = 0
    while True:
        index = current + PREAMBLE + 1
        block = sorted(nums[current:index])
        i = nums[index]
        if not is_pair(block, i):
            return i
        current += 1


def part_02(needle):
    low, high = 0, 1
    while True:
        r = ints[low:high]
        s = sum(r)
        if s == needle:
            return sum((min(r), max(r)))
        else:
            if s > needle:
                low += 1
            else:
                high += 1


if __name__ == "__main__":
    ints = helpers.get_ints(INPUT_PATH)

    p1 = part01(ints)
    assert p1 == 22406676

    p2 = part_02(p1)
    assert p2 == 2942387
