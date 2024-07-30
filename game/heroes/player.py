from settings import settings


class Hero:
    def __init__(self, hero_id):
        self.hero = settings["hero"][hero_id]
        self.name = self.hero["name"]
        self.description = self.hero["description"]
        self.cards = self.hero["start_deck"]


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

    def take_card(self):
        pass

    def use_card(self, card, players):
        all_players = players.copy()
        active_player = False
        other_players = []

        for player in players:
            if player.active:
                active_player = player
            else:
                other_players.append(player)

        effect_for = False
        for key, values in card.effect.items():
            if key == "active_player":
                effect_for = [active_player]
            elif key == "other_players":
                effect_for = other_players
            elif key == "all_players":
                effect_for = all_players

            for new_key, new_values in values.items():
                if new_key == "hp":
                    for player in effect_for:
                        player.hp += new_values
                elif new_key == "attack":
                    for player in effect_for:
                        player.attack += new_values
                elif new_key == "card":
                    for player in effect_for:
                        for _ in range(new_values):
                            player.take_card()
                elif new_key == "death_eater":
                    for player in effect_for:
                        pass
