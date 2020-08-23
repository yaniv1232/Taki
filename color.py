import enum


class Color(enum.Enum):
    Red = 'red'
    Blue = 'blue'
    Green = 'green'
    Yellow = 'yellow'

    def __str__(self):
        return self.name




