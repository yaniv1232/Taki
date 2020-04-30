from constants import CHANGE_COLOR_CARD_NUM


class Card:
    def __init__(self, num=CHANGE_COLOR_CARD_NUM, color="change color", change_color=False):
        self.num = num
        self.color = color
        self.change_color = change_color

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        if self.change_color:
            return f"Change Color"
        else:
            return f"{self.num}-{self.color}"

