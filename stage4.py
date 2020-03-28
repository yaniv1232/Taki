from card import Card
from operator import itemgetter
import random

# Adding cards to the deck
deck = list()
is_card_identical = False
while len(deck) < 40:
    pulled_card = Card()
    for card in deck:
        if card == pulled_card:
            is_card_identical = True
            break
    if is_card_identical:
        is_card_identical = False
        continue
    else:
        deck.append(pulled_card)

random.shuffle(deck)

# - - - - - - - - - - - - - - - - - - - - - - - - -

num_players = 0
while num_players not in range(2, 7):
    num_players_as_str = input("Enter number of players (between 2 to 6): ")
    num_players = int(num_players_as_str)

scores = dict()
for i in range(1, num_players+1):
    scores[i] = 0

player_turn = 1
while deck:
    pulled_card = deck.pop()
    scores[player_turn] += pulled_card.num
    player_turn += 1
    if player_turn > num_players:
        player_turn = 1

for player_index, player_score in scores.items():
    print(f"Player {player_index} has {player_score} points")

winner_index = max(scores.items(), key=itemgetter(1))[0]
winner_score = max(scores.values())
print(f"Player {player_index} is the winner with {winner_score} points")