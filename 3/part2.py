import sys
import collections

NUMBERS = '1234567890'
GEAR = '*'

def find_symbol(lines, i, j):
    def get_symbol(x, y):
        if (x >= 0 and x < len(lines) and
                y >= 0 and y < len(lines[x]) and
                lines[x][y] not in NUMBERS and
                lines[x][y] != '.'):
            return (x, y, lines[x][y])

        return None

    return (get_symbol(i - 1, j - 1) or get_symbol(i - 1, j) or get_symbol(i - 1, j + 1) or
            get_symbol(i, j - 1) or get_symbol(i, j + 1) or
            get_symbol(i + 1, j - 1) or get_symbol(i + 1, j) or get_symbol(i + 1, j + 1))

def part2(lines):
    gear_map = collections.defaultdict(list)

    for i, line in enumerate(lines):
        part_numbers = []
        gear_location = None

        for j, c in enumerate(line):
            if c in NUMBERS:
                part_numbers.append(c)

                symbol_result = find_symbol(lines, i, j)
                if symbol_result:
                    x, y, symbol = symbol_result
                    if symbol == GEAR:
                        gear_location = (x, y)

            else:
                if part_numbers and gear_location:
                    gear_map[gear_location].append(int(''.join(part_numbers)))

                part_numbers.clear()
                gear_location = None

    gear_ratios = 0
    for gear_location, gears in gear_map.items():
        if len(gears) == 2:
            gear_ratios += gears[0] * gears[1]
    
    return gear_ratios

# Append '.' to each line to ensure that we always check numbers at the end of the line
lines = [line.strip() + '.' for line in open(sys.argv[1]).readlines()]
print(part2(lines))
