import sys

import helpers

PATH = r"./data/day_13.txt"


def part01():
    timestamp, nums = parse()
    result = sys.maxsize
    id_ = None
    for n in nums:
        if n is None:
            continue

        test = 0
        while test < timestamp:
            test += n
        if test < result:
            result = test
            id_ = n

    return (result - timestamp) * id_


def part02():
    _, nums = parse()

    tumblers = {
        1: [1, 2],
    }

    results = []
    count = 100_000_000_000_000  # instructions for puzzle indicate it will be > than this number
    current = 1
    while True:
        count += abs(tumblers[current][1] - tumblers[current][0])
        for i, n in enumerate(nums):
            if n is None:
                continue
            r = (count + i) % n
            if r != 0:
                results.append(r)
                if len(results) >= current + 1:
                    if current + 1 in tumblers:
                        tumblers[current + 1].append(count)
                        current += 1
                    else:
                        tumblers[current + 1] = [count]
                # print(len(results), count, stuff, current)
                break
            results.append(r)

        if sum(results) == 0:
            return count

        results = []


def parse():
    lines = helpers.get_lines(PATH)
    timestamp, data = int(lines[0].strip()), lines[1].strip()
    nums = []
    for d in data.split(","):
        parsed = int(d) if d.isdigit() else None
        nums.append(parsed)
    return timestamp, nums


def run():
    assert part01() == 205
    assert part02() == 803025030761664


if __name__ == "__main__":
    run()
