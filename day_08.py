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

    def run(self, in_loop=None, debug=False):
        """Program will exit with an index error when complete."""

        self.__accumulator = 0
        self.idx = 0
        self.seen = {0: 1}

        while True:
            if in_loop:
                in_loop()

            try:
                arg, num = self.program[self.idx]
            except IndexError:
                return 0

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


def in_loop_hack():
    if m.seen[m.idx] > 1:
        raise HackException(f"Current Result: {m.k_neighbours}")


def part01(m):
    try:
        m.run(in_loop=in_loop_hack, debug=True)
    except HackException as e:
        # print(e.args[0])
        return m.k_neighbours


def part02(m):
    idxs = [i for i, l in enumerate(m.program) if l[0] == "jmp"]
    for idx in idxs:
        old = m.program[idx]
        try:
            m.program[idx] = ("nop", 0)
            m.run(in_loop=in_loop_hack, debug=True)
            return m.k_neighbours
        except HackException:
            pass
        m.program[idx] = old


def run():
    global m
    m = Machine(r"./data/day_08.txt")
    assert part01(m) == 1584
    assert part02(m) == 920


if __name__ == "__main__":
    run()
