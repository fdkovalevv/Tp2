import random
import unittest
from Name_function import _min
from Name_function import _max
from Name_function import _sum
from Name_function import _mult
from Name_function import _pop

class Testclass(unittest.TestCase):
    def test_min(self):
        a = []
        for i in range(1, 1000):
            a.append(random.randint(-10 ^ 20, 10 ^ 20))
        self.assertEqual(_min(a), min(a))
    def test_max(self):
        a = []
        for i in range(1, 1000):
            a.append(random.randint(-10 ^ 20, 10 ^ 20))
        self.assertEqual(_max(a), max(a))
    def test_sum(self):
        a = []
        for i in range(1, 1000):
            a.append(random.randint(-10 ^ 20, 10 ^ 20))
        self.assertEqual(_sum(a), sum(a))
    def test_mult(self):
        a = []
        for i in range(1, 1000):
            a.append(random.randint(-10 ^ 20, 10 ^ 20))
        mult = 1
        for i in a:
            mult *= i
        self.assertEqual(_mult(a), mult)
    def test_p(self):
        a = []
        for i in range(1, 1000):
            a.append(random.randint(-10 ^ 20, 10 ^ 20))
        _p = 0
        for i in a:
            _p += i**2
        self.assertEqual(_pop(a), _p)

if __name__ == '__main__':
    unittest.main()
