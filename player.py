from card_type import CardType
from color import Color
import random
import constants


class Player:
    def __init__(self, name, age, cards):
        self.age = age
        self.name = name
        self.cards = cards

    def try_playing_a_card(self, game):
        if self.try_playing_numeric_card_with_matching_number_or_color(game):
            return True
        elif self.try_playing_stop_card(game):
            return True
        elif self.try_playing_change_color_card(game):
            return True
        return False

    def try_playing_numeric_card_with_matching_number_or_color(self, game):
        for card in self.cards:
            if (card.color == game.card_on_table.color or card.num == game.card_on_table.num) and \
                    card.card_type == CardType.Regular_Card:
                self.put_down_card_on_table(card, game)
                return True
        return False

    def try_playing_stop_card(self, game):
        for card in self.cards:
            if card.card_type == CardType.Stop_Card and card.color == game.card_on_table.color:
                self.put_down_card_on_table(card, game)
                game.block_player()
                return True
        return False

    def try_playing_change_color_card(self, game):
        for card in self.cards:
            if card.card_type == CardType.Change_Color_Card:
                most_common_color = Color.find_most_common_color(self.cards)
                if most_common_color:
                    card.color = most_common_color
                else:
                    card.color = random.choice(constants.COLORS)  # BUG - card.color is a string
                self.put_down_card_on_table(card, game)
                return True
        return False

    def pull_card_from_deck(self, game):
        pulled_card = game.deck.pop()
        print(f"{self.name} pulled {pulled_card} from the deck ({len(game.deck)} cards left in the deck) \n")
        self.cards.append(pulled_card)

    def put_down_card_on_table(self, card, game):
        game.card_on_table = card
        self.cards.remove(card)
        print(f"{self.name} discarded {card} (player left with {len(self.cards)} cards) \n")



