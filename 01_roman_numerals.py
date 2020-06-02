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
    """
    lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    acc = 0

    for c in string:
      acc += lookup[c]

    return acc



class TestRomanNumerals:
  """
  Tests the Roman Numerals class
  """

  @staticmethod
  def test():
    strings = ["I", "V", "X", "XIIII", "L", "C", "D", "M", "MMXVI"]

    expected_result = [1, 5, 10, 14, 50, 100, 500, 1000, 2016]

    r = RomanNumerals()

    result = map(r.roman_to_number, strings)
    assert(list(result) == expected_result)

TestRomanNumerals.test()
