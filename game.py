from card import Card
from color import Color
from player import Player
import constants
import random


class Game(Player, Card):
    def __init__(self):
        self.card_on_table = None
        self.players = None
        self.deck = None

    def initialize_deck(self):
        self.deck = [Card(num, color) for color in Color for num in range(1, 10)]
        self.deck += [Card(is_change_color=True) for i in range(constants.CHANGE_COLOR_CARD_AMOUNT)]
        random.shuffle(self.deck)

    @staticmethod
    def get_number_of_players():
        number_of_players = 0
        while number_of_players not in range(constants.PLAYERS_LOWER_LIMIT, constants.PLAYERS_UPPER_LIMIT + 1):
            number_of_players = int(input("Enter number of players (between 2 to 6): "))
        return number_of_players

    def initialize_players_data(self, number_of_players):
        self.players = []
        for i in range(number_of_players):
            name = input(f"Insert player {i} name: ")
            age = int(input(f"Insert player {i} age: "))
            cards = [self.deck.pop() for j in range(constants.INITIAL_AMOUNT_OF_CARDS_PER_PLAYER)]
            player = Player(name, age, cards)
            self.players.append(player)
        self.players.sort(key=lambda x: x.age)

    def put_initial_card_on_table(self):
        self.card_on_table = self.deck.pop()
        while self.card_on_table.is_change_color:
            self.deck.append(self.card_on_table)
            random.shuffle(self.deck)
            self.card_on_table = self.deck.pop()

    @staticmethod
    def find_most_common_color(cards):
        cards_colors = [card.color for card in cards if card.color]
        if not cards_colors:
            return None
        most_common_color = max(set(cards_colors), key=cards_colors.count)
        return most_common_color

    def print_game_status(self):
        print("Game status:")
        print(f"There are {len(self.deck)} cards in the deck")
        print(f"Card on table is {self.card_on_table}")
        for player in self.players:
            cards_text = [str(card) for card in player.cards]
            print(f"{player.name} has {len(player.cards)} cards: {cards_text}")
        print("")

    def put_down_card_on_table(self, player, card):
        self.card_on_table = card
        player.cards.remove(card)
        print(f"{player.name} discarded {self.card_on_table} (player left with {len(player.cards)} cards) \n")

    def try_playing_matching_number_or_color_card(self, player):
        for card in player.cards:
            if card.color == self.card_on_table.color or card.num == self.card_on_table.num:
                self.put_down_card_on_table(player, card)
                return True
        return False

    def try_playing_change_color_card(self, player):
        for card in player.cards:
            if card.is_change_color:
                most_common_color = Game.find_most_common_color(player.cards)
                if most_common_color:
                    card.color = most_common_color
                else:
                    card.color = random.choice(Color.get_list_of_colors())
                self.put_down_card_on_table(player, card)
                return True
        return False

    def pull_card_from_deck(self, player):
        pulled_card = self.deck.pop()
        print(f"{player.name} pulled {pulled_card} from the deck ({len(self.deck)} cards left in the deck) \n")
        player.cards.append(pulled_card)

    def declare_winner(self):
        winner = self.players[0]
        for player in self.players:
            if len(player.cards) < len(winner.cards):
                winner = player
        if not winner.cards:
            print(f"{winner.name} won with 0 cards")
        else:
            print(f"Game is over, the deck is empty. {winner.name} won with {len(winner.cards)} cards")

    def play_game(self):
        self.initialize_deck()
        number_of_players = self.get_number_of_players()
        self.initialize_players_data(number_of_players)
        self.put_initial_card_on_table()
        player_turn = 0
        print(f"\n *** Game started *** \n")
        self.print_game_status()
        while self.deck:
            player_played_card = False
            player = self.players[player_turn]
            if self.try_playing_matching_number_or_color_card(player):
                player_played_card = True
            if not player_played_card and self.try_playing_change_color_card(player):
                player_played_card = True
            if not player.cards:
                break
            if not player_played_card:
                self.pull_card_from_deck(player)
            player_turn += 1
            self.print_game_status()
            if player_turn == number_of_players:
                player_turn = 0

        self.declare_winner()

