def aoc2():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    good_pws = 0
    for line in Lines:
        splits = line.split()
        nums = splits[0].split('-')
        pos1 = int(nums[0])
        pos2 = int(nums[1])
        letter = splits[1][0]
        password = splits[2]
        if (password[pos1-1] == letter) != (password[pos2-1] == letter):
            good_pws += 1
    print("Good passwords:  {}".format(good_pws))

if __name__ == '__main__':
    aoc2()
