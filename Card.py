from enum import Enum


class Color(Enum):
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3

    def __str__(self):
        return self.name


class Name(Enum):
    TWO = [2]
    THREE = [3]
    FOUR = [4]
    FIVE = [5]
    SIX = [6]
    SEVEN = [7]
    EIGHT = [8]
    NINE = [9]
    JACK = [10]
    QUEEN = [10]
    KING = [10]
    ACE = [1, 10]

    def __str__(self):
        return self.name

    def get_value(self):
        return self.value


class Card:

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return "{} of {} with value {}".format(self.name, self.color, self.name.get_value())



