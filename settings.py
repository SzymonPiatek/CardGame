from game.scenarios.first.scenario import each_card_for_heroes

settings = {
    "title": "Card Game",

    "card": {
        0: {
            "name": "Zaklęcie",
            "positive": True,
            "can_be_on_hand": True,
        },
        1: {
            "name": "Przedmiot",
            "positive": True,
            "can_be_on_hand": True,
        },
        2: {
            "name": "Sprzymierzeniec",
            "positive": True,
            "can_be_on_hand": True,
        },
        3: {
            "name": "Czarna magia",
            "positive": False,
            "can_be_on_hand": False,
        },
        4: {
            "name": "Czarny charakter",
            "positive": False,
            "can_be_on_hand": False,
        },
        5: {
            "name": "Miejsce",
            "positive": 0,
            "can_be_on_hand": False,
        },
    },

    "hero": {
        0: {
            "name": "Harry Potter",
            "description": "Chyba zaszłą jakaś pomyłka. Ja nie jestem żadnym czarodziejem",
            "start_deck": [
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Błyskawica": each_card_for_heroes["Błyskawica"]},
                {"Peleryna-niewidka": each_card_for_heroes["Peleryna-niewidka"]},
                {"Hedwiga": each_card_for_heroes["Hedwiga"]},
            ],
        },
        1: {
            "name": "Hermiona Granger",
            "description": "Mogliśmy wszyscy zginąć ... albo zostać wyrzuceni ze szkoły. A teraz, jeśli nie macie nic przeciwko temu, pójdę do łózka",
            "start_deck": [
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Zmieniacz czasu": each_card_for_heroes["Zmieniacz czasu"]},
                {"Baście Barda Beedle'a": each_card_for_heroes["Baście Barda Beedle'a"]},
                {"Krzywołap": each_card_for_heroes["Krzywołap"]},
            ]
        },
        2: {
            "name": "Ron Weasley",
            "description": "Co oni sobie myślą, trzymając coś takiego w szkole?",
            "start_deck": [
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Zmiatacz 11": each_card_for_heroes["Zmiatacz 11"]},
                {"Fasolki wszystkich smaków Bertiego Botta": each_card_for_heroes["Fasolki wszystkich smaków Bertiego Botta"]},
                {"Świstoświnka": each_card_for_heroes["Świstoświnka"]},
            ]
        },
        3: {
            "name": "Neville Longbottom",
            "description": "To przypominajka! Babcia wie, że wciąż o czymś zapominam, a ta kulka daje znać, że czegoś zapomniało się zrobić",
            "start_deck": [
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Alohomora": each_card_for_heroes["Alohomora"]},
                {"Przypominajka": each_card_for_heroes["Przypominajka"]},
                {"Mandragora": each_card_for_heroes["Mandragora"]},
                {"Teodora": each_card_for_heroes["Teodora"]},
            ]
        }
    },

    "color": {
        "background": (0, 0, 0),
    },

    "screen": {
        "width": 1000,
        "height": 800,
    },

    "tick": 60,
}
