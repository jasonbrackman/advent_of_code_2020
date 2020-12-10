import helpers
from functools import lru_cache

NUMS = helpers.get_ints(r"./data/day_10.txt")
cache = dict()


def part01(nums):
    collection = {
        1: [],
        2: [],
        3: [],
    }

    start = 0
    end = max(nums)

    collection[3].append(end + 3)

    while start != end:
        value = next(start + i for i in range(1, 4) if start + i in nums)
        key = value - start
        collection[key].append(value)
        start = value

    return len(collection[1]) * len(collection[3])


@lru_cache
def part02(start):
    if start == max(NUMS):
        return 1

    count = 0
    for i in range(1, 4):
        if start + i not in NUMS:
            continue
        return_value = part02(start + i)
        count += return_value
    return count


if __name__ == "__main__":
    p1 = part01(NUMS)
    assert p1 == 2414

    p2 = part02(0)
    assert p2 == 21156911906816
