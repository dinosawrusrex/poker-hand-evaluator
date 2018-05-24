# Conversions
ROYALTY_CONVERSIONS = {'j': 10, 'q': 11, 'k': 12}

def ACE_CONVERSION(ranks):
    low_order = {2,3,4,5}
    if set(ranks).intersection(low_order) == low_order:
        return(1)
    else:
        return(13)

def convert_alpha(rank, ranks):
    if rank == 'a':
        return(ACE_CONVERSION(ranks))
    else:
        return(ROYALTY_CONVERSIONS[rank])

# Hands
with open('hands', 'r') as hands:
    hands = hands.read()

hand_one, hand_two = [sorted(hand.split(', ')) for hand in hands.split('\n')
                      if hand != '']

trial_hand = ['sa', 's2', 's6', 's4', 's5']


# Check for flush and straights
def check_for_same_suit(hand):
    suits = [card[0] for card in hand]
    if len(set(suits)) == 1:
        return(True)
    else:
        return(False)

def check_for_numeric_order(hand):
    ranks = [int(card[1]) if card[1].isdigit() else card[1] for card in hand]
    ranks = sorted([convert_alpha(rank, ranks) if isinstance(rank, str)
                    else rank for rank in ranks])
    output = sum([ranks[i]-ranks[i+1] for i in range(len(ranks)-1)]) == -4
    return(output)

# Check for identical ranks



def rank_hand(hand):
    if check_for_numeric_order(hand):
        if check_for_same_suit(hand):
            return('straight flush')
        return('straight')
    elif check_for_same_suit(hand) and not check_for_numeric_order(hand):
        return('flush')

print(rank_hand(trial_hand))
