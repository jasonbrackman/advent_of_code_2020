import copy

import helpers
from collections import defaultdict, deque


def get_players(lines):
    players = defaultdict(deque)
    current_player = None
    for line in lines:
        if line:
            if "Player" in line:
                _, current_player = line.split()
                current_player = current_player.strip(":")
                current_player = int(current_player)
            else:
                players[current_player].append(int(line))
    return players


def part_01(players):
    p1 = players[1]
    p2 = players[2]

    while p1 and p2:
        c1 = p1.popleft()
        c2 = p2.popleft()
        if max(c1, c2) == c1:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    answer = 0
    for result in (p1, p2):
        for i, r in enumerate(reversed(result), 1):
            answer += r * i
    return answer


def part_02(players, game=0):
    # print(f"New Game {game} started!")
    deck_order = set()

    p1 = players[1]
    p2 = players[2]

    while p1 and p2:
        if (tuple(p1), tuple(p2)) in deck_order:
            # if game < 4:
            #     print(f"[{game}] Repeated Deck Encountered!", p1, p2)
            return p1, []
        deck_order.add((tuple(p1), tuple(p2)))
        c1 = p1.popleft()
        c2 = p2.popleft()

        if c1 <= len(p1) and c2 <= len(p2):
            d = {
                1: copy.deepcopy(deque(list(p1)[:c1])),
                2: copy.deepcopy(deque(list(p2)[:c2])),
            }
            result1, _ = part_02(d, game=game + 1)
            if result1:
                p1.extend([c1, c2])
            else:
                p2.extend([c2, c1])
        elif max(c1, c2) == c1:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    # print(f"Game {game} ended.")
    return p1, p2


def run():
    lines = helpers.get_lines(r"./data/day_22.txt")
    players = get_players(lines)
    p1 = part_01(players)
    assert p1 == 31809

    lines = helpers.get_lines(r"./data/day_22.txt")
    players = get_players(lines)
    p1, p2 = part_02(players)
    answer = 0
    for result in (p1, p2):
        for i, r in enumerate(reversed(result), 1):
            answer += r * i

    assert answer not in (33648, 33004)  # too high
    assert answer not in (32731,)  # too low
    assert answer == 32835


if __name__ == "__main__":
    run()
