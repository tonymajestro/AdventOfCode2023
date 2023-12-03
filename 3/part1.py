import sys

NUMBERS = '1234567890'

def is_next_to_symbol(lines, i, j):
    def is_symbol(x, y):
        return (x >= 0 and x < len(lines) and
                y >= 0 and y < len(lines[x]) and
                lines[x][y] not in NUMBERS and
                lines[x][y] != '.')

    return (is_symbol(i - 1, j - 1) or is_symbol(i - 1, j) or is_symbol(i - 1, j + 1) or
            is_symbol(i, j - 1) or is_symbol(i, j + 1) or
            is_symbol(i + 1, j - 1) or is_symbol(i + 1, j) or is_symbol(i + 1, j + 1))

def part1(lines):
    total = 0
    for i, line in enumerate(lines):

        part_numbers = []
        found_symbol = False

        for j, c in enumerate(line):
            if c in NUMBERS:
                part_numbers.append(c)
                found_symbol = found_symbol or is_next_to_symbol(lines, i, j)

            else:
                if part_numbers and found_symbol:
                    total += int(''.join(part_numbers))

                part_numbers.clear()
                found_symbol = False

    return total

# Append '.' to each line to ensure that we always check numbers at the end of the line
lines = [line.strip() + '.' for line in open(sys.argv[1]).readlines()]
print(part1(lines))
