import re

import helpers

pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


def part_01(policy: str) -> bool:
    """
    The policy indicates the lowest and highest number of times a given letter must appear for
    the password to be valid. For example:
    -- `1-3 a` means that the password must contain `a` at least 1 time and at most 3 times.
    """
    low, high, letter, password = re.search(pattern, policy).groups()
    return int(low) <= password.count(letter) <= int(high)


def part_02(policy: str) -> bool:
    """
    Each policy describes two positions in the password, where 1 means the first character,
    2 means the second character, and so on.  Only 1 index should contain the correct letter
    at the position indicated.
    """

    idx1, idx2, letter, password = re.search(pattern, policy).groups()

    # index is `1 based` rather than zero indexed, so all numbers are one index off in the positive
    test1 = password[int(idx1) - 1] == letter
    test2 = password[int(idx2) - 1] == letter

    return (test1 or test2) and test1 is not test2


def run():
    global line
    lines = helpers.get_lines(r"./data/day_02.txt")
    p1 = sum(part_01(line) for line in lines)
    assert p1 == 643
    p2 = sum(part_02(line) for line in lines)
    assert p2 == 388


if __name__ == "__main__":
    run()
