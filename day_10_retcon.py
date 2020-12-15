from functools import lru_cache

import helpers

ints = helpers.get_ints(r"./data/day_10.txt")
ints.append(max(ints) + 3)

d = [0, 0, 0]

current = 0
while current != max(ints):
    n = min([current + i for i in range(1, 4) if current + i in ints])
    d[n - current - 1] += 1
    current = n
print(d)

start, end = 0, max(ints)


@lru_cache
def recurse(start):
    if start == end:
        return 1
    count = 0
    for i in range(1, 4):
        if start + i in ints:
            count += recurse(start + i)
    return count


print(recurse(start))
