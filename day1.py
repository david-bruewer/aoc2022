

def parse(filename):
    entries = ''
    with open(filename, "r") as f:
        for line in f:
            entries = entries + line
    return entries.split('\n\n')


def part_one(filename):
    entries =(parse(filename))
    print(max_calories(entries))


def max_calories(entries):
    maximum =0
    for entry in entries:
        maximum = max(maximum, sum([int(i) for i in (entry.split('\n'))]))
    return  maximum

def top_three(entries):
    all_cals = list()
    for entry in entries:
        all_cals.append(sum([int(i) for i in (entry.split('\n'))]))
        all_cals.sort()
        all_cals.reverse()
        if len(all_cals) > 3:
            all_cals.pop(3)
    return sum(all_cals)


def part_two(filename):
    entries = parse(filename)
    print(top_three(entries))


if __name__ == '__main__':
    part_one("test.txt")
    part_one("input.txt")
    part_two("test.txt")
    part_two("input.txt")
