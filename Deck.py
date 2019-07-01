from Card import Card, Color, Name


class Deck:

    def __init__(self):
        self.deck = []
        self.__generate_deck__()

    def __generate_deck__(self):
        for color in Color:
            for name in Name:
                self.deck.append(Card(color, name))

    def shuffle(self):
        import random
        random.shuffle(self.deck)

        for i in range(random.randint(20,40)):
            self.deck.append(self.deck.pop(0))

    def get_card(self):
        return self.deck.pop(0)

    def __str__(self):
        deck_string = ""
        for card in self.deck:
            deck_string += card.__str__()
            deck_string += "\n"
        return deck_string





