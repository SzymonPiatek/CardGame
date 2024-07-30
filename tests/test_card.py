from game.cards.card import Card


def test_card_for_hero():
    new_card = Card(card_name="Alohomora")

    new_card_name = new_card.name
    new_card_type = new_card.card_type
    new_card_effect = new_card.card["effect"]
    
    print("\n")
    print(f"Name: {new_card_name}")
    print(f"Card type: {new_card_type}")
    print(f"Card effect: {new_card_effect}")

    assert new_card_name == "Alohomora"
    assert new_card_type == "Zaklęcie"
    assert new_card_effect == {
        "active_player": {
            "money": 1
        }
    }

def test_card_to_buy():
    new_card = Card(card_name="Descendo")

    new_card_name = new_card.name
    new_card_type = new_card.card_type
    new_card_effect = new_card.card["effect"]
    new_card_buy_cost = new_card.card["buy_cost"]

    print("\n")
    print(f"Name: {new_card_name}")
    print(f"Card type: {new_card_type}")
    print(f"Card effect: {new_card_effect}")
    print(f"Card buy cost: {new_card_buy_cost}")

    assert new_card_name == "Descendo"
    assert new_card_type == "Zaklęcie"
    assert new_card_effect == {
        "active_player": {
            "attack": 2
        }
    }
    assert new_card_buy_cost == 5

def test_dark_arts_card():
    new_card = Card(card_name="Expulso")

    new_card_name = new_card.name
    new_card_type = new_card.card_type
    new_card_effect = new_card.card["effect"]

    print("\n")
    print(f"Name: {new_card_name}")
    print(f"Card type: {new_card_type}")
    print(f"Card effect: {new_card_effect}")

    assert new_card_name == "Expulso"
    assert new_card_type == "Czarna magia"
    assert new_card_effect == {
        "active_player": {
            "hp": -2
        }
    }

def test_place_card():
    new_card = Card(card_name="Ulica pokątna")

    new_card_name = new_card.name
    new_card_type = new_card.card_type
    new_card_effect = new_card.card["effect"]

    print("\n")
    print(f"Name: {new_card_name}")
    print(f"Card type: {new_card_type}")
    print(f"Card effect: {new_card_effect}")

    assert new_card_name == "Ulica pokątna"
    assert new_card_type == "Miejsce"
    assert new_card_effect == {
        "active_player": {
            "take_dark_arts_card": 1,
        }
    }

def test_villain_card():
    new_card = Card(card_name="Kwiryniusz Quirrell")

    new_card_name = new_card.name
    new_card_type = new_card.card_type
    new_card_effect = new_card.card["effect"]
    new_card_prize = new_card.card["prize"]
    new_card_hp = new_card.card["hp"]

    print("\n")
    print(f"Name: {new_card_name}")
    print(f"Card type: {new_card_type}")
    print(f"Card effect: {new_card_effect}")
    print(f"Card prize: {new_card_prize}")
    print(f"Card hp: {new_card_hp}")

    assert new_card_name == "Kwiryniusz Quirrell"
    assert new_card_type == "Czarny charakter"
    assert new_card_effect == {
        "active_player": {
            "hp": -1
        }
    }
    assert new_card_prize == {
        "all_players": {
            "money": 1,
            "hp": 1,
        }
    }
    assert new_card_hp == 6
