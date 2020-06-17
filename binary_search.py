class BinarySearch():
  """
  Hashing and binary search both address the same problem: finding an item in a collection. What are some trade-offs between the two strategies?
  * You can only use binary search on something you're able to sort by some sort of metric. You can use hashing on almost anything, possibly? since theoretically you could use pointers to point to whatever it is. and if it's a whole object perhaps you hash the memory location? I'm not sure, actually, and now that I mention it I wonder how that is done for languages that allow say, values to be entire objects.
  * Assuming stuff in the collection doesn't change, hashing might be faster to look stuff up because it's a constant o(1) time amortized, but binary search is generally log n.

  When might you want to pick one over the other?
  If sorting takes (at minimum) O(n log n) time, and binary search takes O(log n) time, under what circumstances might it worth it to sort a collection in order to perform binary search?
  * When the number of times you need to sort it is far less than the number of times you need to search. There's probably some mathematical formula one can come up with, but I'm not sure. I suppose if you binary search X times, that's O(X log n) time total. And sorting once is O(n log n). so you have O((X+n) log n) time where X is the number of times you binary search the sorted list and n is the number of items in the list. And you'd probably have to add this up over the number of times you say, re-sort the list. Take into account the number of new items, the number of times you'll search on this newly sorted list, etc. If the list is really small or really large and only looked up once or twice, linear search in O(n) time is probably more worth it. In those cases constants probably come into play.
  * I'd really like to know if there is some mathematical way you can calculate whether it is more worth it to sort + search or just do linear search, which is O(n) time, or do hashing.
  """
  def binary_search(self, arr, target):
    """
    takes a sorted array and a target
    returns {num_of_searches, list_of_indexes_searched, True/False}
    depending on whether the target is in the list
    """

    low = 0
    hi = len(arr) - 1
    med = (low + hi) // 2
    info = {
      "arr": arr,
      "num_searches": 0,
      "idxs_searched": [],
      "target": target,
      "target_found": False,
      "target_idx": None
    }

    while low <= hi:
      print(f'low: {low}, med: {med}, hi: {hi}')
      num = arr[med]
      info["num_searches"] += 1
      info["idxs_searched"].append(med)
      if num > target:
        # discard top half of the array
        hi = med - 1
        med = (low + hi) // 2
      elif num < target:
        # discard bottom half of the array
        low = med + 1
        med = (low + hi) // 2
      else: # num == target:
        info["target_found"] = True
        info["target_idx"] = med
        return info

    print(f'terminated loop. low: {low}, med: {med}, hi: {hi}')
    return info

a = BinarySearch()
print(a.binary_search([5,10,15,20,25], 1))
print(a.binary_search([5,10,15,20,25], 5))
print(a.binary_search([5,10,15,20,25], 10))
print(a.binary_search([5,10,15,20,25], 55))

print(a.binary_search([5,10,15,20,25,30], 1))
print(a.binary_search([5,10,15,20,25,30], 5))
print(a.binary_search([5,10,15,20,25,30], 100))

