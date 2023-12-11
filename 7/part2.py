import sys
import collections
import functools

JOKER = 'J'
CARDS = 'AKQT98765432'
CARD_SCORES = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 11,
    '9': 10,
    '8': 9,
    '7': 8,
    '6': 7,
    '5': 6,
    '4': 5,
    '3': 4,
    '2': 3,
    'J': 2
}

def is_five_of_a_kind(hand):
    counter = collections.Counter([card for card in hand])
    return max(counter.values()) == 5

def is_four_of_a_kind(hand):
    counter = collections.Counter([card for card in hand])
    return max(counter.values()) == 4

def is_three_of_a_kind(hand):
    counter = collections.Counter([card for card in hand])
    return max(counter.values()) == 3

def is_pair(hand):
    counter = collections.Counter([card for card in hand])
    return max(counter.values()) == 2

def is_high_card(hand):
    counter = collections.Counter([card for card in hand])
    return max(counter.values()) == 1

def is_full_house(hand):
    counter = collections.Counter([card for card in hand])
    return 3 in counter.values() and 2 in counter.values()

def is_two_pair(hand):
    counter = collections.Counter([card for card in hand])
    num_pairs = len([count for count in counter.values() if count == 2])
    return num_pairs == 2

def score_hand(hand):
    if is_five_of_a_kind(hand):
        return 7
    elif is_four_of_a_kind(hand):
        return 6
    elif is_full_house(hand):
        return 5
    elif is_three_of_a_kind(hand):
        return 4
    elif is_two_pair(hand):
        return 3
    elif is_pair(hand):
        return 2
    elif is_high_card(hand):
        return 1
    else:
        return 0

def score_joker_hand(hand):

    def inner(current_hand, position):
        """ Backtrack to find best possible score with jokers """
        if position >= len(hand):
            return score_hand(current_hand)
        elif current_hand[position] != JOKER:
            return inner(current_hand, position + 1)

        # Find best card for the joker
        best_score = 0
        for card in CARDS:
            # Copy current hand into new list before recursing
            temp = list(current_hand)
            temp[position] = card

            score = inner(temp, position + 1)
            best_score = max(score, best_score)

        return best_score

    return inner(list(hand), 0)

def score_equal_hands(hand1, hand2):
    for card1, card2 in zip(hand1, hand2):
        card1_score = CARD_SCORES[card1]
        card2_score = CARD_SCORES[card2]

        if card1_score < card2_score:
            return -1
        elif card1_score > card2_score:
            return 1

    return 0

def compare_hands(hand1, hand2):
    hand1_score = score_joker_hand(hand1)
    hand2_score = score_joker_hand(hand2)

    if hand1_score == hand2_score:
        return score_equal_hands(hand1, hand2)
    else:
        return hand1_score - hand2_score

def solve(hands, bets):
    hands_to_bets_map = dict(zip(hands, bets))
    hands.sort(key=functools.cmp_to_key(compare_hands))

    total = 0
    for i, hand in enumerate(hands):
        bet = hands_to_bets_map[hand]
        total += (i + 1) * bet

    return total


hands = []
bets = []
with open(sys.argv[1]) as f:
    for line in f:
        hand, bet = line.split()
        hands.append(hand)
        bets.append(int(bet))

print(solve(hands, bets))
