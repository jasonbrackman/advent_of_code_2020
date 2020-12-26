import helpers

SUBJECT = 7
MAGIC = 20201227


def get_loop_size(public):
    value = 1
    for index in range(public):
        value = (value * SUBJECT) % MAGIC
        if value == public:
            return index + 1


def transform(number, loop):
    value = 1
    for index in range(loop):
        value = (value * number) % MAGIC
    return value


def run():
    lines = helpers.get_ints(r"./data/day_25.txt")
    card, door = lines

    rcard = get_loop_size(card)
    rdoor = get_loop_size(door)

    part01a = transform(card, rdoor)
    part01b = transform(door, rcard)
    assert part01a == part01b == 12181021


if __name__ == "__main__":
    run()
