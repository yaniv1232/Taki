

class Card:
    def __init__(self, num=None, color=None, is_change_color=False):
        self.num = num
        self.color = color
        self.change_color = is_change_color

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        if self.change_color:
            if self.color is None:
                return f"Change Color"
            else:
                return f"Change Color to {self.color}"
        else:
            return f"{self.num}-{self.color}"

