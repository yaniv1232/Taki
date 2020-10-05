from card import Card
from card_type import CardType
from player import Player
import constants
import random


class Game:
    def __init__(self):
        self.card_on_table = None
        self.players = None
        self.deck = None
        self.player_turn = 0
        self.number_of_players = None
        self.direction_of_play = 1

    def play_game(self):
        self.initialize_deck()
        self.initialize_players_data()
        self.put_down_initial_card_on_table()
        print(f"\n *** Game has started *** \n")
        self.print_game_status()
        if self.card_on_table.card_type == CardType.Stop_Card:
            self.block_player()
        elif self.card_on_table.card_type == CardType.Switch_Direction_Card:
            self.switch_direction_of_play()
        while self.deck:
            player_played_card = False
            player = self.players[self.player_turn]
            if player.try_playing_a_card(self):
                player_played_card = True
            if not player.cards:
                break
            if not player_played_card:
                player.pull_card_from_deck(self)
            self.print_game_status()
            self.advance_to_next_player_turn()

        self.declare_winner()

    def initialize_deck(self):
        self.deck = [Card(num, color, card_type=CardType.Regular_Card) for color in constants.COLORS
                     for num in range(constants.CARD_MIN_NUMERIC_VALUE, constants.CARD_MAX_NUMERIC_VALUE)]
        self.deck += [Card(color=random.choice(constants.COLORS), card_type=CardType.Stop_Card)
                      for i in range(constants.AMOUNT_OF_STOP_CARDS)]
        self.deck += [Card(card_type=CardType.Switch_Color_Card) for i in range(constants.AMOUNT_OF_SWITCH_COLOR_CARDS)]
        for color in constants.COLORS:
            self.deck += [Card(card_type=CardType.Switch_Direction_Card, color=color)
                          for i in range(constants.AMOUNT_OF_SWITCH_DIRECTION_CARDS_PER_COLOR)]
        random.shuffle(self.deck)

    def update_number_of_players_from_user_input(self):
        while self.number_of_players not in range(constants.PLAYERS_LOWER_LIMIT, constants.PLAYERS_UPPER_LIMIT + 1):
            self.number_of_players = int(input(f'Enter number of players (between {constants.PLAYERS_LOWER_LIMIT} '
                                               f'to {constants.PLAYERS_UPPER_LIMIT}): '))

    def initialize_players_data(self):
        self.players = []
        self.update_number_of_players_from_user_input()
        for i in range(self.number_of_players):
            name = input(f"Insert player {i} name: ")
            age = int(input(f"Insert player {i} age: "))
            cards = [self.deck.pop() for j in range(constants.INITIAL_AMOUNT_OF_CARDS_PER_PLAYER)]
            player = Player(name, age, cards)
            self.players.append(player)
        self.players.sort(key=lambda x: x.age)

    def put_down_initial_card_on_table(self):
        self.card_on_table = self.deck.pop()
        while self.card_on_table.card_type == CardType.Switch_Color_Card:
            self.deck.append(self.card_on_table)
            random.shuffle(self.deck)
            self.card_on_table = self.deck.pop()
        self.card_on_table.is_initial_card = True

    def block_player(self):
        if self.card_on_table.is_the_initial_card_on_table:
            self.notify_player_was_blocked()
            self.advance_to_next_player_turn()
        else:
            self.advance_to_next_player_turn()
            self.notify_player_was_blocked()

    def notify_player_was_blocked(self):
        blocked_player = self.players[self.player_turn]
        print(f"{blocked_player.name}'s turn was blocked by a stop card\n")

    def print_game_status(self):
        print("Game status:")
        print(f"There are {len(self.deck)} cards in the deck")
        print(f"Card on table is {self.card_on_table}")
        for player in self.players:
            cards_text = [str(card) for card in player.cards]
            print(f"{player.name} has {len(player.cards)} cards: {cards_text}")
        print("")

    def advance_to_next_player_turn(self):
        self.player_turn += self.direction_of_play
        if self.player_turn >= self.number_of_players:
            self.player_turn = 0
        elif self.player_turn < 0:
            self.player_turn = self.number_of_players - 1

    def switch_direction_of_play(self):
        self.direction_of_play *= -1

    def declare_winner(self):
        winner = self.players[0]
        for player in self.players:
            if len(player.cards) < len(winner.cards):
                winner = player
        if not winner.cards:
            print(f"{winner.name} won with 0 cards")
        else:
            print(f"Game is over, the deck is empty. {winner.name} won with {len(winner.cards)} cards")