import random
from collections import Counter
from .all_heroes_list import heroes


class Hero:
    def __init__(self, hero_name):
        self.name = hero_name
        self.hero = heroes[hero_name]
        self.cards = self.hero["start_deck"]


class Player(Hero):
    def __init__(self, hero_name):
        super().__init__(hero_name)
        
        # Values
        self.hp = 10
        self.money = 0
        self.attack = 0

        # Cards
        self.cards_in_hand = []
        self.cards_to_draw = self.cards.copy()
        self.cards_played = []
