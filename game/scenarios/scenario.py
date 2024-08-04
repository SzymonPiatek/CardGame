from .first import scenario as first_scenario
import random

class Scenario:
    def __init__(self, scenario_id):
        self.match_scenario(scenario_id)

        self.place_cards = first_scenario.place_cards
        random.shuffle(self.dark_arts_cards)
        random.shuffle(self.villain_cards)
        random.shuffle(self.cards_to_buy)

    def match_scenario(self, scenario_id):
        match scenario_id:
            case 0:
                self.place_cards = first_scenario.place_cards
                self.dark_arts_cards = first_scenario.dark_arts_cards
                self.villain_cards = first_scenario.villain_cards
                self.cards_to_buy = first_scenario.cards_to_buy
            case _:
                self.place_cards = []
                self.dark_arts_cards = []
                self.villain_cards = []
                self.cards_to_buy = []

