from challenge import regNumber
import unittest

class MyTest(unittest.TestCase):
  def test(self):
    self.assertEqual(regNumber(10, 10), 10)

"""
class SecTest(unittest.TestCase):
  def aTest(self):
    self.assertEqual(alphaString(10), None)
"""
if __name__ == '__main__':
  unittest.main()
