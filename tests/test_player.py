import pytest
from game.heroes.player import Hero, Player



@pytest.fixture
def harry():
    cards = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    ]

    return Hero(name = "Harry", cards = cards)


def test_player_starting_deck(harry):
    player = Player(harry) 
    player.start()

    assert len(player.cards) == 10
    assert len(player.cards_in_hand) == 5
    assert len(player.cards_to_draw) == len(player.cards)- len(player.cards_in_hand)
    assert set(player.cards) == set(player.cards_in_hand + player.cards_to_draw)
