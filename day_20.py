import math
import re
from typing import Dict, List
import display
import helpers


def rotate(array):
    final = [array[:]]

    array_length = len(array)
    for rotate_90 in range(3):
        r = [
            [final[-1][j][i] for j in range(array_length)] for i in range(array_length)
        ]
        r = [list(reversed(line)) for line in r]
        final.append(r)

    return final


def flip(array):
    v = [line for line in reversed(array)]
    h = [list(reversed(line)) for line in array]
    return [v, h]


def parse(lines):
    r = dict()
    key = None
    for line in lines:
        if not line:
            continue
        elif line.startswith("Tile"):
            key = line.split(" ")[1][:-1]
            r[key] = []
        else:
            r[key].append(list(line))
    return r


def is_match(arg1: List[List[str]], arg2: List[List[str]], direction=None) -> bool:
    u = arg1[0] == arg2[-1]
    d = arg2[0] == arg1[-1]
    r = all([l1[0] == l2[-1] for l2, l1 in zip(arg1, arg2)])
    l = all([r1[0] == r2[-1] for r1, r2 in zip(arg1, arg2)])

    if direction:

        if direction == "u" and u:
            return True
        if direction == "d" and d:
            return True
        if direction == "l" and l:
            return True
        if direction == "r" and r:
            return True

        return False

    return u or d or l or r


def dfs(array, keys):
    order = []
    for k in keys:
        if len(keys) == 0:
            return order
        for key in keys:
            if k == key:
                continue
            neighbours = get_variations(array, k)

            for neighbour in neighbours:
                placement = is_match(array[key], neighbour)
                if placement:
                    order.append((k, key))
    return order


def get_variations(image_dict, image_key: str):
    seen = set()
    all_ = [image_dict[image_key]]
    seen.add(str(image_dict[image_key]))
    assert len(image_dict[image_key]) == len(image_dict[image_key][0])
    assert len(image_dict[image_key]) > 0

    rotates = rotate(image_dict[image_key])
    for a in rotates:
        temp = str(a)
        if temp not in seen:
            seen.add(temp)
            all_.append(a)

    for x in all_[:]:
        flips = flip(x)
        for b in flips:
            temp = str(b)
            if temp not in seen:
                seen.add(temp)
                all_.append(b)

    return all_


def part_01(array):
    keys = list(array.keys())
    response = dfs(array, keys)
    total = get_image_graph(response)
    corners = [k for k, v in total.items() if len(v) == 2]

    return math.prod([int(i) for i in corners]), corners, total


def get_image_graph(response):
    total = dict()
    for resp in set(response):
        a, b = resp
        if a not in total:
            total[a] = set()
        if b not in total:
            total[b] = set()
        total[a].add(b)
        total[b].add(a)
    return total


def part_02(image_dict: Dict[str, List[List[str]]], corners, total):
    stack = []
    while len(stack) != 2:
        stack.clear()
        corner = corners.pop()
        stack = get_starting_stack(image_dict, total, corner)

    used_keys = [k[0] for k in stack]

    # get the header row
    while len(stack) < math.sqrt(len(image_dict)):
        key, image = stack[-1]
        # print(f"Searching for {key} in the neighbours of {total[key]}")
        for ii in total[key]:
            if ii in used_keys:
                continue
            for new in get_variations(image_dict, ii):
                new_result = is_match(image, new, direction="r")
                if new_result:
                    stack.append((ii, new))
                    used_keys.append(ii)
    temp_stack = stack[:]
    temp_used_keys = used_keys[:]

    while len(stack) != len(image_dict):
        stack = temp_stack[:]
        used_keys = temp_used_keys[:]

        for s in stack:
            key, image = s
            for ii in total[key]:

                if ii in used_keys:
                    continue

                for new in get_variations(image_dict, ii):
                    new_result = is_match(image, new, direction="d")
                    if new_result:
                        stack.append((ii, new))
                        used_keys.append(ii)
                        break

    squared = math.sqrt(len(image_dict))

    return get_image_stitched(stack, squared)


def print_stack(stack, squared):
    for i, s in enumerate(stack, 1):
        print(s[0], end=" ")
        if i % int(squared) == 0:
            print()
    print("=" * 50)

    count = 1
    for j in range(len(stack)):

        for i, s in enumerate(stack, 1):
            print("".join(s[1][j]), end=" ")
            if i % int(squared) == 0:
                print()
        if count % int(squared) == 0:
            print()
        count += 1


def get_starting_stack(image_dict: dict, total: dict, corner: str):
    stack = []
    key1, key2 = total[corner]

    image1 = image_dict[key1]
    image2 = image_dict[key2]

    for n in get_variations(image_dict, corner):

        result1 = is_match(n, image1, direction="r")
        result2 = is_match(n, image2, direction="r")

        if result1:
            for nn in get_variations(image_dict, key2):
                result_new = is_match(n, nn, direction="d")
                if result1 and result_new:
                    stack.append((corner, n))
                    stack.append((key1, image1))
                    break

        if result2:
            for nnn in get_variations(image_dict, key1):
                result_new = is_match(n, nnn, direction="d")
                if result2 and result_new:
                    stack.append((corner, n))
                    stack.append((key2, image2))
                    break

    return stack


def display_image(image, index):
    display.generic_out(
        image, {".": "white", "#": "green", "M": "red"}, "day_20", index
    )


m1 = re.compile(r".{18}#.")
m2 = re.compile(r"#.{4}##.{4}##.{4}###")
m3 = re.compile(r".#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}")


def get_monsters(r):
    # display_image(r, -1)
    displays = dict()

    targets = dict()
    waters = sum(v.count("#") for v in r)
    s = {"0": r}
    n = get_variations(s, "0")

    for index, lines in enumerate(n):
        displays[index] = []
        lines = list(lines)
        targets[index] = 0
        while lines:
            try:
                t1 = lines.pop(0)
                t2 = lines.pop(0)
                t3 = lines.pop(0)
            except IndexError:
                continue

            r1 = m1.findall("".join(t1))
            r2 = m2.findall("".join(t2))
            r3 = m3.findall("".join(t3))

            if r1 and r2 and r3:
                assert (
                    len(r1) == 1 or len(r2) == 1 or len(r3) == 1
                ), "Could be > 1 of the same monster on three lines."
                targets[index] += 1

            lines.insert(0, t3)
            lines.insert(0, t2)

    monsters = max(v for k, v in targets.items())
    for k, v in targets.items():
        if v == monsters:
            paint(n[k])
    return waters - (monsters * 15)


def paint(lines):
    stuff = []
    while lines:
        try:
            t1 = lines.pop(0)
            t2 = lines.pop(0)
            t3 = lines.pop(0)
        except IndexError:
            continue
        t1_s = "".join(t1)
        t2_s = "".join(t2)
        t3_s = "".join(t3)

        r1 = m1.findall(t1_s)
        r2 = m2.findall(t2_s)
        r3 = m3.findall(t3_s)

        if r1 and r2 and r3:
            start = m3.search("".join(t3)).start() - 1
            while True:
                start += 1
                s1 = re.subn(m1, "                  M ", t1_s[start : start + 20])
                s2 = re.subn(m2, "M    MM    MM    MMM", t2_s[start : start + 20])
                s3 = re.subn(m3, " M  M  M  M  M  M   ", t3_s[start : start + 20])
                if s1[1] >= 1 and s2[1] >= 1:
                    break
            stuff.append(t1_s[:start] + s1[0] + t1_s[start + 20 :])
            stuff.append(t2_s[:start] + s2[0] + t2_s[start + 20 :])
            stuff.append(t3_s[:start] + s3[0] + t3_s[start + 20 :])
        else:
            stuff.append(t1_s)
        lines.insert(0, t3)
        lines.insert(0, t2)
    display_image(stuff, 99)


def run():
    # part 01
    lines = helpers.get_lines(r"./data/day_20.txt")
    array = parse(lines)

    p1, corners, total = part_01(array)
    assert p1 == 23386616781851

    # part 02 (requires partial solution from p1)
    r = part_02(array, corners, total)
    p2 = get_monsters(r)
    assert p2 == 2376, f"Expected 2376, but received {p2}"


def get_image_stitched(stack, squared):

    squared = int(squared)
    imgs = [img for _, img in stack]

    transpose = []
    while imgs:
        img = [imgs.pop(0) for _ in range(int(squared))]
        line = []

        for index in range(1, len(img[0]) - 1):
            line += ["".join(t[index][1:-1]) for t in img]
            transpose.append("".join(line))
            line = []

    assert len(transpose) == len(
        transpose[0]
    ), f"Transpose: {len(transpose)} Internal:{len(transpose[0])}"
    return transpose


if __name__ == "__main__":
    run()
