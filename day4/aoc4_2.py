import re


def check_hgt(height):
    unit = height[-2:]
    num = height[:-2]
    if unit == 'cm':
        return 150 <= int(num) <= 193
    elif unit == 'in':
        return 59 <= int(num) <= 76
    return False


validations = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': check_hgt,
    'hcl': lambda x: re.search('^#[0-9a-f]', x),
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: re.search('^\d{9}$', x)
}


def check_id(passport):
    raw_fields = passport.replace('\n', ' ').split()
    field_dict = {}
    for field in raw_fields:
        field_dict[field[:3]] = field[4:]
    for category, check in validations.items():
        if category not in field_dict.keys() or not check(field_dict[category]):
            return False
    return True


def check_ids(passports):
    count = 0
    total = 0
    for passport in passports:
        if check_id(passport):
            count += 1
        total += 1
    print("Good passports:  {}  total:  {}".format(count, total))


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    groups = file1.read().split('\n\n')
    check_ids(groups)
