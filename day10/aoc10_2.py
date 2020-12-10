acceptable_jolt_diffs = [1, 2, 3]
calculated_paths = {}


def count_paths(point, graph, final):
    if point in calculated_paths:
        return calculated_paths[point]
    else:
        paths = 0
        for next_point in graph[point]:
            paths += count_paths(next_point, graph, final)
        calculated_paths[point] = paths
        return paths


def find_possible_next_adapters(num, next_3):
    nexts = []
    for jolt_diff in acceptable_jolt_diffs:
        if num+jolt_diff in next_3:
            nexts.append(num+jolt_diff)
    return nexts


def find_adapter_possibilities(adapters):
    adapters.append(0)
    adapters.sort()
    graph = {}
    for i in range(len(adapters)-1):
        possible_nexts = find_possible_next_adapters(adapters[i], adapters[i+1:i+4])
        graph[adapters[i]] = possible_nexts
    final_adapter = adapters[len(adapters)-1]
    calculated_paths[final_adapter] = 1
    return count_paths(0, graph, final_adapter)


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = list(map(int, file1.readlines()))
    adapter_possibilities = find_adapter_possibilities(lines)
    print("The number of possibilities is {}".format(adapter_possibilities))
