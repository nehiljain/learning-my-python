import unittest
from leetcode.solutions.s20_valid_parantheses import Solution

class TestSolution(unittest.TestCase):
  def test_valid(self):
    valid_cases = [
      '[]',
      '[{}]',
      '()',
      '({[{}]})((((()))))'
    ]
    s = Solution()
    for case in valid_cases:
      self.assertTrue(s.isValid(case))

  def test_invalid(self):
    invalid_cases = [
      '[',
      '[(])',
      '{()',
      '}()',
      '{{{{{{}}}}}}('
    ]
    s = Solution()
    for case in invalid_cases:
      self.assertFalse(s.isValid(case))
