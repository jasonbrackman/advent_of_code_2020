import math
from typing import Tuple

import helpers


def day_03(rules: Tuple) -> int:
    lines = helpers.get_lines(r"./data/day_03.txt")

    m = []
    for k, v in rules:
        # prime iterator each time
        forest = iter(lines)
        _ = next(forest)  # always skip header

        x = 0
        total = []
        for trees in forest:
            x += k

            # Skip lines if the rules expect it
            for _ in range(v - 1):
                trees = next(forest)

            total.append(trees[x % len(trees)] == "#")

        m.append((sum(total)))

    return math.prod(m)


def run():
    part1 = ((3, 1),)
    part2 = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
    assert day_03(part1) == 274
    assert day_03(part2) == 6050183040


if __name__ == "__main__":
    run()
