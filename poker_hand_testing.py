import unittest
from evaluate_poker_hand import rank_hand, separate_ranks_and_suits

TEST = [(['spade 5', 'spade 6', 'spade 7', 'spade 8', 'spade 9'],
         'straight flush'),
        (['spade 8', 'diamond ace', 'spade ace', 'heart ace', 'club ace'],
         'four of a kind'),
        (['club king', 'heart king', 'spade king', 'club 10', 'spade 10'],
         'full house'),
        (['club queen', 'club 8', 'club 6', 'club 4', 'club 3'],
         'flush'),
        (['diamond 2', 'club 3', 'spade 4', 'diamond 5', 'club 6'],
         'straight'),
        (['diamond jack', 'club jack', 'heart jack', 'club 5', 'diamond 8'],
         'three of a kind'),
        (['spade 6', 'club 6', 'club 10', 'diamond 10', 'diamond king'],
         'two pair'),
        (['diamond 2', 'heart 6', 'spade 8', 'club ace', 'heart ace'],
         'one pair'),
        (['heart king', 'spade jack', 'club 10', 'heart 6', 'diamond 3'],
         'high card')
        ]

class Evaluate_Hand_Test(unittest.TestCase):

    def test_straight_flush(self):
        self.assertEqual(rank_hand(separate_ranks_and_suits(TEST[0][0])),
                TEST[0][1])

    def test_straight_flush(self):
        self.assertEqual(rank_hand(separate_ranks_and_suits(TEST[0][0])),
                TEST[0][1])

    def test_four_of_a_kind(self):
        self.assertEqual(rank_hand(separate_ranks_and_suits(TEST[1][0])),
                TEST[1][1])

    def test_full_house(self):
        self.assertEqual(rank_hand(separate_ranks_and_suits(TEST[2][0])),
                TEST[2][1])

    def test_flush(self):
        self.assertEqual(rank_hand(separate_ranks_and_suits(TEST[3][0])),
                TEST[3][1])

    def test_straight(self):
        self.assertEqual(rank_hand(separate_ranks_and_suits(TEST[4][0])),
                TEST[4][1])

    def test_three_of_a_kind(self):
        self.assertEqual(rank_hand(separate_ranks_and_suits(TEST[5][0])),
                TEST[5][1])

    def test_two_pair(self):
        self.assertEqual(rank_hand(separate_ranks_and_suits(TEST[6][0])),
                TEST[6][1])

    def test_one_pair(self):
        self.assertEqual(rank_hand(separate_ranks_and_suits(TEST[7][0])),
                TEST[7][1])

    def test_high_cards(self):
        self.assertEqual(rank_hand(separate_ranks_and_suits(TEST[8][0])),
                TEST[8][1])



if __name__ == '__main__':
    unittest.main()
