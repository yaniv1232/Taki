from card import Card
import random


deck = list()
cards_in_deck = 0
is_card_identical = 0
while cards_in_deck < 40:
    pulled_card = Card()
    for card in deck:
        if card == pulled_card:
            is_card_identical = 1
            break
    if is_card_identical == 1:
        is_card_identical = 0
        continue
    else:
        cards_in_deck += 1
        deck.append(pulled_card)

random.shuffle(deck)

num_players = 0
while int(num_players) not in range(2, 7):
    num_players = input("Enter number of players (between 2 to 6): ")

scores = list()
for i in range(int(num_players)):
    scores.append(0)

player_turn = 0
while deck:
    pulled_card = deck.pop()
    scores[player_turn] += pulled_card.num
    player_turn += 1
    if player_turn is num_players:
        player_turn = 0

for x in scores:
    player_index = x+1
    player_score = scores[x]
    print(f"Player {player_index} has {player_score} points")

winner_index = str(scores.index(max(scores)) + 1)
winner_score = str(max(scores))
print(f"Player {winner_index} is the winner with {winner_score} points")


