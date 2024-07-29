from .cards_to_buy import cards_to_buy, each_spell_card, each_ally_card, each_item_card
from .dark_arts_cards import dark_arts_cards, each_dark_arts_card
from .villain_cards import villain_cards, each_villain_card
from .cards_for_heroes import each_card_for_heroes
from .place_cards import place_cards, each_place_card


all_cards = cards_to_buy + dark_arts_cards + villain_cards + place_cards
each_card = {**each_spell_card, **each_ally_card, **each_item_card, **each_dark_arts_card, **each_villain_card, **each_card_for_heroes, **each_place_card}