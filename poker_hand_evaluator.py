import json

class Card:
    def __init__(self, card, hand):
        self.suit = card['suit']
        self.rank = card['rank']
        self.hand = hand

    def rank_score(self):
        if isinstance(self.rank, int):
            return self.rank
        else:
            return self.convert_alpha()

    def convert_alpha(self):
        royalty_conversion = {'jack': 11, 'queen': 12, 'king': 13,
                'ace': self.ace_conversion()}
        return royalty_conversion[self.rank]

    def ace_conversion(self):
        if {2,3,4,5}.issubset([self.hand[card]['rank'] for card in self.hand]):
            return 1
        else:
            return 14


class Hand:

    def __init__(self, hand):
        self.cards = [Card(hand[card], hand) for card in hand]
        self.suits = [card.suit for card in self.cards]
        self.rank_scores = sorted([card.rank_score() for card in self.cards])
        self.score = self.SCORE[self.poker_hand()]

    SCORE = {'high card': 1,
         'one pair': 2,
         'two pair': 3,
         'three of a kind': 4,
         'straight': 5,
         'flush': 6,
         'full house': 7,
         'four of a kind': 8,
         'straight flush': 9}

    def frequency_of_ranks(self):
        frequencies = {count: sorted([score for score in set(self.rank_scores)
                    if self.rank_scores.count(score) == count], reverse=True)
                    for count in reversed(self.list_of_counts())}
        return frequencies

    def poker_hand(self):
        if self.check_for_straight():
            if self.check_for_flush():
                return 'straight flush'
            return 'straight'
        elif self.check_for_flush() and not self.check_for_straight():
            return 'flush'
        elif self.list_of_counts() == [1,4]:
            return 'four of a kind'
        elif self.list_of_counts() == [2,3]:
            return 'full house'
        elif self.list_of_counts() == [1,1,3]:
            return 'three of a kind'
        elif self.list_of_counts() == [1,2,2]:
            return 'two pair'
        elif self.list_of_counts() == [1,1,1,2]:
            return 'one pair'
        else:
            return 'high card'

    def list_of_counts(self):
        count_pattern = sorted([self.rank_scores.count(score)
                        for score in set(self.rank_scores)])
        return count_pattern


    def check_for_flush(self):
        output = len(set(self.suits)) == 1
        return output

    def check_for_straight(self):
        output = [self.rank_scores[i]-self.rank_scores[i+1] for i in
                range(len(self.rank_scores)-1)].count(-1) == 4
        return output


class Game:
    def __init__(self, data):
        self.hand_one = Hand(data['hand_one'])
        self.hand_two = Hand(data['hand_two'])

    def evaluate_hands(self):
        if self.hand_one.score > self.hand_two.score:
            return 'Hand one wins by score.'
        elif self.hand_one.score < self.hand_two.score:
            return 'Hand two wins by score.'
        else:
            return self.evaluate_tied_hands()

    def evaluate_tied_hands(self):
        print('Hands are tied. Looking down the ranks:\n')
        for key in self.hand_one.frequency_of_ranks():
            print('Looking for card(s) with count {}:\n'.format(key))
            for i in range(len(self.hand_one.frequency_of_ranks()[key])):
                rank_one = self.hand_one.frequency_of_ranks()[key][i]
                rank_two = self.hand_two.frequency_of_ranks()[key][i]
                print('Comparing ranks of hand one: {}, hand two: {}.'.format(
                    rank_one, rank_two))
                if rank_one > rank_two:
                    return '\nHand one wins by a higher rank.'
                elif rank_one < rank_two:
                    return '\nHand two wins by a higher rank.'
                else:
                    print('Still tied. Continue looking.\n')
        else:
            return 'Identical hands. Draw.'

    def print_information(self):
        print('Hand one: {}'.format([(card.suit, card.rank) for card in
            self.hand_one.cards]))
        print('Hand two: {} \n'.format([(card.suit, card.rank) for card in
            self.hand_two.cards]))
        print('Hand one is a {} and has a score of {}.'.format(
            self.hand_one.poker_hand(), self.hand_one.score))
        print('Hand two is a {} and has a score of {}.\n'.format(
            self.hand_two.poker_hand(), self.hand_two.score))
        print(self.evaluate_hands())


if __name__ == '__main__':
    with open('hands.json', 'r') as hands:
        data = json.load(hands)
        game = Game(data)
        game.print_information()
