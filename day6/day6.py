def parse(filename):
    entries = str
    with open(filename, "r") as f:
        for line in f:
            return list(line)


def check_for_packet(entries):
    previous = entries[0:1]
    i = 1
    while i < len(entries):
        if not entries[i] in previous:
            if len(previous) == 3:
                return i + 1
            previous.append(entries[i])
            i+=1
        else:
            del previous[0:previous.index(entries[i])+1]



def part_one(filename):
    entries = parse(filename)
    print(check_for_packet(entries))


def check_for_message(entries):
    previous = entries[0:1]
    i = 1
    while i < len(entries):
        if not entries[i] in previous:
            if len(previous) == 13:
                return i + 1
            previous.append(entries[i])
            i += 1
        else:
            del previous[0:previous.index(entries[i]) + 1]


def part_two(filename):
    entries = parse(filename)
    print (check_for_message(entries))


if __name__ == '__main__':
    part_one("test.txt")
    part_one("input.txt")
    part_two("test.txt")
    part_two("input.txt")
