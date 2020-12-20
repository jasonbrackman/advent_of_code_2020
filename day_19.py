import helpers
from collections import deque


def parse_values(values):
    r = dict()
    for idx, val in enumerate(values.split("|")):
        r[idx] = list(val.strip(" \"").split())
    return r


def parse_rules(lines):
    rules = dict()
    messages = list()
    for line in lines:
        if not line:
            continue
        elif line[0].isdigit():
            key, values = line.split(":")
            rules[key] = parse_values(values)
        else:
            messages.append(line)
    return rules, messages


def bfs(rules, message):
    q = deque([(message, ['0'])])
    while q:
        message, keys = q.popleft()
        if not message and not keys:
            return True
        elif not message or not keys:
            continue

        rule, keys = rules[keys[0]], keys[1:]
        for k, v in rule.items():
            v_length = len([i for i in v if i.isalpha()])
            if v_length == 1:
                if message[0] == v[0]:
                    q.append((message[1:], keys))
                    # print(message, v[0])
                    continue
            else:
                # Backtrack and try with an alternative option if one is present.
                q.append((message, v + keys))
    return False


def run():
    # Part1
    lines = helpers.get_lines(r"./data/day_19.txt")
    rules, messages = parse_rules(lines)
    total = sum([bfs(rules, message) for message in messages])
    assert total == 124

    # Part2
    lines = helpers.get_lines(r"./data/day_19_part2.txt")
    rules, messages = parse_rules(lines)
    total = sum([bfs(rules, message) for message in messages])
    assert total == 228


if __name__ == "__main__":
    run()
