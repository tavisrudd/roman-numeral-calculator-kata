import re
from nose.tools import assert_raises, assert_equals

#from roman.calculator import *

valid_chars = 'IVXLCDM'
illegal_seqs = ('IIII', 'CD', 'DD')

class Roman(object):
    # wrapper obj just to prevent construction of illegal strings
    def __init__(self, s):
        if (any(1 for seq in illegal_seqs if seq in s)
            or not all(c in valid_chars for c in s)):
            raise ValueError(s)
        self.s = s

    def __str__(self):
        return self.s

    def __eq__(self, other):
        if isinstance(other, Roman):
            return self.s == other.s
        elif isinstance(other, basestring):
            return self.s == other
        else:
            return False

matcher = re.compile('(M*)(CM|D)?(C{0,3})(L|XC)?(X{0,3})(V|IX|IV)?(I{0,3})')

def from_roman(roman):
    (emm, cmd, cee, lxc,
     exx, vix, i) = matcher.match(roman.s).groups()
    number = 0
    number += 1000 * len(emm)
    if cmd == 'CM':
        number += 900
    elif cmd == 'D':
        number += 500
    number += 100 * len(cee)
    if lxc == 'L':
        number += 50
    elif lxc == 'XC':
        number += 90
    number += 10 * len(exx)
    if vix == 'V':
        number += 5
    elif vix == 'IX':
        number += 9
    elif vix == 'IV':
        number += 4
    number += 1 * len(i)

    return number

def to_roman(number):
    s = ""
    for r, n in zip(['M', 'CM', 'D', 'C', 'XC', 'L', 'X', 'IX', 'V', 'IV', 'I'],
                    [1000, 900, 500, 100, 90, 50, 10, 9, 5, 4, 1]):
        while number >= n:
            s += r
            number -= n
    return Roman(s)

def add_romans(a, b):
    return to_roman(from_roman(a) + from_roman(b))

def assert_roman_add(a, b, res):
    assert_equals(add_romans(Roman(a), Roman(b)), res)

def assert_illegal(s):
    assert_raises(ValueError, lambda: Roman(s))

def test_illegals():
    map(assert_illegal, illegal_seqs)

def test_simple_cases():
    assert_roman_add('I', 'I', 'II')
    assert_roman_add('I', 'II', 'III')
    assert_roman_add('II', 'I', 'III')
    assert_roman_add('M', 'M', 'MM')
    assert_roman_add('M', 'M', 'MM')

    for L in valid_chars[1:]:
        assert_roman_add('I', L, L+'I')

def test_hard_shit():
    assert_roman_add('MDCCCLXXX', 'I', 'MDCCCLXXXI')
    # 2900 + 1900
    assert_roman_add('MMCM', 'MCM', 'MMMMDCCC')
