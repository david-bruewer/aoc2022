def parse(filename):
    entries = list()
    with open(filename, "r") as f:
        for line in f:
            entries.append(line.strip())
    return entries


def part_one(filename):
    priority = 0
    entries = parse(filename)
    for entry in entries:
        compartment_one = entry[:int(len(entry)/2)]
        compartment_two = entry[int(len(entry)/2):]
        item = check(compartment_one, compartment_two)
        priority += prioritize(item)
    print(priority)

def check(compartment_one, compartment_two):
    for item in compartment_one:
        if item in compartment_two:
            return item

def prioritize(item):
    score = ord(item)
    score-=38
    if score > 52:
        score-=58
    return score


def part_two(filename):
    entries = parse(filename)
    i=0
    priority=0
    while i < len(entries):
        item = check_three_compartments(entries[i], entries[i+1], entries[i+2])
        i += 3
        priority+=prioritize(item)
    print(priority)


def check_three_compartments(compartment_one, compartment_two, compartment_three):
    for item in compartment_one:
        if item in compartment_two and item in compartment_three:
            return item

if __name__ == '__main__':
    part_one("test.txt")
    part_one("input.txt")
    part_two("test.txt")
    part_two("input.txt")
