
def calc_2020():
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    array = []
    for line in Lines:
        array.append(int(line))
    size = len(array)
    for x in range(size):
        for y in range(x+1, size):
            for z in range(y+1, size):
                i = array[x]
                j = array[y]
                k = array[z]
                if i+j+k == 2020:
                    print("{}, {}, {}, {}".format(i, j, k, i*j*k))



if __name__ == '__main__':
    calc_2020()
