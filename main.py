from cards import Card, WildCard, NormalCard
from player import Player
import random


listOfColors = ["Yellow", "Red", "Green", "Blue"]

# Normal cards aka cards from 0-9 with each color [76 total cards]
normalCards = []

# Wild cards aka cards such as +4, +2 (each color), change color, reverse (each color) and skip/block (each color) [32 total cards]
wildCards = []

# The entire deck [108 cards]
deckOfCards = []

# List of players
players = []

# This is the starting card
current_card = None

# When a player does a +4 or a ColorChange, then there is a forced next color
forced_color = None

# This is the state of the game,
# I decided to do it like this because it looked fancy :P
# When the game is in progress, the game state is true. if the game is over, the state becomes false
game_state = True


def NormalCardCreation():
    counter = 0
    color_idx = 0

    # Apparently I can only have 4 0s inside a deck and not 8 so
    # I'll just append this to the list of normal cards
    all_the_0s = []
    for _ in range(0, 4):
        all_the_0s.append(NormalCard(0, listOfColors[color_idx]))
        color_idx += 1

    for i in all_the_0s:
        normalCards.append(i)
    counter = 1

    while len(normalCards) != 76:
        if color_idx >= len(listOfColors):
            color_idx = 0
        if 1 <= counter <= 9:
            normalCards.append(
                NormalCard(counter, listOfColors[color_idx]))
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
            wildCards.append(WildCard("Block", listOfColors[color_idx]))
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
                WildCard("ReverseTurn", listOfColors[color_idx]))
            counter += 1
        if counter > 1:
            color_idx += 1
            counter = 0

    # Creation of 2 +2 cards per color
    while len(wildCards) != 24:
        if color_idx >= len(listOfColors):
            color_idx = 0
        if counter <= 1:
            wildCards.append(WildCard("+2", listOfColors[color_idx]))
            counter += 1
        if counter > 1:
            color_idx += 1
            counter = 0

    for _ in range(0, 4):
        wildCards.append(WildCard("+4", None))
        wildCards.append(WildCard("ChangeColor", None))


def combineAndShuffle():
    combined = normalCards + wildCards
    for i in combined:
        deckOfCards.append(i)

    random.shuffle(deckOfCards)

# Functions first checks if the full deck of cards still has enough cards for each player,
# then it takes cards out of the full deck and distrubutes them to the player.


def distribute_cards(number_of_cards):

    # len(deckOfCards) - 1 because index 0 is also counted as a card;
    # Meaning the deck could have 12 cards but index 12 = 13th card --> out of range error
    if number_of_cards > len(deckOfCards) - 1:
        raise ValueError(
            f"The number of cards per player X amount of players exceeds the amount of cards inside the deck.")

    cards_for_player = []

    for i in range(0, number_of_cards):
        cards_for_player.append(deckOfCards.pop(i))

    return cards_for_player


def gameStart():
    amount_Of_Players = int(
        input("How many players do wish to participate?: "))
    amount_Of_Cards_Per_Player = int(input("How many cards per player?: "))

    # For each player inside of the game,
    # the amount of cards given gets distributed and they enter the game.
    for i in range(1, amount_Of_Players + 1):
        player = Player(input(f"Enter the name of Player {i}: "))

        player.cards = distribute_cards(amount_Of_Cards_Per_Player)

        players.append(player)

    print("Participants inside of the game are: ")
    for player in players:
        print(player)

    print("""
        How the game works:
          - All the players are randomly shuffled and then they each take a turn placing a card.
          - Placing cards works as follows: You give the number of the position of the card inside the deck (First card: 1)
          - A card has to match the color of the starting card.
          - If the card of other color matches the card the number of the card placed most recent than the color can be changed
          - The game ends as soon as one's deck is empty.
          """)
    print("Game begins!")

    print("""
Starting card is...
          """)

    # At the start of every game; 1 card from the deck gets placed. This card cannot be a wild card.
    global current_card
    for card in range(0, len(deckOfCards)):
        if deckOfCards[card].type == "Normal":
            current_card = deckOfCards.pop(card)
            break

    print(current_card)
    return current_card


# This is the function that runs while the game itself is busy.
def gameProgress():

    # Players are randomly shuffled so that the turns aren't dependent on which player got added first.
    random.shuffle(players)

    global game_state
    while game_state:
        winner = None

        global current_card
        global forced_color
        for player in players:
            print(f"It's {player.name}'s turn")
            print(f"Deck: {player.cards}")
            print(f"Forced color is: {forced_color}")
            print(f"Current card is: {current_card}")

            # This is the card that will end up being placed by the player
            picked_card = None

            while picked_card == None:
                if current_card.type == "Wild" and current_card.sign == "+2":
                    for i in range(0, 2):
                        player.add_to_deck(deckOfCards.pop(i))

                if current_card.type == "Wild" and current_card.sign == "+4":
                    for i in range(0, 4):
                        player.add_to_deck(deckOfCards.pop(i))
                    current_card = deckOfCards.pop(0)

                # if the player has a wild card or a card of the same color,
                # then he has a card he can place, otherwise he must take a new card from the deck
                has_card = False
                for card in player.cards:
                    if card.type == "Wild" and card.color == None:
                        has_card = True
                        break
                    if card.color == current_card.color:
                        has_card = True
                        break

                # If the player doesn't have a card, a new card gets picked from the deck.
                # If the card matches the color of the currently placed card or is a wildcard such as "ChangeColor" or "+4" then it gets placed
                # Otherwise the new card just gets added to their deck and their turn is skipped
                if has_card == False:
                    new_card = deckOfCards.pop(0)
                    print(
                        f"{player.name} has no cards to place. A new card has been automatically been added to their deck.")

                    if new_card.color == current_card.color:
                        picked_card = new_card
                        has_card = True
                    else:
                        player.add_to_deck(new_card)
                    break

                index_card = int(input("Pick your card: "))
                while index_card > len(player.cards) or index_card < 1:
                    index_card = int(input(
                        "You can't pick a number that under 1 or that is higher than the amount of cards in the deck. Pick again!: "))

                card_checked = False
                while card_checked == False:
                    if forced_color != None:
                        if player.cards[index_card-1].color == forced_color or player.cards[index_card-1].color == None:
                            card_checked = True
                            break
                        else:
                            index_card = int(
                                input("You can't pick this card! Try Again: "))

                    if player.cards[index_card-1].color == current_card.color:
                        card_checked = True
                        break
                    if player.cards[index_card-1].type == "Wild" and player.cards[index_card-1].color == None:
                        card_checked = True
                        break
                    index_card = int(
                        input("You can't pick this card! Try Again: "))

                player_card = player.cards[index_card - 1]
                player.remove_from_deck(player_card)

                if player_card.sign in ["+4", "ChangeColor"]:
                    color = int(
                        input(f"Choose a color between 1 - 4 in {listOfColors}: "))
                    forced_color = listOfColors[color-1]

                if len(player.cards) == 0:
                    winner = player.name

                picked_card = player_card

            if picked_card != None:
                current_card = picked_card

            print(f"Current card is: {current_card}")
            if winner != None:
                break


def main():
    NormalCardCreation()
    WildCardCreation()
    combineAndShuffle()
    # print(current_card)
    gameStart()
    # print(current_card)
    gameProgress()
    # print(len(deckOfCards))
    # print(deckOfCards)


main()
