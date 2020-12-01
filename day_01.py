import helpers


def part1(ints):
    """Find the two entries that sum to 2020; what do you get if you multiply them together?"""
    for i in ints:
        r = 2020 - i
        if r in ints:
            return i * r


def part2(ints):
    """what is the product of the three entries that sum to 2020?"""
    for i in ints:
        for ii in ints:
            for iii in ints:
                if i + ii + iii == 2020:
                    return i*ii*iii


def main():
    lines = helpers.get_lines(r"./data/day_01.txt")
    ints = [int(line) for line in lines]
    p1 = part1(ints)
    p2 = part2(ints)

    assert p1 == 935419
    assert p2 == 49880012


if __name__ == "__main__":
    main()