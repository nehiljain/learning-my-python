import unittest
from collections import Counter

def validPalindrome(s: str) -> bool:
  l, r = 0, len(s) - 1
  while l < r:
    if s[l] != s[r]:
      left_sub, right_sub = s[l:r], s[l+1:r+1]
      return left_sub == left_sub[::-1] or right_sub == right_sub[::-1]
    l += 1
    r -= 1

  return True





class TestSolution(unittest.TestCase):
  def test_idea_cases(self):
    self.assertTrue(validPalindrome(s='aba'))
    self.assertTrue(validPalindrome(s='abca'))
    self.assertTrue(validPalindrome(s="aabcbaad"))


  def test_failed_cases(self):
    self.assertFalse(validPalindrome('aabbaacde'))
    self.assertFalse(validPalindrome(s='abbaaca'))
    self.assertFalse(validPalindrome(s='abbaaca'))

if __name__ == '__main__':
    unittest.main()
