import unittest
import MathUtils

class testMathUtils(unittest.TestCase):
    def testClass(self):
       o = MathUtils.MathUtils()
       assert o.add()== 5

unittest.main()