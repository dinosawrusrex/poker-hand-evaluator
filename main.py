import json, evaluate_poker_hand, random_hand_generator

if __name__ == '__main__':
    with open('card_template.json', 'r+') as hands:
        template = json.load(hands)
        new_hands = random_hand_generator.generate_random_card(template)
    game = evaluate_poker_hand.Game(new_hands)
    game.print_information()

