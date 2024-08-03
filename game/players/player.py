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
        self.cards_on_hand = random.sample(self.cards, 5)
        self.cards_to_draw = [card for card in self.cards if card not in self.cards_on_hand]
        self.cards_played = []
        self.cards_played_round = []
        
        # Values
        self.hp = 10
        self.money = 0
        self.attack = 0

        # Additional
        self.active = False
        self.death = False

    def loss_of_life(self):
        if self.hp < 1:
            self.death = True
            cards_amount = len(self.cards_on_hand)

            if cards_amount % 2 == 0:
                cards_to_remove = int(cards_amount / 2)
            else:
                cards_to_remove = int((cards_amount - 1) / 2)

            # TODO The player must choose cards
            for _ in range(cards_to_remove):
                self.cards_on_hand.remove(self.cards_on_hand[0])

    def draw_new_hand(self):
        while len(self.cards_on_hand) != 5:
            if len(self.cards_to_draw) > 0:
                self.take_card()
            else:
                self.shuffle_cards()

    def shuffle_cards(self):
        self.cards_to_draw = self.cards_played.copy()
        self.cards_played = []

    def end_turn(self):
        if self.active:
            self.draw_new_hand()
            self.cards_played_round = []
            
    def check_max_hp(self, value):
        if self.hp == 10:
            if value > 0:
                return False
            return True
        elif 0 < self.hp < 10:
            return True
        elif self.hp < 1:
            self.loss_of_life()
            return False
            
    def check_max_card(self, value):
        if len(self.cards_to_draw) > 0:
            return True
        elif len(self.cards_played) > 0:
            self.shuffle_cards()
            self.check_max_card(value)

    def take_card(self):
        if len(self.cards_to_draw) > 0:
            card = self.cards_to_draw[0]
            self.cards_to_draw.remove(card)
            self.cards_on_hand.append(card)
        else:
            if len(self.cards_played) > 0:
                self.shuffle_cards()
                self.take_card()

    def identify_card(self, card_name):
        return next((card for card in self.cards_on_hand if card.name == card_name), None)
            
    def choose_effect(self, card, effect):
        return card.effect[effect]
    
    def apply_effect(self, effect_for, values):
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

            self.apply_effect(effect_for, values)

        self.cards_on_hand.remove(card)
        self.cards_played.append(card)
        self.cards_played_round.append(card)
