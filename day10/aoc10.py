def find_jolt_product(adapters):
    adapters.sort()
    previous = 0
    differences = []
    for adapter in adapters:
        differences.append(adapter-previous)
        previous = adapter
    differences.append(3)  # for my device
    return differences.count(1) * differences.count(3)


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = list(map(int, file1.readlines()))
    jolt_product = find_jolt_product(lines)
    print("The jolt product is {}".format(jolt_product))
