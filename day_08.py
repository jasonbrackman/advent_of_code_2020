import helpers


class HackException(Exception):
    pass


class Machine(object):
    def __init__(self, path):
        self.__accumulator = 0
        self.idx = 0
        self.program = self.load(path)
        self.seen = {0: 1}

    @property
    def result(self):
        return self.__accumulator

    def run(self, preparse=None, debug=False):
        """Program will exit with an index error when complete."""

        self.__accumulator = 0
        self.idx = 0
        self.seen = {0: 1}

        while True:
            if preparse:
                preparse()

            arg, num = self.program[self.idx]

            if arg == "acc":
                self.__accumulator += num
                self.idx += 1
            elif arg == "jmp":
                self.idx += num
            elif arg == "nop":
                self.idx += 1

            if debug:
                self.debug(arg, num)

    @staticmethod
    def load(path):
        compiled = []

        lines = helpers.get_lines(path)
        for line in lines:
            arg, num = line.split()
            num = int(num)
            compiled.append((arg, num))

        return compiled

    def debug(self, arg, num, silent=True):
        if self.idx not in self.seen:
            self.seen[self.idx] = 0
        self.seen[self.idx] += 1

        if not silent:
            print(
                f"{arg:<3} {num:<5} | ({self.seen[self.idx]:>3}) {self.idx:<5} {self.__accumulator:<5}"
            )


# def part01(lines):
#
#     accumulator = 0
#     seen = set()
#     pointer = 0
#
#     while True:
#         if pointer in seen:
#             return accumulator
#
#         seen.add(pointer)
#         arg, num = lines[pointer].split()
#         num = int(num)
#
#         if arg == "acc":
#             accumulator += num
#             pointer += 1
#         elif arg == "jmp":
#             pointer += num
#         elif arg == "nop":
#             pointer += 1
#
#
# def part02(lines):
#     jumps = [i for i, l in enumerate(lines) if l.startswith( "jmp")]
#
#     for jump in jumps:
#         accumulator = 0
#         seen = set()
#         pointer = 0
#         while True:
#             if pointer in seen:
#                 break
#
#             seen.add(pointer)
#
#             try:
#                 arg, num = ("nop", "0") if pointer == jump else lines[pointer].split()
#                 num = int(num)
#             except IndexError:
#                 return accumulator
#
#             if arg == "acc":
#                 accumulator += num
#                 pointer += 1
#             elif arg == "jmp":
#                 pointer += num
#             elif arg == "nop":
#                 pointer += 1
#


def hack01():
    if m.seen[m.idx] > 1:
        raise HackException(m.result)


if __name__ == "__main__":
    lines = helpers.get_lines(r"./data/day_08.txt")

    m = Machine(r"./data/day_08.txt")

    # Part01
    try:
        m.run(preparse=hack01, debug=True)
    except HackException as e:
        print(e.args[0])

    # part 02
    idxs = [i for i, l in enumerate(m.program) if l[0] == "jmp"]
    for idx in idxs:
        print(idx)
        old = m.program[idx]
        try:
            m.program[idx] = ("nop", 0)
            m.run(preparse=hack01, debug=True)
        except IndexError:
            print("Part2:", m.result)
        except HackException as e:
            pass
        m.program[idx] = old

    assert part01(lines) == 1584
    assert part02(lines) == 920
