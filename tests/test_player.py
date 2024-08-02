import pytest
from game.players.player import Player
from game.cards.card import Card


@pytest.fixture()
def player_one():
    return Player(hero_id=0)

@pytest.fixture()
def player_two():
    return Player(hero_id=1)


def test_player(player_one):
    
    assert player_one.name == "Harry Potter"
    assert player_one.hp == 10
    assert player_one.money == 0
    assert player_one.attack == 0
    assert len(player_one.cards) == 10
    assert len(player_one.cards_on_hand) == 5
    assert len(player_one.cards_to_draw) == 5
    assert len(player_one.cards_played) == 0

def test_player_take_card(player_one):

    assert len(player_one.cards_on_hand) == 5
    assert len(player_one.cards_to_draw) == 5

    # First card
    player_one.take_card()

    assert len(player_one.cards_on_hand) == 6
    assert len(player_one.cards_to_draw) == 4

    # All card to draw
    player_one.take_card()
    player_one.take_card()
    player_one.take_card()
    player_one.take_card()

    assert len(player_one.cards_on_hand) == 10
    assert len(player_one.cards_to_draw) == 0

    # Test max validation
    player_one.take_card()

    assert len(player_one.cards_on_hand) == 10
    assert len(player_one.cards_to_draw) == 0

def test_player_choose_effect(player_one):
    new_card = Card(card_name="Reparo")

    player_one.active = True
    players = [player_one]

    assert len(player_one.cards_on_hand) == 5
    assert len(player_one.cards_to_draw) == 5

    player_one.cards_on_hand.append(new_card)

    assert len(player_one.cards_on_hand) == 6

    if len(new_card.effect) > 1:
        player_one.use_card(new_card, players, effect=1)
        assert len(player_one.cards_on_hand) == 6
        assert len(player_one.cards_to_draw) == 4
        assert len(player_one.cards_played) == 1
        assert len(player_one.cards_player_round) == 1
    else:
        player_one.use_card(new_card, players)
        assert len(player_one.cards_on_hand) == 5
        assert len(player_one.cards_to_draw) == 5
        assert len(player_one.cards_played) == 1
        assert len(player_one.cards_player_round) == 1

def test_player_end_turn(player_one, player_two):
    player_one.active = True
    players = [player_one, player_two]

    assert len(player_one.cards_on_hand) == 5
    assert len(player_one.cards_to_draw) == 5
    assert len(player_one.cards_played) == 0
    
    player_one.use_card(card=player_one.cards_on_hand[0], players=players)
    player_one.use_card(card=player_one.cards_on_hand[0], players=players)
    player_one.use_card(card=player_one.cards_on_hand[0], players=players)
    player_one.use_card(card=player_one.cards_on_hand[0], players=players)
    player_one.use_card(card=player_one.cards_on_hand[0], players=players)

    assert len(player_one.cards_on_hand) == 0
    assert len(player_one.cards_to_draw) == 5
    assert len(player_one.cards_played) == 5

    player_one.end_turn()

    assert player_one.active == False
    assert len(player_one.cards_on_hand) == 5
    assert len(player_one.cards_to_draw) == 0
    assert len(player_one.cards_played) == 5

def test_player_shuffle_cards(player_one):
    player_one.active = True

    assert len(player_one.cards_on_hand) == 5
    assert len(player_one.cards_to_draw) == 5
    assert len(player_one.cards_played) == 0
    assert len(player_one.cards) == 10

    player_one.cards_on_hand = []
    player_one.cards_to_draw = []
    player_one.cards_played = player_one.cards
    

    assert len(player_one.cards_on_hand) == 0
    assert len(player_one.cards_to_draw) == 0
    assert len(player_one.cards) == 10
    assert len(player_one.cards_played) == 10

    player_one.end_turn()

    assert len(player_one.cards_on_hand) == 5
    assert len(player_one.cards_to_draw) == 5
    assert len(player_one.cards_played) == 0

def test_player_death(player_one):
    player_one.active = True
    
    assert player_one.hp == 10
    assert len(player_one.cards_on_hand) == 5

    player_one.hp = 0

    player_one.check_max_hp(0)

    assert player_one.death == True
    assert len(player_one.cards_on_hand) == 3
