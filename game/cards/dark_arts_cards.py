each_dark_arts_card = {
    "Ten którego imienia nie wolno wymawiać": {
        "card_type": 3,
        "effect": {
            "death_eater": {
                "add": 1
            }
        }
    },
    "Petryfikacja": {
        "card_type": 3,
        "effect": {
            "all_players": {
                "hp": -1,
            },
            # You cannot draw additional cards this turn
        }
    },
    "Expulso": {
        "card_type": 3,
        "effect": {
            "active_player": {
                "hp": -2,
            }
        }
    },
    "Flipendo": {
        "card_type": 3,
        "effect": {
            "active_player": {
                "hp": -1,
                "card": -1,
            }
        }
    }
}

dark_arts_cards = [
    {"Ten którego imienia nie wolno wymawiać": each_dark_arts_card["Ten którego imienia nie wolno wymawiać"]},
    {"Ten którego imienia nie wolno wymawiać": each_dark_arts_card["Ten którego imienia nie wolno wymawiać"]},
    {"Ten którego imienia nie wolno wymawiać": each_dark_arts_card["Ten którego imienia nie wolno wymawiać"]},
    {"Petryfikacja": each_dark_arts_card["Petryfikacja"]},
    {"Petryfikacja": each_dark_arts_card["Petryfikacja"]},
    {"Expulso": each_dark_arts_card["Expulso"]},
    {"Expulso": each_dark_arts_card["Expulso"]},
    {"Expulso": each_dark_arts_card["Expulso"]},
    {"Flipendo": each_dark_arts_card["Flipendo"]},
]
