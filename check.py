from collections import Counter

# Based on Jacks or Better pay table:
# https://en.wikipedia.org/wiki/Video_poker#Jacks_or_Better
prize_table = {
    "Royal Flush": 800,
    "Straight Flush": 50,
    "Four of a kind": 25,
    "Full House": 9,
    "Flush": 6,
    "Straight": 4,
    "Three of a kind": 3,
    "Two Pair": 2,
    "Jacks or Better": 1,
    "Nothing": 0
}


def check_jacks_or_better(hand):
    c = dict(Counter([v for v, _ in hand]))
    d = [v for k, v in c.items() if k >= 9] # Only jacks or better counts
    return 2 in d # At least one pair

def check_two_pairs(hand):
    c = Counter(Counter([v for v, _ in hand]).values())
    return 2 in c and c[2] == 2

def check_three_of_a_kind(hand):
    return 3 in Counter([v for v, _ in hand]).values()

def check_straight(hand):
    sv = sorted([v for v, _ in hand])[::-1]
    diffs = [sv[n] - sv[n+1] for n in range(len(sv)-1)]
    return diffs == [1, 1, 1, 1]

def check_flush(hand):
    return 5 in Counter([s for _, s in hand]).values()

def check_full_house(hand):
    c = Counter(Counter([v for v, _ in hand]).values())
    return 2 in c and 3 in c

def check_four_of_a_kind(hand):
    return 4 in Counter([v for v, _ in hand]).values()

def check_straight_flush(hand):
    return check_straight(hand) and check_flush(hand)

def check_royal_flush(hand):
    return check_straight_flush(hand) and max([v for v, _ in hand]) == 12

def get_prize(hand):
    if check_royal_flush(hand):
        pattern = "Royal Flush"
    elif check_straight_flush(hand):
        pattern = "Straight Flush"
    elif check_four_of_a_kind(hand):
        pattern = "Four of a kind"
    elif check_full_house(hand):
        pattern = "Full House"
    elif check_flush(hand):
        pattern = "Flush"
    elif check_straight(hand):
        pattern = "Straight"
    elif check_three_of_a_kind(hand):
        pattern = "Three of a kind"
    elif check_two_pairs(hand):
        pattern = "Two Pair"
    elif check_jacks_or_better(hand):
        pattern = "Jacks or Better"
    else:
        pattern = "Nothing"
    return pattern, prize_table[pattern]
