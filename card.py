

class Card:
    def __init__(self, num1, color1):
        self.num = num1
        self.color = color1

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f"Card number: {self.num}, Card color: {self.color} \n"

