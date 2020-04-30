from card import Card
from color import Color
from player import Player
import constants
import random


def initialize_deck():
    deck = [Card(num, color) for color in Color for num in range(1, 10)]
    for i in range(constants.CHANGE_COLOR_AMOUNT):
        deck.append(Card(change_color=True))
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


def find_most_common_color(cards):
    cards_colors = [card.color for card in cards if card.color != "change color"]
    most_common_color = max(set(cards_colors), key=cards_colors.count)
    return most_common_color


def put_card_on_table(deck):
    card_on_table = deck.pop()
    while card_on_table.change_color:
        deck.append(card_on_table)
        random.shuffle(deck)
        card_on_table = deck.pop()
    return card_on_table


def print_game_status(players, card_on_table, deck):
    print("Game status:")
    print(f"There are {len(deck)} cards in the deck")
    print(f"Card on table is {card_on_table}")
    for player in players:
        cards_text = [str(card) for card in player.cards]
        print(f"{player.name} has {len(player.cards)} cards: {cards_text}")
    print("")


def declare_winner(players):
    winner = players[0]
    for player in players:
        if len(player.cards) < len(winner.cards):
            winner = player
    if not len(winner.cards):
        print(f"{winner.name} won with 0 cards")
    else:
        print(f"Game is over, the deck is empty. {winner.name} won with {len(winner.cards)} cards")


def main():
    deck = initialize_deck()
    number_of_players = get_number_of_players()
    players = initialize_players(number_of_players, deck)
    card_on_table = put_card_on_table(deck)
    player_turn = 0
    print(f"\n *** Game started *** \n")
    print_game_status(players, card_on_table, deck)

    while deck:
        player_has_card = False
        player = players[player_turn]
        for card in player.cards:
            if card.color == card_on_table.color or card.num == card_on_table.num:
                card_on_table = card
                player.cards.remove(card)
                player_has_card = True
                print(f"{player.name} discarded {card_on_table} (player left with {len(player.cards)} cards) \n")
                break
        if not player_has_card:
            for card in player.cards:
                if card.change_color:
                    player_has_card = True
                    card_on_table = card
                    player.cards.remove(card)
                    print(f"{player.name} discarded {card_on_table} (player left with {len(player.cards)} cards) \n")
                    if not player.cards:
                        break
                    common_color = find_most_common_color(player.cards)
                    common_color_cards = [card for card in player.cards if card.color == common_color]
                    for common_card in common_color_cards:
                        card_on_table = common_card
                        player.cards.remove(common_card)
                        print(f"{player.name} discarded {card_on_table} (player left with {len(player.cards)} cards) \n")
        if not len(player.cards):
            break
        if not player_has_card:
            pulled_card = deck.pop()
            print(f"{player.name} pulled {pulled_card} from the deck ({len(deck)} cards left in the deck) \n")
            player.cards.append(pulled_card)
        player_turn += 1
        print_game_status(players, card_on_table, deck)
        if player_turn == number_of_players:
            player_turn = 0

    declare_winner(players)


if __name__ == "__main__":
    main()
