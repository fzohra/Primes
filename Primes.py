__author__ = 'Fatimah Zohra'

# ----------
# Prime.py
# ----------

from math import sqrt
from unittest import main, TestCase


def is_prime(n):
    assert n > 0
    if (n == 2):
        return True
    if (n != 1) and (n % 2 != 0):
        for i in range(3, int(sqrt(n)) + 1, 2):
            if(n % i == 0):
                return False
        return True
    return False

class MyUnitTests (TestCase) :
    def test_1 (self) :
        self.assertFalse(is_prime(1))

    def test_2 (self) :
        self.assertTrue(is_prime(2))

    def test_3 (self) :
        self.assertTrue(is_prime(3))

    def test_4 (self) :
        self.assertFalse(is_prime(4))

    def test_5 (self) :
        self.assertTrue(is_prime(5))

    def test_6 (self) :
        self.assertTrue(is_prime(7))

    def test_7 (self) :
        self.assertFalse(is_prime(9))

    def test_8 (self) :
        self.assertFalse(is_prime(27))

    def test_9 (self) :
        self.assertTrue(is_prime(29))


if __name__ == "__main__" :
    main()