each_card_for_heroes = {
    "Alohomora": {
        "card_type": 0,
        "effect": {
            "active_player": {
                "money": 1,
            }
        },
    },
    "Błyskawica": {
        "card_type": 1,
        "effect": {
            "active_player": {
                "active_player": {
                    "attack": 1
                    # If you defeat the villain you will receive 1 coin
                }
            }
        }
    },
    "Peleryna-niewidka": {
        "card_type": 1,
        "effect": {
            "active_player": {
                "money": 1,
                # If you have this card in your hand, the effect of any Dark Arts or Villain card cannot reduce your health by more than 1.
            }
        }
    },
    "Hedwiga": {
        "card_type": 2,
        "effect": {
            "active": {
                "attack": 1,
                # or hp 2
            }
        }
    },
    "Zmiatacz 11": {
        "card_type": 1,
        "effect": {
            "active_player": {
                "active_player": {
                    "attack": 1
                    # If you defeat the villain you will receive 1 coin
                }
            }
        }
    },
    "Fasolki wszystkich smaków Bertiego Botta": {
        "card_type": 1,
        "effect": {
            "active_player": {
                "money": 1,
                # You gain 1 attack for each ally card played this turn
            }
        }
    },
    "Świstoświnka": {
        "card_type": 2,
        "effect": {
            "active": {
                "attack": 1,
                # or hp 2
            }
        }
    },
    "Przypominajka": {
        "card_type": 1,
        "effect": {
            "active_player": {
                "active_player": {
                    "money": 1
                    # If you discard this card you will receive 2 coins
                }
            }
        }
    },
    "Mandragora": {
        "card_type": 1,
        "effect": {
            "active_player": {
                "attack": 1,
                # or any hero increases his health by 2
            }
        }
    },
    "Teodora": {
        "card_type": 2,
        "effect": {
            "active": {
                "attack": 1,
                # or hp 2
            }
        }
    },
    "Zmieniacz czasu": {
        "card_type": 1,
        "effect": {
            "active_player": {
                "active_player": {
                    "money": 1
                    # You may place purchased spell cards on top of your deck instead of in your discard pile
                }
            }
        }
    },
    "Baście Barda Beedle'a": {
        "card_type": 1,
        "effect": {
            "active_player": {
                "money": 2,
                # or all heroes receive 1 coin
            }
        }
    },
    "Krzywołap": {
        "card_type": 2,
        "effect": {
            "active": {
                "attack": 1,
                # or hp 2
            }
        }
    }
}
