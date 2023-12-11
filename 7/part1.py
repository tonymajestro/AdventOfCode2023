import sys
import collections
import functools

CARD_SCORES = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
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
    hand1_score = score_hand(hand1)
    hand2_score = score_hand(hand2)

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
