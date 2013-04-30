class RomanNumeral(object):
    mapping = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}

    def __init__(self, value):
        self.value = value

    def to_int(self):
        return 1

    def _parse(self, value):
        current = None
        for char in value.reverse():
            if current is None:
                current = self.mapping[char]
            else:
                current -= self.mapping[char]
        return current



