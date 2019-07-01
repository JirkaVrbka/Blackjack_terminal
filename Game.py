from Deck import Deck
from APlayer import APlayer
import logging
import UserInputUtils
from Blackjack import Blackjack


def main():
    logging.basicConfig(level=logging.DEBUG)
    print("Hello World!")
    deck = Deck()
    deck.shuffle()

    initial_money = UserInputUtils.get_positive_int_with_default(600, "How much should be initial money?")
    croupier = APlayer(100000)

    players = [APlayer(initial_money)]

    blackjack = Blackjack(croupier, players, 100)
    winners = blackjack.new_game()
    for winner in winners:
        print("A winner is: \n{}".format(winner))



if __name__ == "__main__":
    main()
