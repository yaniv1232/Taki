import random


class Card:
    def __init__(self):
        colors = ["Red", "Blue", "Green", "Yellow"]
        self.num = random.randrange(1, 11)
        self.color = random.choice(colors)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f"Card number: {self.num}, Card color: {self.color} \n"

