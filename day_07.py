import re
import helpers


BAG_INFO = re.compile(r'(\d+) (\w+ \w+)')


class Bag:
    def __init__(self, name, count=1):
        self.name: str = name.strip()
        self.count: int = count
        self.contains = list()

    def __str__(self):
        r = ""
        for c in self.contains:
            r += f"{c.name} - {c.count}, "
        return f"{self.name} - {self.count} => {r}"


def get_bags():
    bags = []
    lines = helpers.get_lines(r'./data/day_07.txt')
    for line in lines:
        name, *_ = line.split("bags")

        bag = Bag(name)
        for bag_info in BAG_INFO.findall(line):
            bag_count, bag_name = bag_info
            bag.contains.append(Bag(bag_name, int(bag_count)))
        bags.append(bag)

    return bags


def part01(bags):
    total = 0
    for bag in bags:
        visited = set()
        frontier = list(bag.contains)

        # shiny gold must be contained by another bag -- so skip the main attraction
        if bag.name == "shiny gold":
            continue

        while frontier:
            child = frontier.pop()
            if child.name not in visited:
                if child.name == "shiny gold":
                    total += 1
                    break
                else:
                    visited.add(child.name)

                    for b in bags:
                        if b.name == child.name:
                            frontier.extend(list(b.contains))

    return total


def part02(bags, start):
    total = 0
    parent = [bag for bag in bags if bag.name == start][0]
    for item in parent.contains:
        total += item.count
        total += sum(i.count for i in item.contains)
        total += part02(bags, item.name) * item.count
    return total


if __name__ == "__main__":
    bags = get_bags()

    assert part01(bags) == 112
    assert part02(bags, "shiny gold") == 6260



