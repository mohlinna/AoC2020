def tree_check(landscape):
    pattern_width = len(landscape[0].strip())
    position = 0
    count = 0
    for line in landscape:
        if '#' == line[position % pattern_width]:
            count += 1
        position += 3
    return count


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    trees = tree_check(lines)
    print("{} trees encountered".format(trees))
