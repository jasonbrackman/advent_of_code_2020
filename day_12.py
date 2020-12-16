import sys

import display
import helpers

DIR = {
    "N": helpers.Pos(-1, 0),
    "S": helpers.Pos(1, 0),
    "E": helpers.Pos(0, 1),
    "W": helpers.Pos(0, -1),
}


def parse(lines):
    return [(line[0], int(line[1:])) for line in lines]


def part01(values):

    current = helpers.Pos(0, 0)
    directions = ["N", "E", "S", "W"]
    facing = 1

    for direction, units in values:
        if direction in DIR:
            current += DIR[direction] * units
        elif direction == "F":
            current += DIR[directions[facing]] * units
        elif direction in ("L", "R"):
            m = -1 if direction == "L" else 1
            u = int(units) // 90 * m
            facing = (facing + u) % 4
            # print("New Facing:", directions[facing])
        # print(current)

    return current.manhattan_distance(helpers.Pos(0, 0))


def part02(values):
    for_display = {
        "positions": [],
        "waypoints": [],
    }
    current = helpers.Pos(0, 0)
    waypoint = helpers.Pos(-1, 10)
    directions = ["N", "E", "S", "W"]

    for direction, units in values:
        if direction in DIR:
            waypoint += DIR[direction] * units
        elif direction == "F":
            current += waypoint * units
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

            waypoint = helpers.Pos(a, b)

        for_display["positions"].append(current)
        for_display["waypoints"].append(waypoint)

    return current.manhattan_distance(helpers.Pos(0, 0)), for_display


def get_rows_col():
    rows = cols = 0
    row_min = sys.maxsize
    col_min = sys.maxsize
    for k, v in view.items():
        xs = [p.x for p in v]
        r = max(xs) - min(xs)
        if min(xs) < row_min:
            row_min = min(xs)
        if r > rows:
            rows = r

        ys = [p.y for p in v]
        r = max(ys) - min(ys)
        if min(ys) < col_min:
            col_min = min(ys)
        if r > cols:
            cols = r

    return rows, cols, helpers.Pos(row_min, col_min)


def visualize_day():
    scale_down = 300
    rows, cols, offset = get_rows_col()
    rows = rows // scale_down
    cols = cols // scale_down
    print(rows, cols)
    c = ['.'] * cols
    for i, (p, w) in enumerate(zip(view["positions"], view["waypoints"])):
        data = [c[:] for r in range(rows)]
        p1 = p - offset
        try:
            data[p1.x // scale_down][p1.y // scale_down] = "S"
            for stretch in range(30):
                w1 = p1 + (w * (20 + stretch))
                data[w1.x // scale_down][w1.y // scale_down] = "W"
            display.generic_out(data, {'.': 'black', 'S': 'white', 'W': 'red'}, 'day_12', i)
        except IndexError as e:
            print(e, p1, w1, i)
    imgs = display.load_images_starting_with("day_12")
    imgs[60].save(
        r"./images/day_12.gif",
        save_all=True,
        append_images=imgs[61:],
        optimize=True,
        duration=60,
        loop=0,
    )


if __name__ == "__main__":
    lines = helpers.get_lines(r"./data/day_12.txt")
    values = parse(lines)
    assert part01(values) == 757
    p2, view = part02(values)
    assert p2 == 51249

    # visualize_day()
