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

def find_num(line, start, stop, step):
    for i in range(start, stop, step):
        if line[i] in NUMS:
            return int(line[i])

        for num_word, num in WORD_TO_NUMBER_DICT.items():
            if num_word in line[i: i+len(num_word)]:
                return num

def part2(lines):
    total = 0

    for line in lines:
        first = find_num(line, 0, len(line), 1)
        last = find_num(line, len(line) - 1, -1, -1)
        total += int(f'{first}{last}')

    return total

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
print(part2(lines))

