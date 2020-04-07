from card import Card
from color import Color
from player import Player
import constants
import random


def initialize_deck():
    deck = [Card(num, color) for color in Color for num in range(1, 10)]
    random.shuffle(deck)
    return deck


def get_number_of_players():
    number_of_players = 0
    while number_of_players not in range(constants.PLAYERS_LOWER_LIMIT, constants.PLAYERS_UPPER_LIMIT + 1):
        number_of_players_text = input("Enter number of players (between 2 to 6): ")
        number_of_players = int(number_of_players_text)
    return number_of_players


def initialize_players_details(number_of_players):
    players = []
    for i in range(number_of_players):
        name = input(f"Insert player {i} name: ")
        age_text = input(f"Insert player {i} age: ")
        age_number = int(age_text)
        cards = []
        player_details = Player(name, age_number, cards)
        players.append(player_details)
    players.sort(key=lambda player: player.age)
    return players


def print_game_status(players, card_on_table, deck):
    number_of_players = len(players)
    print("Game status:")
    print(f"There are {len(deck)} cards in the deck")
    print(f"Card on table is {card_on_table}")
    for i in range(number_of_players):
        player_num_of_cards = len(players[i].cards)
        player_name = players[i].name
        print(f"{player_name} has {player_num_of_cards} cards:", end=" ")
        print(*players[i].cards)
    print("")


def declare_winner(players, winner_index):
    winner_index = 0
    winner_num_of_cards = len(players[0].cards)
    number_of_players = len(players)
    for i in range(1, number_of_players):
        player_num_of_cards = len(players[i].cards)
        if player_num_of_cards < winner_num_of_cards:
            winner_index = i
            winner_num_of_cards = player_num_of_cards
    winner_name = players[winner_index].name
    if not winner_num_of_cards:
        print(f"{winner_name} won with 0 cards")
    else:
        print(f"Game is over, the deck is empty. {winner_name} won with {winner_num_of_cards} cards")


def main():
    deck = initialize_deck()
    number_of_players = get_number_of_players()
    players = initialize_players_details(number_of_players)

    for i in range(number_of_players):
        players[i].cards = [deck.pop() for j in range(3)]

    card_on_table = deck.pop()
    winner_index = 0
    player_turn = 0

    print(f"Game started with {number_of_players} players and {card_on_table} on the table \n")

    while deck:
        player_has_card = False
        player_name = players[player_turn].name
        player_cards = players[player_turn].cards
        player_num_of_cards = len(player_cards)
        for card in range(player_num_of_cards):
            player_current_card = player_cards[card]
            if player_current_card.color == card_on_table.color or player_current_card.num == card_on_table.num:
                card_on_table = player_current_card
                player_cards.remove(player_current_card)
                player_has_card = True
                player_num_of_cards -= 1
                print(f"{player_name} discarded {card_on_table} (player left with {player_num_of_cards} cards) \n")
                break
        if player_num_of_cards == 0:
            winner_index = player_turn
            break
        if not player_has_card:
            pulled_card = deck.pop()
            print(f"{player_name} pulled {pulled_card} from the deck ({len(deck)} cards left in the deck) \n")
            player_cards.append(pulled_card)
            player_num_of_cards += 1
        player_turn += 1
        print_game_status(players, card_on_table, deck)
        if player_turn == number_of_players:
            player_turn = 0

    declare_winner(players, winner_index)


if __name__ == "__main__":
    main()
