
import re

HCL_PATTERN = re.compile(r'[0-9A-Fa-f]{6}')
PID_PATTERN = re.compile(r'[0-9]{9}')

REQUIRED = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]


def process01(passport):
    c = True
    for req in REQUIRED:
        if c is False:
            continue

        if req not in passport.keys():
            c = False
    return c


def process02(passport):
    c = True
    for req in REQUIRED:
        if c is False:
            continue

        if req not in passport.keys():
            c = False

        elif req == "byr":
            if not 1920 <= int(passport[req]) <= 2002:
                c = False

        elif req == "iyr":
            if not 2010 <= int(passport[req]) <= 2020:
                c = False

        elif req == "eyr":
            if not 2020 <= int(passport[req]) <= 2030:
                c = False

        elif req == "hgt":
            if passport[req].endswith("cm"):
                v = int(passport[req][:-2])
                if not 150 <= v <= 193:
                    c = False

            elif passport[req].endswith("in"):
                v = int(passport[req][:-2])
                if not 59 <= v <= 76:
                    c = False
            else:
                c = False

        elif req == "hcl":
            if passport[req].startswith("#") is False:
                c = False

            else:
                v = passport[req][1:]
                if len(v) != 6 or HCL_PATTERN.search(v) is False:
                    c = False

        elif req == "ecl":
            if passport[req] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                c = False

        elif req == "pid":
            v = passport[req]
            if len(v) != 9 or PID_PATTERN.search(v) is False:
                c = False

    return c


def parse(func):
    total = list()

    with open(r'./data/day_04.txt') as f:
        passports = f.read().split("\n\n")

        for passport in passports:
            r = dict()

            items = passport.replace("\n", " ").split()
            for item in items:
                key, value = item.split(":")
                value = value.strip()
                r[key] = value

            c = func(r)

            total.append(c)
    return sum(total)


if __name__ == "__main__":
    assert parse(process01) == 228
    assert parse(process02) == 175
