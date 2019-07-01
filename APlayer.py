from abc import ABC, abstractmethod
import logging


class APlayer(ABC):
    global __id_generator
    __id_generator = 0

    def __init__(self, money):
        self.logger = logging.getLogger(__name__)
        self.id = APlayer.__get_id__()
        self.current_money = money
        self.hand = []

    def take_card(self, card):
        self.logger.info("Player {} takes card {}".format(self.id, card))

        self.hand.append(card)

    def values_of_hand(self):
        values = [0]

        for card in self.hand:
            values = APlayer.__combine_arrays__(values, card.name.get_value())

        return values

    def can_take_card(self):
        return len(self.hand) < 6

    @staticmethod
    def __combine_arrays__(base_values, new_values):
        new_base_values = []

        for base_value in base_values:
            for new_value in new_values:
                new_base_values.append(base_value + new_value)

        return new_base_values

    @staticmethod
    def __get_id__():
        global __id_generator
        __id_generator += 1
        return __id_generator - 1

    def __str__(self):
        string = "Player {} with hand value of {} with cards:\n[\n".format(self.id, self.values_of_hand())
        for card in self.hand:
            string += "\t"
            string += card.__str__()
            string += "\n"
        string += "]"
        return string


