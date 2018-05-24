ROYALTY_CONVERSIONS = {'j': 10, 'q': 11, 'k': 12}

#ACE_CONVERSION

with open('hands', 'r') as hands:
    hands = hands.read()

hand_one, hand_two = [sorted(hand.split(', ')) for hand in hands.split('\n')
                      if hand != '']

def check_for_same_suit(hand):
    suits = [card[0] for card in hand]
    if len(set(suits)) == 1:
        return(True)
    else:
        return(False)

def check_for_numeric_order(hand):
    ranks = [int(card[1]) if card[1].isdigit() else card[1] for card in hand]
    if 'a' in ranks:
        ranks = ranks.remove('a')
    return(ranks)

print(hand_two)
print(check_for_numeric_order(hand_two))


def rank_hand(hand):
    for card in hand:
        if hand[0][0] in card:
            continue

