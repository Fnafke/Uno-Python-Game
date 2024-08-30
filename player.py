class Player:
    def __init__(self, name):
        self.name = name

        # Each players gets an empty deck
        self.__cards = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        if len(name.strip(" ")) == 0:
            raise ValueError("Name cannot be empty")
        else:
            self.__name = name

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, deck):
        self.__cards = deck

    def add_to_deck(self, card):
        self.__cards.append(card)

    def remove_from_deck(self, card):
        if card in self.__cards:
            self.__cards.remove(card)
        else:
            raise ValueError("Card does not exit within the deck")

    def __str__(self):
        return f"{self.__name}: {self.__cards}"
