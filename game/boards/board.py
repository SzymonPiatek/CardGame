from settings import settings
from game.cards.card import Card


class Board():
    def __init__(self, players, cards_to_buy, dark_arts_cards, place_cards, villain_cards):
        self.players = players

        self.cards_to_buy = [Card(list(card.keys())[0]) for card in cards_to_buy]
        self.dark_arts_cards = [Card(list(card.keys())[0]) for card in dark_arts_cards]
        self.place_cards = [Card(list(card.keys())[0]) for card in place_cards]
        self.villain_cards = [Card(list(card.keys())[0]) for card in villain_cards]

        self.death_eater = 0

        self.player_turn_count = 0

    def next_turn(self):
        if self.player_turn_count == (len(self.players)):
            self.player_turn_count = 0

        self.players[self.player_turn_count].active = True
        self.player_turn_count += 1
