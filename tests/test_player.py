from game.heroes.player import Player


def test_player():
    new_player = Player(hero_id=0)
    new_player_cards = [list(card.keys())[0] for card in new_player.cards]
    
    print("\n")
    print(f"Name: {new_player.name}")
    print(f"Hero: {new_player.hero}")
    print(f"Hp: {new_player.hp}")
    print(f"Money: {new_player.money}")
    print(f"Attack: {new_player.attack}")
    print(f"Cards: {new_player_cards}")

    assert new_player.name == "Harry Potter"
    assert new_player.hp == 10
    assert new_player.money == 0
    assert new_player.attack == 0
    assert len(new_player.cards) == 10
    assert len(new_player.cards_on_hand) == 5
    assert len(new_player.cards_to_draw) == 5
    assert len(new_player.cards_played) == 0
