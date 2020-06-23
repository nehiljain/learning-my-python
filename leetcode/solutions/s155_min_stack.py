class MinStack:

    def __init__(self):
      """
      initialize your data structure here.
      """
      self._data = []
      self._min = None

    @property
    def _is_empty(self) -> bool:
      return self._data == []

    def push(self, x: int) -> None:
      if self._is_empty:
        self._min = x
      else:
        self._min = min(x, self._min)
      self._data.append(x)

    def _find_min(self):
        if self._is_empty:
            return None
        r = self._data[-1]
        for item in self._data:
            r = min(item, r)
        return r

    def pop(self) -> None:
      if self._is_empty:
        raise Exception('Empty stack, nothing to pop')

      result = self._data.pop()
      if self._min == result:
            self._min = self._find_min()
      return result

    def top(self) -> int:
      if self._is_empty:
        raise Exception('Empty stack')
      return self._data[-1]


    def getMin(self) -> int:
      if self._is_empty:
        raise Exception('Empty stack')
      return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


