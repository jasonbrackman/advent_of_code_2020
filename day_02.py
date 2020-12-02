import helpers
from collections import Counter


def part_01(policy: str) -> bool:
    """
    The password policy indicates the lowest and highest number of times a given letter
    must appear for the password to be valid.
    For example,
        1-3 a means that the password must contain a at least 1 time and at most 3 times.
    """
    a, b, c = policy.split()
    low, high = [int(i) for i in a.split("-")]
    b = b.strip(":")
    count = Counter(c)[b]
    return low <= count <= high


def part_02(policy: str) -> bool:
    """
    Each policy actually describes two positions in the password, where 1 means the
    first character, 2 means the second character, and so on.  Only 1 index should
    contain the correct letter at the position indicated.
    :param policy:
    :return: bool
    """
    a, b, c = policy.split()

    # Note: index is `1 based`
    index1, index2 = [int(i)-1 for i in a.split("-")]

    b = b.strip(":")
    test1 = c[index1] == b
    test2 = c[index2] == b

    return (test1 or test2) and test1 is not test2


if __name__ == "__main__":
    lines = helpers.get_lines(r'./data/day_02.txt')

    p1 = sum(part_01(line) for line in lines)
    assert p1 == 643

    p2 = sum(part_02(line) for line in lines)
    assert p2 == 388
