from settings import settings
from game.cards.card import Card
import random


class Player():
    def __init__(self, hero_id):
        self.hero = settings["hero"][hero_id]
        self.name = self.hero["name"]
        self.description = self.hero["description"]

        # Cards
        self.cards = [Card(list(card.keys())[0]) for card in self.hero["start_deck"]]
        self.cards_on_hand = []
        self.cards_to_draw = self.cards.copy()
        self.cards_played = []
        self.cards_player_round = []
        
        # Values
        self.hp = 10
        self.money = 0
        self.attack = 0

        # Additional
        self.active = False

        self.start()

    def start(self):
        self.cards_on_hand = random.sample(self.cards_to_draw, 5)
        self.cards_to_draw = [card for card in self.cards_to_draw if card not in self.cards_on_hand]

    def shuffle_cards(self):
        self.cards_to_draw = self.cards_played.copy()
        self.cards_played = []

    def end_turn(self):
        if self.active:
            self.active = False
            
            while len(self.cards_on_hand) != 5:
                if len(self.cards_to_draw) > 0:
                    self.take_card()
                else:
                    self.shuffle_cards()

    def check_max_hp(self, value):
        if value >= 1:
            if self.hp >= 10:
                return False
            else:
                return True
        else:
            if self.hp == 0:
                return False
            else:
                return True
            
    def check_max_card(self, value):
        if value >= 1:
            if len(self.cards_to_draw) == 0:
                return False
            else:
                return True
        else:
            if len(self.cards_on_hand) == 0:
                return False
            else:
                return True
            
    def take_card(self):
        if len(self.cards_to_draw) >= 1:
            card = self.cards_to_draw[0]
            self.cards_to_draw.remove(card)
            self.cards_on_hand.append(card)

    def identify_card(self, card_name):
        for card in self.cards_on_hand:
            if card.name == card_name:
                return card
            
    def choose_effect(self, card, effect):
        return card.effect[effect]

    def use_card(self, card, players, effect=0):
        all_players = players.copy()
        active_player = next((player for player in players if player.active), None)
        other_players = [player for player in players if not player.active]

        effect_for = False
        card_effect = None
        if len(card.effect) > 1:
            card_effect = self.choose_effect(card, effect)
        else:
            card_effect = card.effect    
        for key, values in card_effect.items():
            if key == "active_player":
                effect_for = [active_player]
            elif key == "other_players":
                effect_for = other_players
            elif key == "all_players":
                effect_for = all_players

            for new_key, new_values in values.items():
                if new_key == "hp":
                    if self.check_max_hp(new_values):
                        for player in effect_for:
                            player.hp += new_values

                elif new_key == "attack":
                    for player in effect_for:
                        player.attack += new_values

                elif new_key == "money":
                    for player in effect_for:
                        player.money += new_values

                elif new_key == "card":
                    if self.check_max_card(new_values):
                        for player in effect_for:
                            for _ in range(new_values):
                                player.take_card()

                elif new_key == "death_eater":
                    for player in effect_for:
                        pass

        self.cards_on_hand.remove(card)
        self.cards_played.append(card)
        self.cards_player_round.append(card)
