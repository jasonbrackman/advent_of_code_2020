import math
from typing import List
import helpers


def rotate(array):
    final = [array[:]]
    n_array = array[:]
    array_length = len(array)
    squared = int(math.sqrt(array_length))
    for x in range(squared):
        r = []
        for i in range(array_length):
            item = []
            for j in range(array_length):
                item.append(n_array[j][i])
            r.append(item)
        r = [list(reversed(line)) for line in r]

        final.append(r[:])
        n_array = r[:]

    return final


def flip(array):
    v = [line for line in reversed(array)]
    h = [list(reversed(line)) for line in array]
    h1 = [list(reversed(line)) for line in v]
    v1 = [line for line in reversed(h)]
    return [v, v1, h, h1]


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
        elif direction == "d" and d:
            return True
        elif direction == "l" and l:
            return True
        elif direction == "r" and r:
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
            neighbours = get_neighbours(array, k)

            for neighbour in neighbours:
                # print(key * 50)
                placement = is_match(array[key], neighbour)
                if placement:
                    order.append((k, key))
    return order


def get_neighbours(array, k: str):
    seen = set()
    all_ = [array[k]]
    seen.add(str(array[k]))

    rotates = rotate(array[k])
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


def part_02(array, corners, total):
    corner = str(corners[0])
    stack = get_starting_stack(array, total, corner)
    used_keys = [k[0] for k in stack]
    # get the header row
    while len(stack) < math.sqrt(len(array)):
        key, image = stack[-1]
        for ii in total[key]:
            if ii in used_keys:
                continue
            for new in get_neighbours(array, ii):
                new_result = is_match(image, new, direction='r')
                if new_result:
                    stack.append((ii, new))
                    used_keys.append(ii)

    for s in stack:
        key, image = s
        # print(key)
        for ii in total[key]:
            # print(ii)
            if ii in used_keys:
                continue
            for new in get_neighbours(array, ii):
                new_result = is_match(image, new, direction='d')
                if new_result:
                    stack.append((ii, new))
                    used_keys.append(ii)


    squared = math.sqrt(len(array))
    print_stack(stack, squared)


def print_stack(stack, squared):
    for i, s in enumerate(stack, 1):
        print(s[0], end=' ')
        if i % int(squared) == 0:
            print()
    print("=" * 50)

    count = 1
    for j in range(len(stack)):

        for i, s in enumerate(stack, 1):
            print(''.join(s[1][j]), end=' ')
            if i % int(squared) == 0:
                print()
        if count % int(squared) == 0:
            print()
        count += 1
        # print(count)
    # print("=" * 50)
    # ffinal = []
    # final = []
    #
    # for index, st in enumerate(stack, 1):
    #     temp_string = ""
    #     for i in range(0, len(stack)):
    #         temp_string += ''.join(st[1][i])
    #         # print(temp_string)
    #         # print("  " + temp_string[2:-2] + "  ")
    #         if len(temp_string) == len(stack[0][1]) * squared:
    #             final.append(temp_string)
    #             temp_string = ""
    #         if len(final) == len(stack[0][1]):
    #             ffinal.extend(final)
    #             final.clear()
    #
    # for f in ffinal:
    #     print(f)


def get_starting_stack(array: dict, total: dict, corner: str):

    stack = []
    for i in total[corner]:
        image = array[i]
        for n in get_neighbours(array, corner):
            result = is_match(n, image, direction='r')
            if result:
                stack.append((corner, n))
                stack.append((i, image))
                break

    if len(stack) != 2:
        print("Stack:", stack)
        raise
    return stack


def run():
    # part 01
    lines = helpers.get_lines(r"./data/day_20_test.txt")
    array = parse(lines)
    p1, corners, total = part_01(array)
    # assert p1 == 23386616781851

    part_02(array, corners, total)


if __name__ == "__main__":
    run()
