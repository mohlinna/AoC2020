byr = "byr"
iyr = "iyr"
eyr = "eyr"
hgt = "hgt"
hcl = "hcl"
ecl = "ecl"
pid = "pid"
cid = "cid"


def check_id(fields):
    return byr in fields and \
           iyr in fields and \
           eyr in fields and \
           hgt in fields and \
           hcl in fields and \
           ecl in fields and \
           pid in fields


def check_ids(inputs):
    count = 0
    total = 0
    fields = []
    for line in inputs:
        if not line.isspace():
            items = line.split()
            for item in items:
                fields.append(item[:3])
        else:
            if check_id(fields):
                count += 1
            del fields[:]
            total += 1
    if check_id(fields):
        count += 1
    print("Good passports:  {}  total:  {}".format(count, total))


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    check_ids(lines)
