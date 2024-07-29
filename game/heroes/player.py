import random
from all_heroes_list import heroes


class Hero:
    def __init__(self, hero_name):
        self.name = hero_name
        self.hero = heroes[hero_name]


class Player(Hero):
    def __init__(self, hero_name):
        super().__init__(hero_name)
        
        # Values
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
