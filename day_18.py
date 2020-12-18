import helpers
import math


def addition_takes_precedence(items):
    while "+" in items:
        index = items.index("+")
        arg1, arg2 = items[index - 1], items[index + 1]
        items.pop(index)
        items.pop(index)
        items[index - 1] = sum((int(arg1), int(arg2)))

    return in_brackets(items)


def in_brackets(items):
    arg2 = operator = None
    current = 0
    for i in items:
        if isinstance(i, int) or i.isdigit():
            if operator is None:
                current = int(i)
            else:
                arg2 = int(i)
        elif i == "+":
            operator = sum
        elif i == "*":
            operator = math.prod

        if current and arg2 and operator:
            r = operator((current, arg2))
            arg2 = None
            current = r

    return current


def do_math(lines, func_):
    """

    :param lines: puzzle input
    :param func_: if part01 -- pass in the 'in_brackets' func else 'addition_takes_precedence'
    :return:
    """
    total = 0
    for line in lines:
        # minor data cleanup
        items = [l for l in line if l != ' ']

        index = 0
        math_stack = dict()
        math_stack[index] = []
        for n in items:
            if n == "(":
                index += 1
                if index not in math_stack:
                    math_stack[index] = []
            elif n == ")":
                # store, clear, and then place the result
                r = func_(math_stack[index])
                math_stack[index].clear()
                index -= 1
                math_stack[index].append(r)
            else:
                math_stack[index].append(n)

        total += func_(math_stack[index])

    return total


if __name__ == "__main__":
    lines = helpers.get_lines(r"./data/day_18.txt")
    assert do_math(lines, in_brackets) == 98621258158412
    assert do_math(lines, addition_takes_precedence) == 241216538527890
