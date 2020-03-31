from card import Card
import random

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

num_of_players = 0
while num_of_players not in range(2, 7):
    num_of_players_as_str = input("Enter number of players (between 2 to 6): ")
    num_of_players = int(num_of_players_as_str)

# - - - - - - - - - - - - - - - - - - - - - - - - -

cards = dict()
for player in range(1, num_of_players + 1):
    cards[player] = list()
    for j in range(3):
        cards[player].append(deck.pop())

card_on_table = deck.pop()
winner_index = 0
player_turn = 1
player_has_card = False

while deck:
    current_player_num_of_cards = len(cards[player_turn])
    current_player_cards = cards[player_turn]
    for i in range(current_player_num_of_cards):
        current_player_card_color = getattr(current_player_cards[i], "color")
        card_on_table_color = getattr(card_on_table, "color")
        if current_player_card_color == card_on_table_color:
            card_on_table = current_player_cards[i]
            current_player_cards.remove(current_player_cards[i])
            player_has_card = True
            break
    if current_player_num_of_cards == 0:
        winner_index = player_turn
        break
    if not player_has_card:
        pulled_card = deck.pop()
        current_player_cards.append(pulled_card)
    player_turn += 1
    player_has_card = False
    if player_turn > num_of_players:
        player_turn = 1

if winner_index != 0:
    print(f"The winner is Player {winner_index} with 0 cards")
else:
    winner_index = 1
    winner_num_of_cards = len(cards[1])
    for player in range(1, num_of_players + 1):
        if len(cards[player]) < winner_num_of_cards:
            winner_index = player
            winner_num_of_cards = len(cards[player])

print(f"Player {winner_index} is the winner with {winner_num_of_cards} cards")

