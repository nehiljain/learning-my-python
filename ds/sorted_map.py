from ds import map_base

class SortedMap(MapBase):
  def __init__(self, n=101, p=3):
    self._table = n * [None]


  def _find_index(self, k, low, high):
    '''return the left most index of the key which is greater than or equal to k
    Algo:
    look at the mid point
    if mid point is greater than
    '''

    if high < low:
      return high + 1
    else:
      mid = (high + low) // 2

      if k == self._table[mid]['key']:
        return mid
      elif k < self._table[mid]['key']:
        return self._find_index(k, low, mid - 1)
      else:
        return self._find_index(k, mid + 1, high)

  def
