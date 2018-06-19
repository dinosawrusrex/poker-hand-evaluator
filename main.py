import json, poker_hand_evaluator, random_hand_generator

if __name__ == '__main__':
    with open('card_template.json', 'r+') as hands:
        template = json.load(hands)
        new_hands = random_hand_generator.generate_random_hand(template)
    game = poker_hand_evaluator.Game(new_hands)
    game.print_information()

