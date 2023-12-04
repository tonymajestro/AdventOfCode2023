import sys

def solve(lines):
    card_counts = {game: 1 for game in range(len(lines))}

    for game, line in enumerate(lines):
        parts = line.split('|')

        winners = set(parts[0].split()[2:])
        numbers = set(parts[1].split())
        num_cards = card_counts[game]

        num_matches = len(winners.intersection(numbers))

        for i in range(num_matches):
            card_counts[game + i + 1] += num_cards

    return sum(card_counts.values())

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
print(solve(lines))
