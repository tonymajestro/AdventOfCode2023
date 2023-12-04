import sys

def solve(lines):
    total = 0
    for line in lines:
        parts = line.split('|')
        winners = set(parts[0].split()[2:])
        numbers = set(parts[1].split())

        num_matches = len(winners.intersection(numbers))
        if num_matches > 0:
            total += 2 ** (num_matches - 1)

    return total

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
print(solve(lines))
