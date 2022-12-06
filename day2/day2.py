

def parse(filename):
    entries = list()
    with open(filename, "r") as f:
        for line in f:
            entries.append(line.strip().split(' '))
    return entries


def part_one(filename):
    entries =parse(filename)
    score = 0
    for entry in entries:
        converted = [convert(e) for e in entry]
        difference = difference_check(converted[1]-converted[0])

        score += converted[1] + (3 + 3*difference)
    print(score)


def difference_check(difference):
    if difference == 2:
        return -1
    if difference == -2:
        return 1
    return difference

def convert(letter):
    if letter == 'A' or letter == 'X':
        return 1
    if letter == 'B' or letter == 'Y':
        return 2
    return 3


def part_two(filename):
    entries = parse(filename)
    score = 0
    for entry in entries:
        converted = [convert(e) for e in entry]
        score += (converted[1]-1) * 3 + zero_to_three((converted[1]+converted[0] + 1) % 3)
    print(score)

def zero_to_three(num):
    if num == 0:
        return 3
    return num
# def convert_two(letter):
#     if letter == 'A' or letter == 'X':
#         return 1
#     if letter == 'B' or letter == 'Y':
#         return 2
#     return 3


if __name__ == '__main__':
    part_one("test.txt")
    part_one("input.txt")
    part_two("test.txt")
    part_two("input.txt")
