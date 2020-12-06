
def part01():
    count = 0
    for group in groups:
        count += len([g for g in set(group) if g.isalpha()])
    return count


def part02():
    count = 0
    for group in groups:
        items = list(group)
        lines = group.split()
        count += len([item for item in set(items) if items.count(item) == len(lines)])

    return count


if __name__ == "__main__":

    with open(r'./data/day_06.txt') as f:
        groups = f.read().split("\n\n")

    assert part01() == 6506
    assert part02() == 3243
