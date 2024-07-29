from .cards_for_heroes import cards_for_heroes
from .cards_to_buy import cards_to_buy
from .dark_arts_cards import dark_arts_cards
from .place_cards import place_cards
from .villain_cards import villain_cards


all_cards = {card_name: card_details for card_dict in [cards_for_heroes, dark_arts_cards, place_cards, villain_cards, cards_to_buy] for card_name, card_details in card_dict.items()}
