import enum


class Color(enum.Enum):
    Red = 'red'
    Blue = 'blue'
    Green = 'green'
    Yellow = 'yellow'

    def __str__(self):
        return self.name

    def get_list_of_colors(self):
        return [self.name for color in self]




