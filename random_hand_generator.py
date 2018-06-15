import json
from random import randrange

def generate_random_card(hands):
    for hand in hands:
        for card in hands[hand]:
            hands[hand][card]["suit"] = generate_random_suit()
            hands[hand][card]["rank"] = generate_random_rank()
    return(hands)

def generate_random_suit():
    suits = ["spade", "club", "diamond", "heart"]
    return(suits[randrange(len(suits)-1)])

def generate_random_rank():
    ranks = [randrange(2, 11), "ace", "jack", "queen", "king"]
    return(ranks[randrange(len(ranks)-1)])

if __name__ == '__main__':
    with open('card_template.json', 'r+') as file:
        template = json.load(file)
        new_json = generate_random_card(template)
        file.seek(0)
        file.truncate()
        json.dump(new_json, file)
