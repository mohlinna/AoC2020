def aoc2():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    good_pws = 0
    for line in Lines:
        splits = line.split()
        nums = splits[0].split('-')
        min = int(nums[0])
        max = int(nums[1])
        letter = splits[1][0]
        password = splits[2]
        counts = password.count(letter)
        if counts >= min and counts <= max:
            good_pws += 1
    print("Good passwords:  {}".format(good_pws))

if __name__ == '__main__':
    aoc2()
