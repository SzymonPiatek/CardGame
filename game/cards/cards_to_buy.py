each_spell_card = {
    "Descendo": {
        "buy_cost": 5,
        "card_type": 0,
        "effect": {
            "active_player": {
                "attack": 2,
            }
        },
    },
    "Incendio": {
        "buy_cost": 4,
        "card_type": 0,
        "effect": {
            "active_player": {
                "attack": 1,
                "card": 1,
            }
        }
    },
    "Lumos": {
        "buy_cost": 4,
        "card_type": 0,
        "effect": {
            "all_players": {
                "card": 1,
            }
        }
    },
    "Reparo": {
        "buy_cost": 3,
        "card_type": 0,
        "effect": {
            "active_player": {
                "money": 2,
                # or card 1
            }
        }
    },
    "Wingardium leviosa": {
        "buy_cost": 2,
        "card_type": 0,
        "effect": {
            "active_player": {
                "money": 1,
                # You may place purchased item cards on top of your deck
            }
        }
    },
}

each_item_card = {
    "Eliksir wielosokowy": {
        "buy_cost": 3,
        "card_type": 1,
        "effect": {
            # Choose an ally card you played this turn. You can repeat the effect of this ally card
        }
    },
    "Esencja z dyptamu": {
        "buy_cost": 2,
        "card_type": 1,
        "effect": {
            # Any hero increases his health level by 2
        }
    },
    "Nimbus 2001": {
        "buy_cost": 5,
        "card_type": 1,
        "effect": {
            "active_player": 2,
            # If you defeat the villain you will receive 2 coins
        }
    },
    "Piłki do Quidditcha": {
        "buy_cost": 3,
        "card_type": 1,
        "effect": {
            "active_player": {
                "attack": 1,
                "hp": 1,    
            }
        }
    },
    "Tiara przydziału": {
        "buy_cost": 4,
        "card_type": 1,
        "effect": {
            "active_player": {
                "money": 2,
                # You may place purchased ally cards on top of your deck
            }
        }
    },
    "Złoty znicz": {
        "buy_cost": 5,
        "card_type": 1,
        "effect": {
            "active_player": {
                "money": 2,
                "card": 1,
            }
        }
    }
}

each_ally_card = {
    "Albus Dumbledore": {
        "buy_cost": 8,
        "card_type": 2,
        "effect": {
            "all_players": {
                "attack": 1,
                "money": 1,
                "hp": 1,
                "card": 1,
            }
        }
    },
    "Rubeus Hagrid": {
        "buy_cost": 4,
        "card_type": 2,
        "effect": {
            "active_player": {
                "attack": 1,
            },
            "all_players": {
                "hp": 1,
            }
        }
    },
    "Oliver Wood": {
        "buy_cost": 3,
        "card_type": 2,
        "effect": {
            "active_player": {
                "attack": 1,
            }
            # If you defeat the villain, any hero will increase his life level by 2
        }
    },
}

spell_cards = [
    {"Descendo": each_spell_card["Descendo"]},
    {"Descendo": each_spell_card["Descendo"]},
    {"Incendio": each_spell_card["Incendio"]},
    {"Incendio": each_spell_card["Incendio"]},
    {"Incendio": each_spell_card["Incendio"]},
    {"Incendio": each_spell_card["Incendio"]},
    {"Lumos": each_spell_card["Lumos"]},
    {"Lumos": each_spell_card["Lumos"]},
    {"Reparo": each_spell_card["Reparo"]},
    {"Reparo": each_spell_card["Reparo"]},
    {"Reparo": each_spell_card["Reparo"]},
    {"Reparo": each_spell_card["Reparo"]},
    {"Reparo": each_spell_card["Reparo"]},
    {"Reparo": each_spell_card["Reparo"]},
    {"Wingardium leviosa": each_spell_card["Wingardium leviosa"]},
    {"Wingardium leviosa": each_spell_card["Wingardium leviosa"]},
    {"Wingardium leviosa": each_spell_card["Wingardium leviosa"]},
]

item_cards = [
    {"Eliksir wielosokowy": each_item_card["Eliksir wielosokowy"]},
    {"Esencja z dyptamu": each_item_card["Esencja z dyptamu"]},
    {"Esencja z dyptamu": each_item_card["Esencja z dyptamu"]},
    {"Esencja z dyptamu": each_item_card["Esencja z dyptamu"]},
    {"Esencja z dyptamu": each_item_card["Esencja z dyptamu"]},
    {"Nimbus 2001": each_item_card["Nimbus 2001"]},
    {"Piłki do Quidditcha": each_item_card["Piłki do Quidditcha"]},
    {"Piłki do Quidditcha": each_item_card["Piłki do Quidditcha"]},
    {"Piłki do Quidditcha": each_item_card["Piłki do Quidditcha"]},
    {"Piłki do Quidditcha": each_item_card["Piłki do Quidditcha"]},
    {"Tiara przydziału": each_item_card["Tiara przydziału"]},
    {"Złoty znicz": each_item_card["Złoty znicz"]},
]

ally_cards = [
    {"Albus Dumbledore": each_ally_card["Albus Dumbledore"]},
    {"Rubeus Hagrid": each_ally_card["Rubeus Hagrid"]},
    {"Oliver Wood": each_ally_card["Oliver Wood"]},
]

cards_to_buy = spell_cards + item_cards + ally_cards

each_card_to_buy = {**each_spell_card, **each_item_card, **each_ally_card}
