
import math
import helpers


def day_03(rules):
    m = []
    for k, v in rules:
        # prime iterator each time
        lines = iter(helpers.get_lines(r'./data/day_03.txt'))
        _ = next(lines)  # always skip header

        x = 0
        total = []
        for line in lines:
            x += k

            # Skip lines if the rules expect it
            for _ in range(v-1):
                line = next(lines)

            r = line[x % len(line)]
            total.append(r == '#')

        m.append((sum(total)))

    return math.prod(m)


if __name__ == "__main__":
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
