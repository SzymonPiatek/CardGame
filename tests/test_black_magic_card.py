import pytest
from game.cards import BlackMagicCard
from game.player import Player, Hero


@pytest.fixture
def lord_voldemort():
    effect = {
        "active_player": {
            "hp": 1,
            "card": 2,
        },
        
        "other_players": {
            "card": 1,
        },

        "death_eater" : {
            "add": 1,
        },
    }

    return BlackMagicCard(name="Lord Voldemort", effect=effect)

@pytest.fixture
def harry():
    cards = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    ]

    return Hero(name = "Harry", cards = cards)



def test_effect_of_black_magic_card(harry, lord_voldemort):
    player = Player(harry)
    player.start()

    lord_voldemort.revealing_a_card()
