from typing import List


def get_lines(path: str) -> List[str]:
    with open(path, "r") as text:
        return [line.strip() for line in text.readlines()]


def get_ints(path: str) -> List[int]:
    with open(path, "r") as text:
        return [int(i.strip()) for i in text.readlines()]
