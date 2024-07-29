from settings import settings


class Card:
    def __init__(self, name, effect, card_type_id):
        self.name = name,
        self.effect = effect
        self.card_type = settings["card"][card_type_id]

    def use_card(self):
        for key, values in self.effect.items():
            for new_key, value in values.items():
                print(f"{key}: {new_key} {value}")
