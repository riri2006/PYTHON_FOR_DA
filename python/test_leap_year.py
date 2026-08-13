import unittest
from leap_year import is_leap_year


class TestLeapYear(unittest.TestCase):
    
    def test_divisible_by_400(self):
        """Years divisible by 400 must be leap years."""
        self.assertTrue(is_leap_year(400))
        self.assertTrue(is_leap_year(1600))
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2400))
    
    def test_divisible_by_100_not_400(self):
        """Years divisible by 100 but not 400 must NOT be leap years."""
        self.assertFalse(is_leap_year(100))
        self.assertFalse(is_leap_year(1700))
        self.assertFalse(is_leap_year(1800))
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))
        self.assertFalse(is_leap_year(2200))
        self.assertFalse(is_leap_year(2300))
        self.assertFalse(is_leap_year(2500))
    
    def test_divisible_by_4_not_100(self):
        """Years divisible by 4 but not 100 must be leap years."""
        self.assertTrue(is_leap_year(4))
        self.assertTrue(is_leap_year(2004))
        self.assertTrue(is_leap_year(2008))
        self.assertTrue(is_leap_year(2012))
        self.assertTrue(is_leap_year(2016))
        self.assertTrue(is_leap_year(2020))
        self.assertTrue(is_leap_year(2024))
    
    def test_not_divisible_by_4(self):
        """Years not divisible by 4 must NOT be leap years."""
        self.assertFalse(is_leap_year(1))
        self.assertFalse(is_leap_year(2019))
        self.assertFalse(is_leap_year(2021))
        self.assertFalse(is_leap_year(2022))
        self.assertFalse(is_leap_year(2023))
        self.assertFalse(is_leap_year(2025))


if __name__ == "__main__":
    unittest.main()
