class RomanNumerals:
  """
  I - 1
  V - 5
  X - 10
  L - 50
  C - 100
  D - 500
  M - 1000
  """

  def roman_to_number(self, string):
    """
    Converts a string to roman numerals.
    Assumes that everything in the string is a valid roman numeral
    Subtraction is not present. ie: IX = 9 does not exist. 9 would be XIIII

    Analysis
    Time - o(n)
    * have to iterate through the entire string once. n is the length of the string
    Space - o(1)
    * size of lookup table is constant since there is a fixed set of roman numerals
    * rest are variables that are integers
    """
    lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    acc = 0

    for c in string:
      acc += lookup[c]

    return acc

  def roman_to_number_2(self, string):
    """
    Converts a string to roman numerals.
    Assumes that everything in the string is a valid roman numeral that follows the rules below.
    Subtraction is present. ie: IX = -1+10 = 9
    Numbers go bigger to smaller unless subtraction is present.
    Not all pairs are allowed.
    * I can precede V or X
    * X can precede L or C
    * C can precede D or M
    """
    pass

class TestRomanNumerals:
  """
  Tests the Roman Numerals class
  """

  def test(self, roman_numerals_class):
    self.test_roman_to_number(roman_numerals_class)

  def test_roman_to_number(self, r):
    strings = ["I", "V", "X", "XIIII", "L", "C", "D", "M", "MMXVI"]

    expected_result = [1, 5, 10, 14, 50, 100, 500, 1000, 2016]

    result = map(r.roman_to_number, strings)
    assert(list(result) == expected_result)

  def test_roman_to_number_2(self, r):
    strings = ["I", "IV", "V", "IX", "X", "XIIII", "L", "C", "D", "M", "MCMXIV", "MMXVI"]

    expected_result = [1, 4, 5, 9, 10, 14, 50, 100, 500, 1000, 1914, 2016]

    result = map(r.roman_to_number_2, strings)
    assert(list(result) == expected_result)

test = TestRomanNumerals()
test.test(RomanNumerals())
