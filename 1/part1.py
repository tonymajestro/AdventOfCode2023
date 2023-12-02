import sys

NUMS = '123456789'

def part1(lines):
    total = 0

    for line in lines:
        nums = [num for num in line if num in NUMS]
        total += int(f'{nums[0]}{nums[-1]}')

    return (total)

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
print(part1(lines))


