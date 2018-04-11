import re

class Card(object):
    def __init__(self, value=1, color="hearts"):
        self._value = None
        self._color = None
        self.name = None

        # Calls color.setter
        self.color = color

        # Calls value.setter
        self.value = value
        try:
            self.value = value
        except KeyError:
            raise ValueError("First argument 'value' should be a card name "
                             "or integer between 1 and 13")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color: str = "HEARTS"):
        color = color.upper()
        for c in colors:
            regexp = to_regexp(c).match(color)
            if regexp is None:
                # regexp.match returns None if nothing is matched,
                # which will raise a error if end method is used on the
                # matching result
                continue
            if regexp.end() == len(color):
                self._color = c
                break
        else:
            raise ValueError(
                "Invalid value for Card object's \"color\" member.\n" 
                "Value should be either \"HEARTS\", \"DIAMONDS\", \"CLUBS\", "
                "\"SPADES\", their singular variant, or their first letter.\n"
                "Case is not relevant.")



    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, arg):
        if isinstance(arg, str):
            self.name = arg.upper()
        elif isinstance(arg, int):
            self.name = valueToCardDict[arg]
        self._value = cardToValueDict[self.name]

    def __radd__(self, other):
        if self.name == "ACE":
            if self._value + other <= 11:
                return self._value + other + 10
        return self._value + other
    def __add__(self, other):
        if self.name == "ACE":
            if self._value + other <= 11:
                return self._value + other + 10
        return self._value + other
    def __int__(self):
        return self._value
    def __repr__(self):
        return "Card(value = %d, name = %s, color = %s)" % (self._value,
                                                            self.name,
                                                            self.color)
    def __str__(self):
        return "%s of %s" % (self.name, self.color)


cardNamesAndValues =  {
    ("ACE", 1),
    ("TWO", 2),
    ("THREE", 3),
    ("FOUR", 4),
    ("FIVE", 5),
    ("SIX", 6),
    ("SEVEN", 7),
    ("EIGHT", 8),
    ("NINE", 9),
    ("TEN", 10),
    ("JACK", 11),
    ("QUEEN", 12),
    ("KING", 13),
    }

cardToValueDict = {key : min(10,value) for (key, value) in cardNamesAndValues}
valueToCardDict = {key : value for (value, key) in cardNamesAndValues}
colors = {"HEARTS", "SPADES", "CLUBS", "DIAMONDS"}

# For example, replace "HEARTS" by "H(EART(S)?)?"
# Allows matching "H",  "HEART" and "HEARTS"
to_regexp = lambda string: re.compile(
        string[0] + "(" + string[1:-1] + "(" + string[-1] + ")?)?"
    )
