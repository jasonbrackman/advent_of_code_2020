def part01(groups):
    count = 0
    for group in groups:
        count += len([g for g in set(group) if g.isalpha()])
    return count


def part02(groups):
    count = 0
    for group in groups:
        user_count = len(group.split())
        count += len([item for item in set(group) if group.count(item) == user_count])

    return count


def run():
    with open(r"./data/day_06.txt") as f:
        groups = f.read().split("\n\n")
    assert part01(groups) == 6506
    assert part02(groups) == 3243


if __name__ == "__main__":

    run()
