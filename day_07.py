import re
import helpers
from typing import Dict


BAG_INFO = re.compile(r"(\d+) (\w+ \w+)")


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


def get_bags() -> Dict[str, Bag]:
    bags = dict()
    lines = helpers.get_lines(r"./data/day_07.txt")
    for line in lines:
        name, *_ = line.split("bags")

        bag = Bag(name)
        for bag_info in BAG_INFO.findall(line):
            bag_count, bag_name = bag_info
            bag.contains.append(Bag(bag_name, int(bag_count)))
        bags[bag.name] = bag

    return bags


def part01(bags: Dict[str, Bag]) -> int:
    total = 0
    for name, bag in bags.items():
        visited = set("shiny gold")
        frontier = list(bag.contains)

        while frontier:
            child = frontier.pop()
            if child.name not in visited:
                if child.name == "shiny gold":
                    total += 1
                    break
                else:
                    visited.add(child.name)
                    frontier.extend(list(bags[child.name].contains))
    return total


def part02(bags: Dict[str, Bag], start: str) -> int:
    total = 0
    parent = bags[start]
    for item in parent.contains:
        total += item.count
        total += sum(i.count for i in item.contains)
        total += part02(bags, item.name) * item.count
    return total


if __name__ == "__main__":
    bags = get_bags()
    assert part01(bags) == 112
    assert part02(bags, "shiny gold") == 6260
