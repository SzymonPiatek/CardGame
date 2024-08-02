from game.heroes.player import Player
from game.cards.card import Card


def test_player():
    new_player = Player(hero_id=0)
    
    assert new_player.name == "Harry Potter"
    assert new_player.hp == 10
    assert new_player.money == 0
    assert new_player.attack == 0
    assert len(new_player.cards) == 10
    assert len(new_player.cards_on_hand) == 5
    assert len(new_player.cards_to_draw) == 5
    assert len(new_player.cards_played) == 0

def test_player_take_card():
    new_player = Player(hero_id=0)

    assert len(new_player.cards_on_hand) == 5
    assert len(new_player.cards_to_draw) == 5

    # First card
    new_player.take_card()

    assert len(new_player.cards_on_hand) == 6
    assert len(new_player.cards_to_draw) == 4

    # All card to draw
    new_player.take_card()
    new_player.take_card()
    new_player.take_card()
    new_player.take_card()

    assert len(new_player.cards_on_hand) == 10
    assert len(new_player.cards_to_draw) == 0

    # Test max validation
    new_player.take_card()

    assert len(new_player.cards_on_hand) == 10
    assert len(new_player.cards_to_draw) == 0

def test_player_choose_effect():
    new_player = Player(hero_id=0)
    new_card = Card(card_name="Reparo")

    new_player.active = True
    players = [new_player]

    assert len(new_player.cards_on_hand) == 5
    assert len(new_player.cards_to_draw) == 5

    new_player.cards_on_hand.append(new_card)

    assert len(new_player.cards_on_hand) == 6

    if len(new_card.effect) > 1:
        new_player.use_card(new_card, players, effect=1)
        assert len(new_player.cards_on_hand) == 6
        assert len(new_player.cards_to_draw) == 4
        assert len(new_player.cards_played) == 1
    else:
        new_player.use_card(new_card, players)
        assert len(new_player.cards_on_hand) == 5
        assert len(new_player.cards_to_draw) == 5
        assert len(new_player.cards_played) == 1
    