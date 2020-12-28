import helpers
from collections import defaultdict


def parse(lines):
    foods = []
    for line in lines:
        ingredients, allergens = line.split("(contains ", 1)
        ingredients = set(ingredients.split())
        allergens = allergens.strip(")").split(", ")
        foods.append((allergens, ingredients))
    return foods


def get_inert_ingredients(allergen_db):
    remove_from_search = set()
    answers = defaultdict(list)
    while len(answers) != len(allergen_db):
        for k, v in allergen_db.items():
            new = [i for i in v if i not in remove_from_search]
            if len(new) == 1:
                remove_from_search.update(v)
                answers[k] = new

    return answers


def allergen_database(foods):
    allergen_db = defaultdict(set)
    for allergens, ingredients in foods:
        for a in allergens:
            if a not in allergen_db:
                allergen_db[a] = ingredients
            else:
                allergen_db[a] = allergen_db[a].intersection(ingredients)

    return allergen_db


def count_of_ingredients(foods):
    number_of = defaultdict(int)
    for allergens, ingredients in foods:
        for ingredient in ingredients:
            number_of[ingredient] += 1
    return number_of


def part_01(inert_ingredients, count_of):
    ignore = [v[0] for k, v in inert_ingredients.items()]
    answer = 0
    for k, v in count_of.items():
        if k not in ignore:
            answer += v
    return answer


def part_02(inert_ingredients):
    keys = list(sorted(inert_ingredients.keys()))
    solve = []
    for key in keys:
        solve.append(inert_ingredients[key][0])
    return ",".join(solve)


def run():
    lines = helpers.get_lines(r"./data/day_21.txt")
    foods = parse(lines)
    allergen_db = allergen_database(foods)
    inert_ingredients = get_inert_ingredients(allergen_db)
    count_of = count_of_ingredients(foods)
    p1 = part_01(inert_ingredients, count_of)
    assert p1 == 2614
    p2 = part_02(inert_ingredients)
    assert p2 == "qhvz,kbcpn,fzsl,mjzrj,bmj,mksmf,gptv,kgkrhg"


if __name__ == "__main__":
    run()
