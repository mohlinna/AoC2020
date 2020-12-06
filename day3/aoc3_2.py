def tree_check(landscape, right_speed):
    pattern_width = len(landscape[0].strip())
    position = 0
    count = 0
    for line in landscape:
        if '#' == line[position % pattern_width]:
            count += 1
        position += right_speed
    return count


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    trees11 = tree_check(lines, 1)
    trees13 = tree_check(lines, 3)
    trees15 = tree_check(lines, 5)
    trees17 = tree_check(lines, 7)
    trees21 = tree_check(lines[::2], 1)
    print("Tree path product: {}".format(trees11 * trees13 * trees15 * trees17 * trees21))
