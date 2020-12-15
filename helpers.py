import json

from typing import List, NamedTuple


def get_lines(path: str) -> List[str]:
    with open(path, "r") as text:
        return [line.strip() for line in text.readlines()]


def get_ints(path: str) -> List[int]:
    with open(path, "r") as text:
        return [int(i.strip()) for i in text.readlines()]


def load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)


class Pos(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __mul__(self, other: int):
        return Pos(self.x * other, self.y * other)

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y + other.y)
