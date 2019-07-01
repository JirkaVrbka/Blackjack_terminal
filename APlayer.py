from abc import ABC, abstractmethod
import logging


class APlayer(ABC):
    global __id_generator
    __id_generator = 0

    def __init__(self, money):
        self.logger = logging.getLogger(__name__)
        self.id = APlayer.__get_id__()
        self.current_money = money
        self.passed = False
        self.hand = []

    def take_card(self, card):
        self.logger.info("Player {} takes card {}".format(self.id, card))

        self.hand.append(card)

    def values_of_hand(self):
        values = [0]

        for card in self.hand:
            values = APlayer.__combine_arrays__(values, card.name.get_value())

        return values

    def best_hand_value(self):
        best_value = 1000
        for value in self.values_of_hand():
            if value == 21 \
                    or value < 21 < best_value \
                    or 21 < value < best_value \
                    or best_value < value < 21:
                best_value = value
        return best_value

    def add_money(self, money):
        self.current_money += money

    def new_game(self):
        self.passed = False
        self.hand = []

    def pass_round(self):
        self.passed = True

    def has_passed(self):
        return self.passed

    def can_take_card(self):
        return len(self.hand) < 6

    def bet(self, bet):
        if self.current_money > bet:
            self.current_money -= bet
            return True
        else:
            return False

    def want_take_card(self):
        return self.best_hand_value() < 20

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

