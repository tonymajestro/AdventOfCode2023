import sys

CUBE_COUNT = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def solve(line):
    """ Returns the ID of the game if the game is possible, otherwise 0"""

    game_meta, game = line.split(':')
    game_id = int(game_meta.split()[1])

    for hand in game.split(';'):
        for colors in hand.split(','):
            cubes = int(colors.split()[0])
            color = colors.split()[1]
            
            # Impossible game
            if cubes > CUBE_COUNT[color]:
                return 0

    return game_id


def part1(lines):
    total = 0
    for line in lines:
        total += solve(line)

    return total

lines = [line.strip() for line in open(sys.argv[1]).readlines()]
print(part1(lines))
