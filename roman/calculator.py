class RomanNumeral(object):
    mapping = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}

    def __init__(self, roman):
	if isinstance(roman, int):
	    self.value = roman
        else:
            self.value = self._parse(roman)

    def _parse(self, value):
        last = None
	res = 0
        for current in value:
            i = self.mapping[current]
	    if last is not None:
                if last < i:
                    res -= last
                else:
                    res += last
            last = i
        res += last
        return res

    def __add__(self, other):
        return RomanNumeral(self.value + other.value)

    ones = ['I', 'X', 'C', 'M']
    fives = ['V', 'L', 'D']
    
#    def _roman_digit(self, power, digit):
#        if 0 <= digit <= 3S

#    def __str__(self):
#        num = self.key

