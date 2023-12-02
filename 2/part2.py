import collections
import math
import sys

def solve(line):
    game = line.split(':')[1]
    max_cubes = collections.defaultdict(int)

    for hand in game.split(';'):
        for colors in hand.split(','):
            cubes = int(colors.split()[0])
            color = colors.split()[1]

            max_cubes[color] = max(cubes, max_cubes[color])

    return math.prod(max_cubes.values())

def part2(lines):
    total = 0
    for line in lines:
        total += solve(line)

    return total

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
print(part2(lines))
