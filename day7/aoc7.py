shiny_gold = 'shiny gold'


def make_parent_map(bag_rules):
    parent_map = {}
    for rule in bag_rules:
        rule_segment = rule.split('bag')
        parent_bag_list = rule_segment[0].split()
        parent_bag = '' + parent_bag_list[0] + ' ' + parent_bag_list[1]
        children = []
        first_child_list = rule_segment[1].split()
        if 'no' != first_child_list[2]:
            children.append('' + first_child_list[3] + ' ' + first_child_list[4])
            for other_child in rule_segment[2:]:
                if '.' not in other_child:
                    other_child_list = other_child.split()
                    children.append('' + other_child_list[2] + ' ' + other_child_list[3])
        for child in children:
            if child in parent_map:
                parent_map[child].append(parent_bag)
            else:
                parent_map[child] = [parent_bag]
    return parent_map


def find_possible_parents(bag, parent_map, parent_set):
    if bag in parent_map:
        possible_parents = parent_map[bag]
        for parent in possible_parents:
            parent_set.add(parent)
            find_possible_parents(parent, parent_map, parent_set)


def find_bags(bag_rules):
    parent_map = make_parent_map(bag_rules)
    parent_set = set()
    find_possible_parents(shiny_gold, parent_map, parent_set)
    return len(parent_set)


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    bags = find_bags(lines)
    print("There are {} possible bags".format(bags))
