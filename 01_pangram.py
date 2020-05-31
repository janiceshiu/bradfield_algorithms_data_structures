class Pangram:
  """
  A pangram is a phrase which contains every letter at least once, such as “the quick brown fox jumps over the lazy dog”.

  Write a function which determines if a given string is a pangram.

  This should be an easy problem, so it’s a good excuse to practice Polya’s method. So, please find at least three different strategies for solving this problem, proceeding through Polya’s method each time. In each case, make a note of how you came to that.
  """

  def is_pangram_1(self, phrase):
    pass

  def is_pangram_2(self, phrase):
    pass

  def is_pangram_3(self, phrase):
    pass

class TestPangram:
  """
  Tests the Pangram class
  """

  @staticmethod
  def test():
    phrases = [
      "The quick brown fox jumps over the lazy dog",
      "The quick brown fox",
      "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",
      "THE QUICK BrOWN FOX jUMPs over the LaZy Dog...",
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
      "",
      "    ",
      ")#(%*)$(*,$^"
    ]

    expected_result = [True, False, True, True, True, False, False, False]

    p = Pangram()

    is_pangram_1_result = map(p.is_pangram_1, phrases)
    assert(list(is_pangram_1_result) == expected_result)

    is_pangram_2_result = map(p.is_pangram_2, phrases)
    assert(list(is_pangram_2_result) == expected_result)

    is_pangram_3_result = map(p.is_pangram_3, phrases)
    assert(list(is_pangram_3_result) == expected_result)

TestPangram.test()
