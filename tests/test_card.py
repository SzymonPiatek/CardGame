import pytest
from game.cards import Card
from game.player import Player, Hero


@pytest.fixture
def lord_voldemort():
    effect = {
        "active_player": {
            "hp": -1,
            "card": -2,
        },
        
        "other_players": {
            "card": -1,
        },

        "death_eater" : {
            "add": 1,
        },
    }

    return Card(name="Lord Voldemort", effect=effect, card_type_id=4)

@pytest.fixture
def harry():
    cards = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    ]

    return Hero(name = "Harry", cards = cards)


def test_effect_of_black_magic_card(harry, lord_voldemort):
    player = Player(harry)
    player.start()

    lord_voldemort.use_card()
