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
        number_of_players = int(input("Enter number of players (between 2 to 6): "))
    return number_of_players


def initialize_players(number_of_players, deck):
    players = []
    for i in range(number_of_players):
        name = input(f"Insert player {i} name: ")
        age = int(input(f"Insert player {i} age: "))
        cards = [deck.pop() for j in range(constants.INITIAL_AMOUNT_OF_CARDS)]
        player = Player(name, age, cards)
        players.append(player)
    players.sort(key=lambda x: x.age)
    return players


def print_game_status(players, card_on_table, deck):
    print("Game status:")
    print(f"There are {len(deck)} cards in the deck")
    print(f"Card on table is {card_on_table}")
    for player in players:
        cards_text = [str(card) for card in player.cards]
        print(f"{player.name} has {len(player.cards)} cards: {cards_text}")
    print("")


def declare_winner(players):
    winner_num_of_cards = len(players[0].cards)
    winner = players[0]
    for player in players:
        if len(player.cards) < winner_num_of_cards:
            winner = player
            winner_num_of_cards = len(player.cards)
    if not winner_num_of_cards:
        print(f"{winner.name} won with 0 cards")
    else:
        print(f"Game is over, the deck is empty. {winner.name} won with {winner_num_of_cards} cards")


def main():
    deck = initialize_deck()
    number_of_players = get_number_of_players()
    players = initialize_players(number_of_players, deck)

    card_on_table = deck.pop()
    player_turn = 0

    print(f"\n *** Game started *** \n")
    print_game_status(players, card_on_table, deck)

    while deck:
        player_has_card = False
        current_player = players[player_turn]
        for card in current_player.cards:
            if card.color == card_on_table.color or card.num == card_on_table.num:
                card_on_table = card
                current_player.cards.remove(card)
                player_has_card = True
                print(f"{current_player.name} discarded {card_on_table} (player left with {len(current_player.cards)} cards) \n")
                break
        if len(current_player.cards) == 0:
            break
        if not player_has_card:
            pulled_card = deck.pop()
            print(f"{current_player.name} pulled {pulled_card} from the deck ({len(deck)} cards left in the deck) \n")
            current_player.cards.append(pulled_card)
        player_turn += 1
        print_game_status(players, card_on_table, deck)
        if player_turn == number_of_players:
            player_turn = 0

    declare_winner(players)


if __name__ == "__main__":
    main()
