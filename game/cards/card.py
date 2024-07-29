from .all_cards import all_cards
from settings import settings


class Card:
    def __init__(self, card_name):
        self.name = card_name
        self.card = all_cards[card_name]

    def get_card_type_name(self):
        return settings["card"][self.card["card_type"]]["name"]
        
    def use_card(self):
        pass