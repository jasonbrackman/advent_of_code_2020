import math
import re

import helpers

p = re.compile(r"(\d+-\d+)")


def get_num_ranges(line):
    nums = []
    for ranges in p.findall(line):
        ints = [int(i) for i in ranges.split("-")]
        nums.extend(i for i in range(min(ints), max(ints) + 1))
    return nums


def part01(lines):
    valid_nums = []
    tickets = []
    start = False

    for line in lines:
        if not start and not line.startswith("nearby tickets:"):
            valid_nums += get_num_ranges(line)
        elif line.startswith("nearby tickets:"):
            start = True
        elif start:
            tickets.extend(
                [int(i) for i in line.split(",") if int(i) not in valid_nums]
            )

    return tickets


def part02(lines, invalid_tickets):
    categories, tickets = get_categories_and_tickets(invalid_tickets, lines)
    tickets_nearby = tickets["nearby"]
    tickets_yours = tickets["your"]

    discovered = dict()
    while len(discovered) != len(categories):
        for col_index in range(len(tickets_nearby[0])):  # enumerate(transposed):

            count = []
            test = [
                tickets_nearby[row_index][col_index]
                for row_index in range(len(tickets_nearby))
            ]
            for k, v in categories.items():
                if k not in discovered:
                    if all([t in v for t in test]):
                        count.append(k)

            if len(count) == 1:
                discovered[count[0]] = col_index

    return math.prod(
        tickets_yours[0][v] for k, v in discovered.items() if k.startswith("departure")
    )


def get_categories_and_tickets(invalid_tickets, lines):
    nearby_tickets = "nearby"
    your_tickets = "your"

    categories = dict()
    tickets = {
        nearby_tickets: [],
        your_tickets: [],
    }

    start = False
    for line in lines:
        if not start and not line.startswith((nearby_tickets, your_tickets)):
            nums = get_num_ranges(line)
            if nums:
                categories[line.split(":")[0]] = nums
        elif line.startswith(your_tickets):
            start = your_tickets
        elif line.startswith(nearby_tickets):
            start = nearby_tickets
        elif start:
            if len(line) == 0:
                start = False
            else:
                t = [int(i) for i in line.split(",") if int(i) not in invalid_tickets]
                if len(t) == 20:
                    tickets[start].append(list(t))

    return categories, tickets


if __name__ == "__main__":
    lines = helpers.get_lines(r"./data/day_16.txt")
    invalid_tickets = part01(lines)
    assert sum(invalid_tickets) == 23115

    found = part02(lines, invalid_tickets)
    assert found == 239727793813
