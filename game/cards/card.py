from .all_cards import each_card
from settings import settings


class Card:
    def __init__(self, card_name):
        self.name = card_name
        self.card = each_card[card_name]
        self.card_type = settings["card"][self.card["card_type"]]["name"]
        self.positive = settings["card"][self.card["card_type"]]["positive"]
        self.on_hand = settings["card"][self.card["card_type"]]["on_hand"]

    def use_card(self):
        pass
    