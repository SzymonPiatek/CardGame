from settings import settings
from game.cards.card import Card
import random


class Hero:
    def __init__(self, hero_id):
        self.hero = settings["hero"][hero_id]
        self.name = self.hero["name"]
        self.description = self.hero["description"]
        self.cards = []

        for card in self.hero["start_deck"]:
            new_card = Card(list(card.keys())[0])
            self.cards.append(new_card)


class Player(Hero):
    def __init__(self, hero_id):
        super().__init__(hero_id)
        
        # Values
        self.hp = 10
        self.money = 0
        self.attack = 0

        # Additional
        self.active = False

        # Cards
        self.cards_on_hand = []
        self.cards_to_draw = self.cards.copy()
        self.cards_played = []
        self.cards_player_round = []

        self.start()

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

    def start(self):
        cards = random.sample(self.cards_to_draw, 5)

        for card in cards:
            self.cards_on_hand.append(card)
            self.cards_to_draw.remove(card)

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
