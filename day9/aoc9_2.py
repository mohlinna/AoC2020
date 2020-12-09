from collections import deque


def find_sum(num, array):
    size = len(array)
    for x in range(size-1):
        for y in range(x + 1, size):
            if array[x] + array[y] == num:
                return True
    return False


def find_weakness(inputs):
    last25 = deque()
    for num in inputs[:25]:
        last25.append(num)
    for num in inputs[25:]:
        if find_sum(num, last25):
            last25.popleft()
            last25.append(num)
        else:
            target = num
            break

    for i in range(len(inputs)-1):
        total = inputs[i]
        for j in range(i+1, len(inputs)):
            total += inputs[j]
            if total == target:
                return max(inputs[i:j+1]) + min(inputs[i:j+1])
            elif total > target:
                break


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = map(int, file1.readlines())
    weakness = find_weakness(lines)
    print("The weakness is {}".format(weakness))
