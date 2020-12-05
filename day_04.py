
import re

HCL_PATTERN = re.compile(r'^#[0-9A-Fa-f]{6}$')
PID_PATTERN = re.compile(r'^\d{9}$')

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
    for req in REQUIRED:
        if req not in passport.keys():
            return False
    return True


def process02(passport):
    for req in REQUIRED:

        if req not in passport.keys():
            return False

        elif req == "byr":
            if not 1920 <= int(passport[req]) <= 2002:
                return False

        elif req == "iyr":
            if not 2010 <= int(passport[req]) <= 2020:
                return False

        elif req == "eyr":
            if not 2020 <= int(passport[req]) <= 2030:
                return False

        elif req == "hgt":
            if passport[req].endswith("cm"):
                v = int(passport[req][:-2])
                if not 150 <= v <= 193:
                    return False

            elif passport[req].endswith("in"):
                v = int(passport[req][:-2])
                if not 59 <= v <= 76:
                    return False
            else:
                return False

        elif req == "hcl":
            v = passport[req]
            if HCL_PATTERN.search(v) is None:
                return False

        elif req == "ecl":
            if passport[req] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                return False

        elif req == "pid":
            v = passport[req]
            if PID_PATTERN.search(v) is None:
                return False

    return True


def parse(func):
    checked_passports = list()

    with open(r'./data/day_04.txt') as f:
        passports = f.read().split("\n\n")

        for passport in passports:
            r = dict()

            items = passport.replace("\n", " ").split()
            for item in items:
                key, value = item.split(":")
                value = value.strip()
                r[key] = value

            is_valid = func(r)
            checked_passports.append(is_valid)

    return sum(checked_passports)


if __name__ == "__main__":
    assert parse(process01) == 228
    assert parse(process02) == 175
