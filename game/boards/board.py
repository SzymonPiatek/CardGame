from settings import settings
from game.cards.card import Card
import random


class Board():
    def __init__(self, players, cards_to_buy, dark_arts_cards, place_cards, villain_cards):
        self.players = players

        self.cards_to_buy = [Card(list(card.keys())[0]) for card in cards_to_buy]
        random.shuffle(self.cards_to_buy)
        self.dark_arts_cards = [Card(list(card.keys())[0]) for card in dark_arts_cards]
        random.shuffle(self.dark_arts_cards)
        self.place_cards = [Card(list(card.keys())[0]) for card in place_cards]
        self.villain_cards = [Card(list(card.keys())[0]) for card in villain_cards]
        random.shuffle(self.villain_cards)

        self.death_eater = 0
        self.dark_arts_cards_to_take = self.place_cards[0].effect["active_player"]["take_dark_arts_card"]

        self.player_turn_count = 0
        self.players[self.player_turn_count].active = True
        self.active_player = self.players[self.player_turn_count]

    def next_turn(self):
        self.players[self.player_turn_count].end_turn()

        self.player_turn_count += 1
        if self.player_turn_count == (len(self.players)):
            self.player_turn_count = 0

        self.active_player = self.players[self.player_turn_count]
        self.active_player.active = True
