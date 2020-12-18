import itertools
import math
import re

import helpers

from typing import Dict, List, Tuple

p = re.compile(r"(\d+-\d+)")

NEARBY_TICKETS = "nearby"
YOUR_TICKETS = "your"


def get_num_ranges(line: str) -> List[int]:
    """Take in a string contaning N patterns of a 'number1'-'number2' and return all numbers
    in the range and inclusive of the max numbers."""

    nums = []
    for ranges in p.findall(line):
        ints = [int(i) for i in ranges.split("-")]
        nums.extend(i for i in range(min(ints), max(ints) + 1))
    return nums


def part01(lines: List[str]) -> List[int]:
    """Get invalid tickets"""
    valid_nums = []
    tickets = []
    start = False

    for line in lines:
        if not start and not line.startswith(NEARBY_TICKETS):
            valid_nums += get_num_ranges(line)
        elif line.startswith(NEARBY_TICKETS):
            start = True
        elif start:
            tickets.extend(
                [int(i) for i in line.split(",") if int(i) not in valid_nums]
            )

    return tickets


def part02(lines: List[str], invalid_tickets: List[int]) -> int:
    categories, tickets = get_categories_and_tickets(invalid_tickets, lines)
    tickets_nearby = tickets[NEARBY_TICKETS]
    tickets_yours = tickets[YOUR_TICKETS]

    discovered = dict()
    while len(discovered) != len(categories):
        """Require some sleuthing to find out which lines can only exist in one category then eliminate
        the category from subsequent searches till all categories are associated with an index. The 
        assumption here is that there IS a solution.  Otherwise the loop will continue forever."""
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


def get_categories_and_tickets(
    invalid_tickets: List[int], lines: List[str]
) -> Tuple[Dict, Dict]:

    categories = dict()
    tickets = {
        NEARBY_TICKETS: [],
        YOUR_TICKETS: [],
    }

    key = None
    for line in lines:
        if not key and not line.startswith((NEARBY_TICKETS, YOUR_TICKETS)):
            nums = get_num_ranges(line)
            if nums:
                categories[line.split(":")[0]] = nums
        elif line.startswith(YOUR_TICKETS):
            key = YOUR_TICKETS
        elif line.startswith(NEARBY_TICKETS):
            key = NEARBY_TICKETS
        elif key:
            if len(line) == 0:
                key = None
            else:
                t = [int(i) for i in line.split(",") if int(i) not in invalid_tickets]
                if len(t) == 20:
                    tickets[key].append(list(t))

    return categories, tickets


def parse_lines(lines):
    data = dict()
    current_key = None
    for line in lines:
        if line:
            if line[0].isalpha():
                current_key, nums = line.split(":")
                data[current_key] = get_num_ranges(line)
            elif line[0].isdigit():
                data[current_key].append([int(i) for i in line.split(",")])
    return data


if __name__ == "__main__":
    ll = helpers.get_lines(r"./data/day_16.txt")

    data = parse_lines(ll)
    ranges = [v for k, v in data.items() if "ticket" not in k]
    ranges_flat = set(itertools.chain.from_iterable(ranges))
    p1 = [r for row in data["nearby tickets"] for r in row if r not in ranges_flat]
    assert sum(p1) == 23115

    it = part01(ll)
    assert sum(it) == 23115

    found = part02(ll, it)
    assert found == 239727793813
