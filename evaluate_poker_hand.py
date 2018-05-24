# Conversions
ROYALTY_CONVERSIONS = {'jack': 11, 'queen': 12, 'king': 13}

def ace_conversion(ranks):
    low_order = {2,3,4,5}
    if set(ranks).intersection(low_order) == low_order:
        return(1)
    else:
        return(14)

def convert_alpha(rank, ranks):
    if rank == 'ace':
        return(ace_conversion(ranks))
    else:
        return(ROYALTY_CONVERSIONS[rank])

def turn_ranks_to_numbers(hand):
    ranks = [int(card[1]) if card[1].isdigit() else card[1] for card in hand]
    output = sorted([convert_alpha(rank, ranks) if isinstance(rank, str)
                     else rank for rank in ranks])
    return(output)

def separate_ranks_and_suits(hand):
    return([card.split(' ') for card in hand])


# Ranking
SCORE = {'high card': 1,
         'one pair': 2,
         'two pair': 3,
         'three of a kind': 4,
         'straight': 5,
         'flush': 6,
         'full house': 7,
         'four of a kind': 8,
         'straight flush': 9}


# Hands
with open('hands', 'r') as hands:
    hands = hands.read()

hand_one, hand_two = [sorted(hand.split(', ')) for hand in hands.split('\n')
                      if hand != '']
print(hand_one)
hand_one = separate_ranks_and_suits(hand_one)
hand_two = separate_ranks_and_suits(hand_two)


# For checking flush and straights
def check_for_same_suit(hand):
    suits = [card[0] for card in hand]
    if len(set(suits)) == 1:
        return(True)
    else:
        return(False)

def check_for_numeric_order(hand):
    ranks = turn_ranks_to_numbers(hand)
    output = sum([ranks[i]-ranks[i+1] for i in range(len(ranks)-1)]) == -4
    return(output)


# Check for identical ranks
def create_rank_patterns(hand):
    ranks = turn_ranks_to_numbers(hand)
    count_pattern = sorted([ranks.count(rank) for rank in set(ranks)])
    return(count_pattern)


# Identify poker hand
def rank_hand(hand):
    if check_for_numeric_order(hand):
        if check_for_same_suit(hand):
            return('straight flush')
        return('straight')
    elif check_for_same_suit(hand) and not check_for_numeric_order(hand):
        return('flush')
    elif create_rank_patterns(hand) == [1,4]:
        return('four of a kind')
    elif create_rank_patterns(hand) == [2,3]:
        return('full house')
    elif create_rank_patterns(hand) == [1,1,3]:
        return('three of a kind')
    elif create_rank_patterns(hand) == [1,2,2]:
        return('two pair')
    elif create_rank_patterns(hand) == [1,1,1,2]:
        return('one pair')
    else:
        return('high card')


# Compare two hands
def mode_rank(hand):
    ranks = turn_ranks_to_numbers(hand)
    output = max(set(ranks), key=ranks.count)
    return(output)

def evaluate_hands(hand_one, hand_two):
    if SCORE[rank_hand(hand_one)] > SCORE[rank_hand(hand_two)]:
        return('hand one wins by score')
    elif SCORE[rank_hand(hand_one)] < SCORE[rank_hand(hand_two)]:
        return('hand two wins by score')
    else: # If both hands have the same 'points'
        if mode_rank(hand_one) > mode_rank(hand_two):
            return('hand one wins max rank')
        elif mode_rank(hand_one) < mode_rank(hand_two):
            return('hand two wins max rank')
        else:
            return('identical hands')


print('Hand one has {}, which is a {} and has a score of {}.'.format(hand_one,
rank_hand(hand_one), SCORE[rank_hand(hand_one)]))
print()
print('Hand two has {}, which is a {} and has a score of {}.'.format(hand_two,
rank_hand(hand_two), SCORE[rank_hand(hand_two)]))
print()
print(evaluate_hands(hand_one, hand_two))
