from Deck import Deck


class Blackjack:

    def __init__(self, croupier, players, bet):
        self.deck = Deck()
        self.croupier = croupier
        self.players = players
        self.bet = bet

    def new_game(self):
        self.deck.shuffle()
        self.__shuffle_players__()

        for player in self.players:
            player.new_game()

        actual_players = self.__get_players_with_bet__()

        # if no player to play, end game
        number_of_players = len(actual_players)
        if number_of_players == 0:
            return None

        # bank is bet from players + croupier
        bank = len(actual_players)*self.bet + 100*self.bet

        # first round to take
        self.__first_round__(actual_players)

        # players decisions
        all_player_done = False
        while not all_player_done:
            all_player_done = True
            for player in actual_players:
                if self.__player_round__(player):
                    all_player_done = False

        # splitting, double and blackjack calls
        self.__after_first_round_resolutions__()

        # croupier round
        while self.__player_round__(self.croupier):
            pass

        # cash distribution
        winners = self.__get_winners__(actual_players)
        number_of_winners = len(winners)
        single_win = bank / number_of_winners
        for winner in winners:
            winner.add_money(single_win)

        return winners

    def __get_winners__(self, players):
        winners = []
        players.append(self.croupier)
        diffs = {}

        for player in players:
            hand_value = player.best_hand_value()
            real_value = 21 - hand_value if hand_value <= 21 else 100 + hand_value
            diffs.update({player: real_value})

        minimum = min(diffs.values())
        winners = [p for p, v in diffs.items() if v == minimum]
        return winners

    def __after_first_round_resolutions__(self):
        pass

    def __player_round__(self, player):
        want_to_play_next_round = False
        if player.can_take_card() and not player.has_passed() and player.want_take_card():
            player.take_card(self.deck.get_card())
            want_to_play_next_round = True

        return want_to_play_next_round

    def __first_round__(self, players):
        self.croupier.take_card(self.deck.get_card())

        for i in range(2):
            for player in players:
                player.take_card(self.deck.get_card())

    def __get_players_with_bet__(self):
        return [p for p in self.players if p.bet(self.bet) is True]

    def __shuffle_players__(self):
        import random
        if len(self.players) > 1:
            random.shuffle(self.players)
