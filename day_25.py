import helpers


MAGIC = 20201227


def get_loop_size(secret, public):
    value = 1
    for index in range(public):
        value = (value * secret) % MAGIC
        if value == public:
            return index + 1


def transform(number, loop):
    value = 1
    for index in range(loop):
        value = (value * number) % MAGIC
    return value


def run():
    # prep input
    lines = helpers.get_lines(r"./data/day_25.txt")
    card, door = lines
    card = int(card)
    door = int(door)

    # part1
    rcard = None
    rdoor = None
    for i in range(20):
        if rcard is None:
            rcard = get_loop_size(i, card)
        if rdoor is None:
            rdoor = get_loop_size(i, door)
    part01a = transform(card, rdoor)
    part01b = transform(door, rcard)
    assert part01a == part01b == 12181021


if __name__ == "__main__":
    run()
