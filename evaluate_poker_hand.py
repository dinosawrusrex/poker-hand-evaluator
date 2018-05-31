import json

class Card:
    def __init__(self, card, hand):
        self.suit = card['suit']
        self.rank = card['rank']
        self.hand = hand
        self.rank_score = self.rank_to_score()

    # Conversions
    def ace_conversion(self):
        ranks = [self.hand[card]['rank'] for card in self.hand]
        low_order = {2,3,4,5}
        if set(ranks).intersection(low_order) == low_order:
            return(1)
        else:
            return(14)

    def convert_alpha(self):
        royalty_conversion = {'jack': 11, 'queen': 12, 'king': 13}
        if self.rank == 'ace':
            return(self.ace_conversion())
        else:
            return(royalty_conversion[self.rank])

    def rank_to_score(self):
        if isinstance(self.rank, int):
            output = self.rank
        else:
            output = self.convert_alpha()
        return(output)


class Hand:

    SCORE = {'high card': 1,
         'one pair': 2,
         'two pair': 3,
         'three of a kind': 4,
         'straight': 5,
         'flush': 6,
         'full house': 7,
         'four of a kind': 8,
         'straight flush': 9}

    def __init__(self, hand):
        self.cards = [Card(hand[card], hand) for card in hand]
        self.poker_hand = self.rank_hand()
        self.score = self.SCORE[self.poker_hand]

    def check_for_flush(self):
        suits = [card.suit for card in self.cards]
        if len(set(suits)) == 1:
            return(True)
        else:
            return(False)

    def check_for_straight(self):
        ranks = sorted([card.rank_score for card in self.cards])
        output = [ranks[i]-ranks[i+1] for i in range(len(ranks)-1)].count(-1)\
                == 4
        return(output)

    def create_rank_pattern(self):
        ranks = [card.rank for card in self.cards]
        count_pattern = sorted([ranks.count(rank) for rank in set(ranks)])
        return(count_pattern)

    def rank_hand(self):
        if self.check_for_straight():
            if self.check_for_flush():
                return('straight flush')
            return('straight')
        elif self.check_for_flush() and not self.check_for_straight():
            return('flush')
        elif self.create_rank_pattern() == [1,4]:
            return('four of a kind')
        elif self.create_rank_pattern() == [2,3]:
            return('full house')
        elif self.create_rank_pattern() == [1,1,3]:
            return('three of a kind')
        elif self.create_rank_pattern() == [1,2,2]:
            return('two pair')
        elif self.create_rank_pattern() == [1,1,1,2]:
            return('one pair')
        else:
            return('high card')


class Game:
    def __init__(self, data):
        self.hand_one = Hand(data['hand_one'])
        self.hand_two = Hand(data['hand_two'])

    def index_to_compare(self):
        scores_one = [card.rank_score for card in self.hand_one.cards]
        scores_two = [card.rank_score for card in self.hand_two.cards]
        scores_one = sorted(set(scores_one), key=scores_one.count)
        scores_two = sorted(set(scores_two), key=scores_two.count)
        for i in range(len(scores_one)-1, -1, -1):
            if scores_one[i] != scores_two[i]:
                return(scores_one[i], scores_two[i])
        return(scores_one[i], scores_two[i])

    def evaluate_hands(self):
        if self.hand_one.score > self.hand_two.score:
            return('hand one wins by score')
        elif self.hand_one.score < self.hand_two.score:
            return('hand two wins by score')
        else:
            card_one, card_two = self.index_to_compare()
            if card_one > card_two:
                return('hand one wins by max rank_score')
            elif card_one < card_two:
                return('hand two wins by max rank_score')
            else:
                return('identical hands')


with open('hands.json', 'r') as hands:
    data = json.load(hands)

game = Game(data)
print('Hand one is a {} and has a score of {}.'.format(game.hand_one.poker_hand, game.hand_one.score))
print()
print('Hand two is a {} and has a score of {}.'.format(game.hand_two.poker_hand, game.hand_two.score))
print()
print(game.evaluate_hands())
