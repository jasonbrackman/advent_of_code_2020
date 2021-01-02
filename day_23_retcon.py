

def cups_in_place(rounds, curr, ll):
    max_input = len(ll) - 1
    for _ in range(rounds):
        curr = ll[curr]
        p1 = ll[curr]
        p2 = ll[p1]
        p3 = ll[p2]

        num = curr - 1 if curr != 1 else 0
        while num in (p1, p2, p3):
            num -= 1

        if num < 1:
            num = max_input
            while num in (p1, p2, p3):
                num -= 1

        ll[curr] = ll[p3]
        ll[p3] = ll[num]
        ll[num] = p1

    return ll


def part01(puzzle_input):

    ll = [i for i in range(0, len(puzzle_input)+1)]
    pi1 = [int(i) for i in puzzle_input]
    pi2 = pi1[:]
    pi2.append(pi2.pop(0))

    for idx, nxt in zip(pi1, pi2):
        ll[idx] = nxt

    curr = pi1[-1]
    cups_in_place(100, curr, ll)

    ans = ""
    r = ll[1]
    while r != 1:
        ans += str(r)
        r = ll[r]
    return int(ans)


def part02(puzzle_input):

    ll = [i for i in range(0, 1_000_001)]
    pi1 = [int(i) for i in puzzle_input] + [x for x in range(9 + 1, 1_000_001)]
    pi2 = pi1[:]
    pi2.append(pi2.pop(0))
    for idx, nxt in zip(pi1, pi2):
        ll[idx] = nxt

    curr = pi1[-1]
    ll = cups_in_place(10_000_000, curr, ll)

    a = ll[1]
    b = ll[a]
    return a * b


def run():
    puzzle_input = "739862541"
    assert part01(puzzle_input) == 94238657
    assert part02(puzzle_input) == 3072905352


if __name__ == "__main__":
    run()
    # import cProfile
    # cProfile.run("run()")