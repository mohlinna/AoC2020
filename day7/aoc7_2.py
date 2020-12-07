shiny_gold = 'shiny gold'


def make_child_map(bag_rules):
    child_map = {}
    for rule in bag_rules:
        rule_segment = rule.split('bag')
        parent_bag_list = rule_segment[0].split()
        parent_bag = '' + parent_bag_list[0] + ' ' + parent_bag_list[1]
        children = []
        first_child_list = rule_segment[1].split()
        if 'no' != first_child_list[2]:
            children.append([int(first_child_list[2]), '' + first_child_list[3] + ' ' + first_child_list[4]])
            for other_child in rule_segment[2:]:
                if '.' not in other_child:
                    other_child_list = other_child.split()
                    children.append([int(other_child_list[1]), '' + other_child_list[2] + ' ' + other_child_list[3]])
        child_map[parent_bag] = children
    return child_map


def find_num_descendents(bag, child_map):
    num_descendents = 0
    children = child_map[bag]
    for child in children:
        num_of_this_child = child[0]
        num_descendents += num_of_this_child
        num_descendents += num_of_this_child * find_num_descendents(child[1], child_map)
    return num_descendents


def find_bags(bag_rules):
    child_map = make_child_map(bag_rules)
    return find_num_descendents(shiny_gold, child_map)


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    bags = find_bags(lines)
    print("There are {} bags".format(bags))
