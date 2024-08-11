from cards import Card, WildCard, NormalCard
import random


listOfColors = ["Yellow", "Red", "Green", "Blue"]

# Normal cards aka cards from 0-9 with each color [76 total cards]
normalCards = []

# Wild cards aka cards such as +4, +2 (each color), change color, reverse (each color) and skip/block (each color) [32 total cards]
wildCards = []

# The entire deck [108 cards]
deckOfCards = []


def NormalCardCreation():
    counter = 0
    color_idx = 0

    # Apparently I can only have 4 0s inside a deck and not 8 so
    # I'll just append this to the list of normal cards
    all_the_0s = []
    for _ in range(0, 4):
        all_the_0s.append(str(NormalCard(0, listOfColors[color_idx])))
        color_idx += 1

    for i in all_the_0s:
        normalCards.append(i)
    counter = 1

    while len(normalCards) != 76:
        if color_idx >= len(listOfColors):
            color_idx = 0
        if 1 <= counter <= 9:
            normalCards.append(
                str(NormalCard(counter, listOfColors[color_idx])))
            counter += 1
        if counter > 9:
            counter = 1
            color_idx += 1


def WildCardCreation():
    counter = 0
    color_idx = 0
    # Creation of 2 Block/Skip cards per color
    while len(wildCards) != 8:
        if color_idx >= len(listOfColors):
            color_idx = 0
        if counter <= 1:
            wildCards.append(str(WildCard("Block", listOfColors[color_idx])))
            counter += 1
        if counter > 1:
            color_idx += 1
            counter = 0

    # Creation of 2 Reverse cards per color
    while len(wildCards) != 16:
        if color_idx >= len(listOfColors):
            color_idx = 0
        if counter <= 1:
            wildCards.append(
                str(WildCard("ReverseTurn", listOfColors[color_idx])))
            counter += 1
        if counter > 1:
            color_idx += 1
            counter = 0

    # Creation of 2 +2 cards per color
    while len(wildCards) != 24:
        if color_idx >= len(listOfColors):
            color_idx = 0
        if counter <= 1:
            wildCards.append(str(WildCard("+2", listOfColors[color_idx])))
            counter += 1
        if counter > 1:
            color_idx += 1
            counter = 0

    for _ in range(0, 4):
        wildCards.append(str(WildCard("+4", None)))
        wildCards.append(str(WildCard("ChangeColor", None)))


def combineAndShuffle():
    combined = normalCards + wildCards
    for i in combined:
        deckOfCards.append(i)

    random.shuffle(deckOfCards)


def main():
    NormalCardCreation()
    WildCardCreation()
    combineAndShuffle()
    # print(deckOfCards)
    # print(len(deckOfCards))


main()
