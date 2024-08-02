import pytest
from game.cards.card import Card
from game.heroes.player import Player


@pytest.fixture()
def player_one():
    return Player(hero_id=0)

@pytest.fixture()
def player_two():
    return Player(hero_id=1)


def test_card_for_hero():
    new_card = Card(card_name="Alohomora")

    new_card_name = new_card.name
    new_card_type = new_card.card_type
    new_card_effect = new_card.card["effect"]

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

def test_use_card_for_hero(player_one, player_two):
    players = [player_one, player_two]

    # Test actual deck
    assert len(player_one.cards_on_hand) == 5

    # Simulate game
    player_one.active = True

    # Player One use card
    this_card = player_one.identify_card(card_name="Alohomora")
    player_one.use_card(card=this_card, players=players)

    # Test actual stats
    assert player_one.money == 1
    assert player_two.money == 0
    assert len(player_one.cards_on_hand) == 4
    assert len(player_one.cards_played) == 1

def test_use_card_to_buy(player_one, player_two):
    players = [player_one, player_two]

    # Cards
    card_one = Card(card_name="Descendo")

    # Add card to Player One deck
    player_one.cards_on_hand.append(card_one)

    # Test actual deck
    assert len(player_one.cards_on_hand) == 6

    # Simulate game
    player_one.active = True

    # Player One use card
    player_one.use_card(card=card_one, players=players)

    # Test actual stats
    assert player_one.attack == 2
    assert player_two.attack == 0
    assert len(player_one.cards_on_hand) == 5
    assert len(player_one.cards_played) == 1

