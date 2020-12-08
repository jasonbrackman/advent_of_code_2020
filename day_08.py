import helpers

def part01(lines):

    accumulator = 0
    seen = set()
    pointer = 0

    while True:
        if pointer in seen:
            return accumulator

        seen.add(pointer)
        arg, num = lines[pointer].split()
        num = int(num)

        if arg == "acc":
            accumulator += num
            pointer += 1
        elif arg == "jmp":
            pointer += num
        elif arg == "nop":
            pointer += 1


def part02(lines):
    jumps = [i for i, l in enumerate(lines) if l.startswith( "jmp")]

    for jump in jumps:
        accumulator = 0
        seen = set()
        pointer = 0
        while True:
            if pointer in seen:
                break

            seen.add(pointer)

            try:
                arg, num = ("nop", "0") if pointer == jump else lines[pointer].split()
                num = int(num)
            except IndexError:
                return accumulator

            if arg == "acc":
                accumulator += num
                pointer += 1
            elif arg == "jmp":
                pointer += num
            elif arg == "nop":
                pointer += 1


if __name__ == "__main__":
    lines = helpers.get_lines(r'./data/day_08.txt')
    assert part01(lines) == 1584
    assert part02(lines) == 920