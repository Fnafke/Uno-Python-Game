from abc import ABC


class Card(ABC):
    @property
    def type(self):
        pass

    @property
    def sign(self):
        pass

    @sign.setter
    def sign(self, sign):
        pass

    @property
    def color(self):
        pass

    @color.setter
    def color(self, color):
        pass

    @staticmethod
    def checkColor(color):
        colors = ["yellow", "red", "blue", "green"]

        if color.lower() in colors:
            return True
        else:
            return False

    def __str__(self):
        pass


class WildCard(Card):
    def __init__(self, sign, color):
        self.__type = "Wild"
        self.sign = sign
        self.color = color

    @property
    def type(self):
        return self.__type

    @property
    def sign(self):
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        allowed_signs = ["+4", "+2", "changecolor", "block", "reverseturn"]

        if sign.lower() in allowed_signs:
            self.__sign = sign
        else:
            raise ValueError(
                "Signs for Wild Cards must be '+4', '+2', 'ChangeColor', 'Block', 'ReverseTurn'")

# "The Wild Cards '+4', 'ChangeColor' have no assigned color, so they must be 'None'"
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        signs = ["+4", "changecolor"]

        if color != None and not Card.checkColor(color):
            raise ValueError("Cards must be: Yellow, Green, Blue, Red")

        if self.__sign.lower() not in signs and color != None:
            self.__color = color
            return

        if self.__sign.lower() in signs and color != None:
            raise ValueError(
                "The Wild Cards '+4', 'ChangeColor' have no assigned color, so they must be 'None'")
        else:
            self.__color = None

    def __str__(self):
        # return f"Type: {self.__type}, Sign: {self.__sign}, Color: {self.__color}"
        if self.__sign.lower() in ["+4", "changecolor"]:
            return self.__sign
        return f"{self.__color} {self.__sign}"

    def __repr__(self):
        if self.__sign.lower() in ["+4", "changecolor"]:
            return self.__sign
        return f"{self.__color} {self.__sign}"


class NormalCard(Card):
    def __init__(self, sign, color):
        self.__type = "Normal"
        self.sign = sign
        self.color = color

    @property
    def type(self):
        return self.__type

    @property
    def sign(self):
        return self.__sign

    @sign.setter
    def sign(self, sign: int):
        if 0 <= sign <= 9:
            self.__sign = sign
        else:
            raise ValueError(
                "Normal cards must be have a sign/number from 0-9")

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color == None:
            raise ValueError("Color for normal cards can't be None")

        if not Card.checkColor(color):
            raise ValueError("Cards must be: Yellow, Green, Blue, Red")

        self.__color = color

    def __str__(self):
        # return f"Type: {self.__type}, Sign: {self.__sign}, Color: {self.__color}"
        return f"{self.__color} {self.__sign}"

    def __repr__(self):
        return f"{self.__color} {self.__sign}"
