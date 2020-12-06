def get_family_total(family_data):
    return len(set(family_data.replace('\n', '')))


def get_sum(family_surveys):
    return sum(map(get_family_total, family_surveys))


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    groups = file1.read().split('\n\n')
    the_sum = get_sum(groups)
    print("The sum is:  {}".format(the_sum))
