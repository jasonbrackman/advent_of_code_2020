import helpers

DIR = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}


def parse(lines):
    return [(line[0], int(line[1:])) for line in lines]


def part01(values):

    current = (0, 0)
    directions = ['N', 'E', 'S', 'W']
    facing = 1

    for direction, units in values:
        if direction in DIR:
            p2x, p2y = DIR[direction]
            current = (current[0] + p2x * units, current[1] + p2y * units)
        elif direction == "F":
            p2x, p2y = DIR[directions[facing]]
            current = (current[0] + p2x * units, current[1] + p2y * units)
        elif direction in ("L", "R"):
            m = -1 if direction == "L" else 1
            u = int(units) // 90 * m
            facing = (facing + u) % 4
            # print("New Facing:", directions[facing])
        # print(current)

    return abs(current[0]) + abs(current[1])


def part02(values):
    current = (0, 0)
    waypoint = [-1, 10]
    directions = ['N', 'E', 'S', 'W']

    for direction, units in values:
        if direction in DIR:
            p2x, p2y = DIR[direction]
            waypoint = (waypoint[0] + p2x * units, waypoint[1] + p2y * units)
        elif direction == "F":
            p2x, p2y = waypoint
            current = (current[0] + p2x * units, current[1] + p2y * units)
        elif direction in ("L", "R"):
            old_a, old_b = waypoint

            ns = 0 if waypoint[0] < 0 else 2
            we = 3 if waypoint[1] < 0 else 1

            m = -1 if direction == "L" else 1
            u = int(units) // 90 * m
            p1 = directions[(ns + u) % 4]
            p2 = directions[(we + u) % 4]

            a, b = 0, 0

            for p, old in zip((p1, p2), (old_a, old_b)):
                if p in "E":
                    b = abs(old)
                elif p == "W":
                    b = old if old < 0 else old * -1
                elif p == "N":
                    a = old if old < 0 else old * -1
                elif p == "S":
                    a = abs(old)

            waypoint = (a, b)

    return abs(current[0]) + abs(current[1])


if __name__ == "__main__":
    lines = helpers.get_lines(r'./data/day_12.txt')
    values = parse(lines)
    assert part01(values) == 757
    assert part02(values) == 51249
