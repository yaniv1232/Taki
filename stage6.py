from card import Card
from color import Color
import constants


def initialize_deck():
    new_deck = [Card(num, color) for color in Color for num in range(1, 10)]
    return new_deck


def get_number_of_players():
    temp_number_of_players = 0
    while temp_number_of_players not in range(constants.PLAYERS_LOWER_LIMIT, constants.PLAYERS_UPPER_LIMIT + 1):
        number_of_players_text = input("Enter number of players (between 2 to 6): ")
        temp_number_of_players = int(number_of_players_text)
    return temp_number_of_players


def initialize_players_to_cards(number_of_players1):
    temp_players_to_cards = {}
    for player1 in range(1, number_of_players1 + 1):
        temp_players_to_cards[player1] = [deck.pop() for j in range(3)]
    return temp_players_to_cards


deck = initialize_deck()
number_of_players = get_number_of_players()
players_to_cards = initialize_players_to_cards(number_of_players)

card_on_table = deck.pop()
winner_index = 0
player_turn = 1

while deck:
    player_has_card = False
    current_player_cards = players_to_cards[player_turn]
    current_player_num_of_cards = len(current_player_cards)
    for card in range(current_player_num_of_cards):
        player_current_card = current_player_cards[card]
        if player_current_card.color == card_on_table.color or player_current_card.num == card_on_table.num:
            card_on_table = player_current_card
            current_player_cards.remove(player_current_card)
            player_has_card = True
            current_player_num_of_cards -= 1
            break
    if current_player_num_of_cards == 0:
        winner_index = player_turn
        break
    if not player_has_card:
        pulled_card = deck.pop()
        current_player_cards.append(pulled_card)
        current_player_num_of_cards += 1
    player_turn += 1
    if player_turn > number_of_players:
        player_turn = 1

if winner_index:
    print(f"The winner is Player {winner_index} with 0 cards")
else:
    winner_index = 1
    winner_num_of_cards = len(players_to_cards[1])
    for player in range(1, number_of_players + 1):
        player_num_of_cards = players_to_cards[player]
        if len(player_num_of_cards) < winner_num_of_cards:
            winner_index = player
            winner_num_of_cards = len(player_num_of_cards)
    print(f"Player {winner_index} is the winner with {winner_num_of_cards} cards")

