import pytest
from game.players.player import Player
from game.boards.board import Board


@pytest.fixture
def board():
    player_one = Player(hero_id=0)
    player_two = Player(hero_id=1)

    return Board(players=[player_one, player_two], scenario_id=0)


def test_board_active_player(board):
    assert len(board.players) == 2
    assert board.players[board.player_turn_count].active == True
    assert board.cards_to_buy
    assert board.dark_arts_cards
    assert board.place_cards
    assert board.villain_cards
    assert board.death_eater == 0
    assert board.dark_arts_cards_to_take == 1

    # Round 1
    assert board.active_player

    assert len(board.active_player.cards_to_draw) == 5
    assert len(board.active_player.cards_on_hand) == 5
    assert len(board.active_player.cards_played) == 0

    # Variables
    before_active = board.active_player

    # Round 2
    board.next_turn()

    assert board.active_player
    assert before_active != board.active_player

    assert len(before_active.cards_to_draw) == 0
    assert len(before_active.cards_on_hand) == 5
    assert len(before_active.cards_played) == 5

    assert len(board.active_player.cards_to_draw) == 5
    assert len(board.active_player.cards_on_hand) == 5
    assert len(board.active_player.cards_played) == 0

    # Variables
    before_active = board.active_player

    # Round 3
    board.next_turn()

    assert board.active_player
    assert before_active != board.active_player

    assert len(before_active.cards_to_draw) == 0
    assert len(before_active.cards_on_hand) == 5
    assert len(before_active.cards_played) == 5

    assert len(board.active_player.cards_to_draw) == 0
    assert len(board.active_player.cards_on_hand) == 5
    assert len(board.active_player.cards_played) == 5

    # Variables
    before_active = board.active_player

    # Round 4
    board.next_turn()

    assert board.active_player
    assert before_active != board.active_player

    assert len(before_active.cards_to_draw) == 5
    assert len(before_active.cards_on_hand) == 5
    assert len(before_active.cards_played) == 0

    assert len(board.active_player.cards_to_draw) == 0
    assert len(board.active_player.cards_on_hand) == 5
    assert len(board.active_player.cards_played) == 5
