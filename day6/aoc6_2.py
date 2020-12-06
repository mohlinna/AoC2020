def get_family_total(family_data):
    divided_family_data = family_data.split('\n')
    questions_answered_yes = set(divided_family_data[0])
    for member in divided_family_data[1:]:
        print(questions_answered_yes)
        print(member)
        for answer_yes in questions_answered_yes.copy():
            if answer_yes not in member:
                questions_answered_yes.remove(answer_yes)
    print(questions_answered_yes)
    print("")
    return len(questions_answered_yes)


def get_sum(family_surveys):
    return sum(map(get_family_total, family_surveys))


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    groups = file1.read().split('\n\n')
    the_sum = get_sum(groups)
    print("The sum is:  {}".format(the_sum))
