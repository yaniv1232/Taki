from card_type import CardType


class Card:
    def __init__(self, num=None, color=None, card_type=None):
        self.num = num
        self.color = color
        self.card_type = card_type

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        if self.card_type == CardType.Change_Color_Card:
            if self.color:
                return f"Change Color to {self.color}"
            else:
                return f"Change Color"
        elif self.card_type == CardType.Stop_Card:
            return f"Stop Card-{self.color}"
        else:
            return f"{self.num}-{self.color}"

