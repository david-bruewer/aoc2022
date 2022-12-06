def parse(filename):
    stacks = list()
    commands = list()
    with open(filename, "r") as f:
        is_stacks = True
        for line in f:
            if is_stacks:
                stacks.append(line.strip().split(' '))
                if line.strip() == '':
                    is_stacks = False;
                    stacks.pop()
            else:
                commands.append(line.strip().split(' '))
    return stacks, commands


def execute_command(stacks, count, start, end):
    i = 0
    while i < count:
        crate = stacks[start - 1].pop()
        stacks[end - 1].append(crate)
        i += 1
    return stacks


def part_one(filename):
    stacks, commands = parse(filename)
    tops = list()
    for command in commands:
        stacks = execute_command(stacks, int(command[1]), int(command[3]), int(command[5]))

    for stack in stacks:
        tops.append(stack.pop())
    print(''.join(tops))


def execute_command_two(stacks, count, start, end):
    stack_length = len(stacks[start-1])
    crates = stacks[start - 1][stack_length-count:stack_length]
    del stacks[start-1][stack_length-count:stack_length]
    stacks[end - 1].extend(crates)
    return stacks


def part_two(filename):
    stacks, commands = parse(filename)
    tops = list()
    for command in commands:
        stacks = execute_command_two(stacks, int(command[1]), int(command[3]), int(command[5]))

    for stack in stacks:
        tops.append(stack.pop())
    print(''.join(tops))


if __name__ == '__main__':
    part_one("test.txt")
    part_one("input.txt")
    part_two("test.txt")
    part_two("input.txt")
