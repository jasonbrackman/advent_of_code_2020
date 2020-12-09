import helpers

INPUT_PATH = r"./data/day_09.txt"
PREAMBLE = 25


def parse_input():
    lines = helpers.get_lines(INPUT_PATH)
    return [int(i.strip()) for i in lines]


def is_pair(block, next):
    for b in block:
        test = next - b if next > b else b - next
        if test in block and b != test:
            return True
    return False


def part01(nums):
    current = 0
    while True:
        index = current + PREAMBLE + 1
        block = sorted(nums[current:index])
        next = nums[index]
        if not is_pair(block, next):
            return next
        current += 1


def part_02(needle):
    low, high = 0, 1
    while True:
        r = nums[low:high]
        test = sum(r)
        if test == needle:
            return sum((min(r), max(r)))
        else:
            if test > needle:
                low += 1
            else:
                high += 1


if __name__ == "__main__":
    nums = parse_input()
    p1 = part01(nums)
    p2 = part_02(p1)

    assert p1 == 22406676
    assert p2 == 2942387
