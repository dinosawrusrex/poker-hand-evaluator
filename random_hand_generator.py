import json
from random import randrange

def generate_random_hand(hands):
    card_history = []
    one_deck = one_or_infinite_deck()
    for hand in hands:
        for card in hands[hand]:
            hands[hand][card]["suit"], hands[hand][card]["rank"], card_history\
            = generate_random_card(card_history, one_deck)
    #print(card_history)
    return(hands)

def generate_random_card(card_history, one_deck):
    card = (generate_random_suit(), generate_random_rank())
    if card in card_history and one_deck:
        #print('reshuffling')
        return(generate_random_card(card_history, one_deck))
    else:
        card_history.append(card)
        return(card[0], card[1], card_history)

def generate_random_suit():
    suits = ["spade", "club", "diamond", "heart"]
    return(suits[randrange(len(suits))])

def generate_random_rank():
    ranks = [randrange(2, 11), "ace", "jack", "queen", "king"]
    return(ranks[randrange(len(ranks))])

def one_or_infinite_deck():
    deck = input('Enter "1" for one or "0" for infinite decks: ')
    if deck not in ["0", "1"]:
        print('Invalid input. Please try again.')
        return(one_or_infinite_deck())
    output = True if deck == '1' else False
    return(output)

if __name__ == '__main__':
    with open('card_template.json', 'r+') as file:
        template = json.load(file)
        new_json = generate_random_hand(template)
        file.seek(0)
        file.truncate()
        json.dump(new_json, file)
