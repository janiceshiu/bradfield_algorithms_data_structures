class Pangram:
  """
  A pangram is a phrase which contains every letter at least once, such as “the quick brown fox jumps over the lazy dog”.

  Write a function which determines if a given string is a pangram.

  This should be an easy problem, so it’s a good excuse to practice Polya’s method. So, please find at least three different strategies for solving this problem, proceeding through Polya’s method each time. In each case, make a note of how you came to that.
  """

  def is_pangram_1(self, phrase):
    """
    Determines whether a given string is a pangram
    Time analysis references https://wiki.python.org/moin/TimeComplexity
    where possible

    Overall
    * time - o(n^2)? Due to the possible nested o(n) calculations in the for loop?
    * space - o(1) cos everything in the function requires constant space
    * although if we take storage of the phrase into account then o(n) where n
    * is length of the phrase

    Function may terminate early if `phrase` is a pangram and all alphabets are
     reached before the phrase ends
    """
    # time - o(1)
    # space - o(1)
    # o(26) constant space and time, since the number of ascii lowercase
    # characters is constant - 26. so o(1) * 26 = o(26)
    # which simplifies back to o(1)
    alpha = set('abcdefghijklmnopqrstuvwxyz')

    # overall loop
    # time - o(n^2)?
    # * o(n) `for c in phrase`
    # * within that, another o(n) for `len(alpha)`?
    # space - o(1)?
    # * just a fixed number of temporary variables that are ints or chars?
    # * alpha doesn't get any bigger, always smaller or the same size

    # `c in phrase`
    # time - o(n).
    # * is o(1) done max n times, so o(n) where n is the number of characters
    # in `phrase`
    # space - o(1)? constant?
    # * since c is a temporary variable
    for c in phrase:
      # o(1) constant time and space?
      # does set.discard take constant time and space?
      alpha.discard(c.lower())

      # not sure about time and space.
      # time - o(n)?
      # * is length of the set calculated everytime or is it stored in a
      # variable somewhere?
      # * if calculated every time, then o(n) linear time to calculate the l
      # length of the set.
      # space - o(1)?
      # * probably constant, just a single comparison?
      # * may not need to go through the whole phrase if the phrase is a
      # pangram and all alphabets are reached before the phrase ends
      if len(alpha) == 0:
        return True

    return False

  def is_pangram_2(self, phrase):
    """
    Determines whether a given string is a pangram
    Time analysis references https://wiki.python.org/moin/TimeComplexity
    where possible

    Overall
    * time - o(n). `for c in phrase` runs a max of n times where n is length
     of `phrase`
    * space - o(1) cos everything in the function requires constant space
    * although if we take storage of `phrase` into account then o(n) where n
    * is length of the phrase

    Function may terminate early if `phrase` is a pangram and all alphabets are
     reached before the phrase ends

    The only difference from is_pangram_1 is that `len(alpha) == 0` becomes
    `alpha == set()`
    """
    # time - o(1)
    # space - o(1)
    # o(26) constant space and time, since the number of ascii lowercase
    # characters is constant - 26. so o(1) * 26 = o(26)
    # which simplifies back to o(1)
    alpha = set('abcdefghijklmnopqrstuvwxyz')

    # overall loop
    # time - o(n)
    # * o(n) `for c in phrase`
    # space - o(1)?
    # * just a fixed number of temporary variables that are ints or chars?
    # alpha doesn't get any bigger, always smaller or the same size

    # `c in phrase`
    # time - o(n).
    # * is o(1) done max n times, so o(n) where n is the number of characters
    # in `phrase`
    # space - o(1)? constant?
    # * since c is a temporary variable
    for c in phrase:
      # o(1) constant time and space?
      # does set.discard take constant time and space?
      alpha.discard(c.lower())

      # o(1) time and space probably - just a single comparison?
      # may not need to go through the whole phrase if the phrase is a pangram
      # and all alphabets are reached before the phrase ends
      if alpha == set():
        return True

    return False

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
