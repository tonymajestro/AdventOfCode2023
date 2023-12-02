import sys

NUMS = '123456789'

WORD_TO_NUMBER_DICT = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def first_num(line):
    for i in range(len(line)):
        if line[i] in NUMS:
            return int(line[i])

        for num_word, num in WORD_TO_NUMBER_DICT.items():
            if num_word in line[i: i+len(num_word)]:
                return num

def last_num(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i] in NUMS:
            return int(line[i])

        for num_word, num in WORD_TO_NUMBER_DICT.items():
            if num_word in line[i:]:
                return num

def part1(lines):
    total = 0

    for line in lines:
        nums = [num for num in line if num in NUMS]
        total += int(f'{nums[0]}{nums[-1]}')

    return (total)

def part2(lines):
    total = 0

    for line in lines:
        x = first_num(line)
        y = last_num(line)
        total += int(f'{x}{y}')

    return total

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
print(part2(lines))


