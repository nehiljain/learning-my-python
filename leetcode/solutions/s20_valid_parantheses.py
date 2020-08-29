class Solution:
    def isValid(self, s: str) -> bool:
      lefty = '{[('
      righty='}])'
      stack = []
      is_valid = True
      for ch in s:
        if not (ch in lefty + righty):
          continue
        if ch in lefty:
          stack.append(ch)
          continue
        if ch in righty and not stack:
          return False
        if (ch in righty and
            stack and
            righty.index(ch) == lefty.index(stack[-1])):
          stack.pop()
        else:
            return False

      return not stack
