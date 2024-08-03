from game.players.player import Player
from game.boards.board import Board
from game.cards.cards_to_buy import cards_to_buy
from game.cards.place_cards import place_cards
from game.cards.villain_cards import villain_cards
from game.cards.dark_arts_cards import dark_arts_cards


def test_board():
    player_one = Player(0)
    player_two = Player(1)

    board = Board(players=[player_one, player_two], cards_to_buy=cards_to_buy, dark_arts_cards=dark_arts_cards, place_cards=place_cards, villain_cards=villain_cards)

    assert len(board.players) == 2
    assert board.cards_to_buy
    assert board.dark_arts_cards
    assert board.place_cards
    assert board.villain_cards
    assert board.death_eater == 0

    board.next_turn()

    active_player = []
    for player in board.players:
        if player.active:
            active_player.append(player)
            player.end_turn()

    assert len(active_player) == 1

    board.next_turn()

    new_active_player = []
    for player in board.players:
        if player.active:
            new_active_player.append(player)

    assert len(new_active_player) == 1
    assert new_active_player != active_player
