def run_alt_program(instructions, li, ac, rl, end):
    alt_line = li
    alt_acc = ac
    alt_run_lines = set(rl)
    while alt_line not in alt_run_lines:
        alt_run_lines.add(alt_line)
        instruction = instructions[alt_line].split()
        op = instruction[0]
        arg = int(instruction[1])
        if op == 'jmp':
            alt_line += arg
        elif op == 'acc':
            alt_acc += arg
            alt_line += 1
        elif op == 'nop':
            alt_line += 1

        if alt_line == end:
            return [alt_acc]
    return []


def run_program(instructions):
    acc = 0
    line = 0
    run_lines = set()
    end = len(instructions)
    while line not in run_lines:
        run_lines.add(line)
        instruction = instructions[line].split()
        op = instruction[0]
        arg = int(instruction[1])
        if op == 'jmp':
            alt_result = run_alt_program(instructions, line+1, acc, run_lines, end)
            if alt_result:
                return alt_result[0]
            line += arg
        elif op == 'acc':
            acc += arg
            line += 1
        elif op == 'nop':
            alt_result = run_alt_program(instructions, line+arg, acc, run_lines, end)
            if alt_result:
                return alt_result[0]
            line += 1
    return None


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    accumulator = run_program(lines)
    print("The acc is at {}".format(accumulator))
