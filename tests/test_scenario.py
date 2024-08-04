import pytest
from game.scenarios.scenario import Scenario


@pytest.fixture
def scenario01():
    return Scenario(scenario_id=0)


def test_scenario_cards(scenario01):
    assert scenario01.place_cards
    assert scenario01.dark_arts_cards
    assert scenario01.villain_cards
    assert scenario01.cards_to_buy
    
    print(len(scenario01.place_cards))
    print(len(scenario01.dark_arts_cards))
    print(len(scenario01.villain_cards))
    print(len(scenario01.cards_to_buy))