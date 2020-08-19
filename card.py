

class Card:
    def __init__(self, num=None, color=None, is_change_color=False, is_stop_card=False):
        self.num = num
        self.color = color
        self.is_change_color = is_change_color
        self.is_stop_card = is_stop_card

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        if self.is_change_color:
            if self.color:
                return f"Change Color to {self.color}"
            else:
                return f"Change Color"
        elif self.is_stop_card:
            return f"Stop Card-{self.color}"
        else:
            return f"{self.num}-{self.color}"

