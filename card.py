import random
from color import Color


class Card:
    def __init__(self):
        self.num = random.randrange(1, 11)
        colors = list(Color.__members__.values())
        self.color = random.choice(colors).name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f"Card number: {self.num}, Card color: {self.color} \n"

