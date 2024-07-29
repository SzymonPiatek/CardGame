villain_cards = {
    "Kwiryniusz Quirrell": {
        "card_type": 4,
        "effect": {
            "active_player": {
                "hp": -1,
            }
        },
        "prize": {
            "all_players": {
                "money": 1,
                "hp": 1,
            }
        },
        "hp": 6,
    },
    "Crabbe i Goyle": {
        "card_type": 4,
        "effect": {
            # Whenever a hero discards a card from his hand due to the effect of a Dark Arts or Villain card, his health is reduced by 1
        },
        "prize": {
            "all_players": {
                "card": 1,
            }
        },
        "hp": 5,
    },
    "Draco Malfoy": {
        "card_type": 4,
        "effect": {
            # Each time a Death Eater is placed on a location card, the active hero reduces his life by 2
        },
        "prize": {
            "death_eater": {
                "add": -1
            }
        },
        "hp": 5,
    },
}
