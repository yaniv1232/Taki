

class Card:
    def __init__(self, num=0, color="white", change_color=False):
        self.num = num
        self.color = color
        self.change_color = change_color

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f"{self.num}-{self.color}"

