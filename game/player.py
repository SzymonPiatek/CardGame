import random


class Hero:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards


class Player:
    def __init__(self, hero):
        # Values
        self.hero = hero
        self.hp = 10
        self.money = 0
        self.attack = 0

        # Cards
        self.cards = self.hero.cards

        self.cards_in_hand = []
        self.cards_to_draw = []
        self.cards_played = []

        # Start
        self.start()

    def start(self):
        self.cards_in_hand = random.sample(self.cards, 5)
        self.cards_to_draw = [card for card in self.cards if card not in self.cards_in_hand]
