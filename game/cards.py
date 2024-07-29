'''

effect = {
    "active_player": {
        "hp": 1,
        "card": 1,
    },

    "other_players": {
        "hp": 0,
        "card": 0,
    },

    "all_players": {
        "hp": 0,
        "card": 0
    },

    "death_eater": {
        "add": 0,
    },
}

'''
  

class BlackMagicCard:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def revealing_a_card(self):
        for key, values in self.effect.items():
            if key == "active_player":
                for new_key, value in values.items():
                    print(f"Active player: {new_key} {value} " )
            if key == "other_players":
                for new_key, value in values.items():
                    print(f"Other players: {new_key} {value} ")
            if key == "all_players":
                for new_key, value in values.items():
                    print(f"All players: {new_key} {value} ")
            if key == "death_eater":
                for new_key, value in values.items():
                    print(f"Death eater: {new_key} {value}")