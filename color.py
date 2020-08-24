import enum


class Color(enum.Enum):
    Red = 'red'
    Blue = 'blue'
    Green = 'green'
    Yellow = 'yellow'

    def __str__(self):
        return self.name

    @staticmethod
    def find_most_common_color(cards):
        cards_colors = [card.color for card in cards if card.color]
        if not cards_colors:
            return None
        most_common_color = max(set(cards_colors), key=cards_colors.count)
        return most_common_color


