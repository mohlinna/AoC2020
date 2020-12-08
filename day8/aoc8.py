def run_program(instructions):
    acc = 0
    line = 0
    run_lines = set()
    while line not in run_lines:
        run_lines.add(line)
        instruction = instructions[line].split()
        op = instruction[0]
        arg = int(instruction[1])
        if op == 'jmp':
            line += arg
        elif op == 'acc':
            acc += arg
            line += 1
        elif op == 'nop':
            line += 1
    return acc


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    accumulator = run_program(lines)
    print("The acc is at {}".format(accumulator))
