import unittest

def add(a, b):
    return a + b

class TestMathOperation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__=="__main__":
    unittest.main()