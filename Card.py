import random


class Card:
    def __init__(self):
        colors = ["Red", "Blue", "Green", "Yellow"]
        self.num = random.randrange(1, 10)
        self.color = random.choice(colors)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

