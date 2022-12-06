def parse(filename):
    entries = list()
    with open(filename, "r") as f:
        for line in f:
            entries.append(line.strip().split(','))
    return entries


def check_overlap(first, second):
    if (first[0] <= second[0] and first[-1] >= second[-1]) or (second[0] <= first[0] and second[-1] >= first[-1]):
        return 1
    return 0


def part_one(filename):
    entries = parse(filename)
    envelop = 0
    for entry in entries:
        first = entry[0].split('-')
        first = [int(f) for f in first]
        second = entry[1].split('-')
        second = [int(s) for s in second]
        envelop += check_overlap(first, second)
    print(envelop)


def check_overlap_two(first, second):
    if (second[-1] >= first[0] >= second[0]) or (first[-1] >= second[0] >= first[0]):
        return 1
    return 0


def part_two(filename):
    entries = parse(filename)
    envelop = 0
    for entry in entries:
        first = entry[0].split('-')
        first = [int(f) for f in first]
        second = entry[1].split('-')
        second = [int(s) for s in second]
        envelop += check_overlap_two(first, second)
    print(envelop)



if __name__ == '__main__':
    part_one("test.txt")
    part_one("input.txt")
    part_two("test.txt")
    part_two("input.txt")
